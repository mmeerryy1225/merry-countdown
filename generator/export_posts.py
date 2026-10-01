"""out/날짜/ 렌더 결과 → 저장소 posts/날짜/ (업로드용 jpg + caption + meta)
사용: python export_posts.py 2026-10-09 2026-10-15
"""
import sys, json
from pathlib import Path
from PIL import Image

start, end = sys.argv[1], sys.argv[2]
dest_root = Path(__file__).resolve().parent.parent / "posts"
for src in sorted(Path("out").glob("20*")):
    if not (start <= src.name <= end):
        continue
    dst = dest_root / src.name
    dst.mkdir(parents=True, exist_ok=True)
    for p in sorted(src.glob("0[1-9].png")):
        Image.open(p).convert("RGB").save(dst / f"{p.stem}.jpg", quality=92, subsampling=0)
    (dst / "caption.txt").write_text((src / "caption.txt").read_text(encoding="utf-8"), encoding="utf-8")
    (dst / "meta.json").write_text(json.dumps({"tag_username": "mmeerryy_hood", "tag_x": 0.364, "tag_y": 0.864}), encoding="utf-8")
    print("exported", src.name)
