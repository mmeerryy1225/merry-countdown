"""days/*.json 을 한꺼번에 렌더링 → out/날짜/01~05.png + caption.txt + preview.png
사용: python batch.py 2026-10-02 2026-10-08
"""
import sys, json
from pathlib import Path
from PIL import Image
from render_cards import render

CLOSING = """
━━━━━━━━━━
🎄 연말 파티는 홍대 파티룸 메리후드에서
📍 마포구 양화로18안길 40, 4층
👉 @mmeerryy_hood · 예약 문의는 DM

#크리스마스카운트다운 {tags} #연말 #크리스마스 #캐럴추천 #공감 #홍대파티룸 #파티룸 #연말파티 #메리후드"""


def build_caption(d):
    """캡션 = 본문 + 🎧 오늘의 BGM + 메리후드 마무리 블록 + 해시태그"""
    b = d["bgm"]
    bgm = f"🎧 오늘의 BGM · {b['title']} - {b['artist']}"
    return f"{d['caption']}\n\n{bgm}\n{CLOSING.format(tags=d.get('tags', ''))}"


start, end = sys.argv[1], sys.argv[2]
for f in sorted(Path("days").glob("*.json")):
    if not (start <= f.stem <= end):
        continue
    data = json.loads(f.read_text(encoding="utf-8"))
    out = Path("out") / f.stem
    paths, tag = render(data, out)
    (out / "caption.txt").write_text(build_caption(data), encoding="utf-8")
    ims = [Image.open(p) for p in paths]
    w, h = 540, 675
    sheet = Image.new("RGB", (w * 5 + 40, h), "white")
    for i, im in enumerate(ims):
        sheet.paste(im.resize((w, h)), (i * (w + 10), 0))
    sheet.save(out / "preview.png")
    print(f.stem, "tag", tag)
