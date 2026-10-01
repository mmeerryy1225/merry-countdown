"""캐럴 카드뉴스 한 세트 렌더링 — 칠판 + 형광 테이프 + 손글씨 낙서 스타일.
표지 → 소개 → 이야기 → 추천 → 메리후드(항상 마지막)
사용: python render_cards.py sample.json out_dir/
"""
import sys, json, html, random
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
TPL = ROOT / "templates"
TOTAL = 5

# ───────────────────────── 유틸 ─────────────────────────
def t(s: str) -> str:
    """이스케이프 후 <em>, <br>만 허용."""
    s = html.escape(str(s))
    for tag in ("em", "/em", "br"):
        s = s.replace(f"&lt;{tag}&gt;", f"<{tag}>")
    return s


def torn(seed: int, amp: float = 2.2, n: int = 22) -> str:
    """찢어진 가장자리 clip-path (seed 고정 → 매번 같은 모양)."""
    r = random.Random(seed)
    j = lambda: r.uniform(0, amp)
    pts = [(i * 100 / n, j()) for i in range(n + 1)]
    pts += [(100 - j() * .4, i * 100 / 8) for i in range(1, 8)]
    pts += [(100 - i * 100 / n, 100 - j()) for i in range(n + 1)]
    pts += [(j() * .4, 100 - i * 100 / 8) for i in range(1, 8)]
    return "polygon(" + ",".join(f"{x:.2f}% {y:.2f}%" for x, y in pts) + ")"


# ───────────────────────── 낙서 SVG ─────────────────────────
ROUGH = ('<svg width="0" height="0" style="position:absolute"><filter id="rough">'
         '<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="4"/>'
         '<feDisplacementMap in="SourceGraphic" scale="4"/></filter></svg>')

PATHS = {
    "heart": '<path d="M50 86 C22 64 6 44 20 24 C32 9 47 16 50 32 C53 16 68 9 80 24 C94 44 78 64 50 86Z"/>',
    "star": '<path d="M50 6 L61 37 L94 38 L68 58 L78 90 L50 71 L22 90 L32 58 L6 38 L39 37Z"/>',
    "crown": '<path d="M12 78 L18 30 L37 54 L50 18 L63 54 L82 30 L88 78Z"/>',
    "spark_l": '<path d="M8 50 L40 50 M14 22 L42 40 M14 78 L42 60"/>',
    "spark_r": '<path d="M92 50 L60 50 M86 22 L58 40 M86 78 L58 60"/>',
    "zigzag": '<path d="M4 60 L18 40 L32 60 L46 40 L60 60 L74 40 L88 60 L96 48"/>',
    "smile": '<circle cx="50" cy="50" r="40"/><path d="M36 40 L36 46 M64 40 L64 46 M32 60 Q50 78 68 60"/>',
    "note": '<path d="M38 78 L38 18 L80 8 L80 66"/><ellipse cx="28" cy="78" rx="12" ry="9"/><ellipse cx="70" cy="68" rx="12" ry="9"/>',
    "loop": '<path d="M6 60 C20 20 40 20 34 50 C28 80 54 80 62 46 C68 22 84 24 94 40"/>',
}


def d(name, x, y, size, color, rot=0, w=7):
    return (f'<svg class="doodle" viewBox="0 0 100 100" style="left:{x}px;top:{y}px;width:{size}px;'
            f'height:{size}px;transform:rotate({rot}deg)" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round" filter="url(#rough)">{PATHS[name]}</svg>')


def wave(x, y, width, color="var(--lime)", h=34, w=9):
    segs = max(4, width // 60)
    step = 200 / segs
    p = "M4 20 " + " ".join(f"Q{step*i + step/2:.1f} {6 if i % 2 == 0 else 34} {step*(i+1):.1f} 20" for i in range(segs))
    return (f'<svg class="doodle" viewBox="0 0 204 40" preserveAspectRatio="none" style="left:{x}px;top:{y}px;'
            f'width:{width}px;height:{h}px" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round" filter="url(#rough)" vector-effect="non-scaling-stroke"><path d="{p}"/></svg>')


TREE = ('<svg class="doodle" viewBox="0 0 100 120" style="left:{x}px;top:{y}px;width:{s}px;height:{h}px;transform:rotate({r}deg)">'
        '<path d="M50 4 L54 14 L64 14 L56 20 L59 30 L50 24 L41 30 L44 20 L36 14 L46 14Z" fill="#ffd83d"/>'
        '<path d="M50 26 L80 62 L64 62 L88 96 L12 96 L36 62 L20 62Z" fill="#2fa65a" stroke="#14201a" stroke-width="4" stroke-linejoin="round"/>'
        '<rect x="43" y="96" width="14" height="16" fill="#8a5a33" stroke="#14201a" stroke-width="4"/>'
        '<circle cx="44" cy="54" r="5" fill="#ff5d73"/><circle cx="60" cy="76" r="5" fill="#ffd83d"/>'
        '<circle cx="34" cy="84" r="5" fill="#5ec8ff"/><circle cx="70" cy="88" r="5" fill="#ff5d73"/></svg>')


def tree(x, y, s, r=0):
    return TREE.format(x=x, y=y, s=s, h=int(s * 1.2), r=r)


SNOWMAN = ('<svg class="doodle" viewBox="0 0 160 170" style="left:{x}px;top:{y}px;width:{s}px;height:{h}px">'
           '<g stroke="#14201a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round">'
           '<circle cx="80" cy="122" r="44" fill="#fbfaf6"/><circle cx="80" cy="64" r="34" fill="#fbfaf6"/>'
           '<path d="M44 46 Q80 -6 116 46Z" fill="#e8394a"/><path d="M40 48 Q80 34 120 48 L118 58 Q80 46 42 58Z" fill="#fbfaf6"/>'
           '<circle cx="80" cy="12" r="10" fill="#fbfaf6"/>'
           '<path d="M50 92 Q80 104 110 92 L112 102 Q80 114 48 102Z" fill="#c6f36a"/>'
           '<path d="M98 98 L104 126 L92 126 Z" fill="#c6f36a"/></g>'
           '<circle cx="68" cy="66" r="4" fill="#14201a"/><circle cx="92" cy="66" r="4" fill="#14201a"/>'
           '<path d="M80 72 L98 78 L80 80Z" fill="#ff8a3d"/>'
           '<ellipse cx="62" cy="80" rx="6" ry="4" fill="#ff8cc6" opacity=".7"/><ellipse cx="98" cy="80" rx="6" ry="4" fill="#ff8cc6" opacity=".7"/>'
           '<circle cx="80" cy="120" r="4" fill="#14201a"/><circle cx="80" cy="140" r="4" fill="#14201a"/></svg>')


def snowman(x, y, s):
    return SNOWMAN.format(x=x, y=y, s=s, h=int(s * 170 / 160))


# 모든 카드 공통 장식: 오른쪽 위 찢어진 종이+트리, 왼쪽 아래 체크 마스킹테이프
def common_decor():
    return (f'<div class="abs paper" style="right:-30px;top:-30px;width:200px;height:200px;transform:rotate(14deg);'
            f'clip-path:{torn(91, 5)};background:#e9e6dd"></div>' + tree(958, 6, 100, 8) +
            f'<div class="abs" style="left:-40px;bottom:-55px;width:230px;height:120px;transform:rotate(-12deg);'
            f'clip-path:{torn(92, 6)};opacity:.85;background:'
            f'repeating-linear-gradient(0deg,rgba(255,255,255,.18) 0 8px,transparent 8px 24px),'
            f'repeating-linear-gradient(90deg,rgba(255,255,255,.18) 0 8px,transparent 8px 24px),#3d7a55"></div>')


def foot(idx):
    stars = " ".join("★" if i == idx else "☆" for i in range(TOTAL))
    return f'<div class="foot"><span class="me">@m.eeeeeeeerry</span><span class="pg">{stars}</span></div>'


def tape(text, color, x, y, rot, ko=False, seed=1, size=None):
    fs = f"font-size:{size}px;" if size else ""
    return (f'<div class="abs tape {color}{" ko" if ko else ""}" style="left:{x}px;top:{y}px;{fs}'
            f'transform:rotate({rot}deg);clip-path:{torn(seed, 6, 14)}">{t(text)}</div>')


# ───────────────────────── 카드별 레이아웃 ─────────────────────────
def cover(d_):
    return f"""
    {tape("TODAY'S CAROL ♪", "lime", 90, 110, -3, seed=11)}
    <div class="abs en-note" style="left:800px;top:190px;transform:rotate(8deg)">Let's<br>sing!</div>
    {d("spark_r", 720, 190, 70, "var(--chalk)", 0, 6)}
    {tape(f"DAY {d_['day']:02d} · {d_['date']}", "yellow", 120, 300, 2, seed=12)}
    <div class="abs paper" style="left:80px;top:440px;width:920px;padding:70px 70px 80px;transform:rotate(-1.5deg);clip-path:{torn(13)}">
      <div style="font-family:var(--heavy);font-size:132px;line-height:1.12;word-break:keep-all">{t(d_['title'])}</div>
    </div>
    {d("crown", 860, 400, 100, "var(--chalk)", 12, 6)}
    {wave(140, 790, 560)}
    {tape(f"{d_['artist']} · {d_['year']}", "pink", 110, 860, -1, ko=True, seed=14, size=32)}
    <div class="abs" style="left:100px;top:990px;width:860px;font-size:52px;line-height:1.55;word-break:keep-all">{t(d_['hook'])}</div>
    {d("heart", 70, 280, 64, "var(--pink)", -12)}
    {d("star", 930, 980, 70, "var(--gold)", 10)}
    {d("star", 40, 760, 54, "var(--lime)", -8)}
    {foot(0)}"""


def text_card(label, heading, paras, side_note, idx, seed):
    body = "".join(f"<p>{t(p)}</p>" for p in paras)
    return f"""
    {tape(label, "lime", 90, 110, -3, seed=seed)}
    {d("spark_r", 330, 92, 70, "var(--gold)", 0, 6)}
    <div class="abs h1" style="left:96px;top:250px;width:880px">{t(heading)}</div>
    {wave(100, 370, 520)}
    <div class="abs body" style="left:100px;top:470px;width:860px">{body}</div>
    <div class="abs note" style="right:100px;bottom:250px;transform:rotate(-6deg);font-size:52px">{t(side_note)}</div>
    {d("loop", 380, 1050, 120, "var(--lime)", -10, 6)}
    {d("heart", 920, 300, 70, "var(--pink)", 14)}
    {d("star", 60, 1040, 60, "var(--gold)", -10)}
    {d("note", 560, 1060, 66, "var(--chalk)", -8, 6)}
    {foot(idx)}"""


def mood(d_):
    colors = ["lime", "pink", "yellow", "lime", "pink"]
    rots = [-3, 2, -1.5, 3, -2]
    chips = "".join(
        f'<div class="tape ko {colors[i % 5]}" style="font-size:42px;margin:0 22px 26px 0;'
        f'transform:rotate({rots[i % 5]}deg);clip-path:{torn(40 + i, 6, 14)}">{t(c)}</div>'
        for i, c in enumerate(d_["moods"]))
    return f"""
    {tape("LISTEN WHEN", "pink", 90, 110, -3, seed=31)}
    <div class="abs h1" style="left:96px;top:250px;width:880px">이런 날 들어보세요</div>
    {wave(100, 370, 600)}
    <div class="abs" style="left:96px;top:480px;width:900px;display:flex;flex-wrap:wrap">{chips}</div>
    <div class="abs paper" style="left:90px;top:830px;width:900px;padding:50px 60px;background:var(--yellow);
      transform:rotate(-1deg);clip-path:{torn(33)};font-size:42px;line-height:1.6;word-break:keep-all">
      🎧 <b style="font-weight:400;background:linear-gradient(transparent 60%,var(--pink) 60%)">듣는 법</b><br>{t(d_['listen'])}
    </div>
    {d("spark_l", 30, 830, 60, "var(--gold)", 0, 6)}
    {d("heart", 930, 260, 70, "var(--pink)", 12)}
    {d("star", 900, 720, 64, "var(--lime)", -8)}
    {foot(3)}"""


def merryhood(d_):
    return f"""
    {tape("TODAY'S CAROL × MERRYHOOD", "lime", 90, 100, -3, seed=51, size=42)}
    {d("crown", 40, 40, 70, "var(--lime)", -14, 6)}
    <div class="abs en-note" style="left:860px;top:150px;transform:rotate(10deg);font-size:46px">Let's<br>sing! ♪</div>
    <div class="abs" style="left:96px;top:250px;width:900px;font-size:74px;line-height:1.35;word-break:keep-all">{t(d_['merryhood_line'])}</div>
    {wave(100, 455, 640)}
    {d("heart", 30, 250, 66, "var(--pink)", -10)}
    {d("star", 40, 400, 64, "var(--lime)", 0)}

    <div class="abs paper" style="left:70px;top:540px;width:720px;height:250px;transform:rotate(-2deg);clip-path:{torn(52, 4)};
      display:flex;align-items:center;justify-content:center">
      <div style="font-family:var(--heavy);font-size:172px;letter-spacing:.02em;line-height:1">메리후드</div>
    </div>
    {d("spark_l", 20, 610, 80, "var(--chalk)", 0, 7)}
    {d("spark_r", 760, 610, 80, "var(--chalk)", 0, 7)}
    {d("crown", 640, 520, 80, "var(--ink)", 10, 6)}
    {wave(150, 735, 470, h=30, w=8)}
    <div class="abs en-note" style="left:830px;top:520px;transform:rotate(-8deg);color:var(--lime);font-size:58px">Merry<br>Hood</div>
    {d("smile", 960, 590, 70, "var(--lime)", 0, 6)}
    {d("star", 940, 700, 56, "var(--gold)", 12)}

    {tape("홍대 프라이빗 파티룸 · 연말 파티 & 모임 대관", "pink", 110, 815, -2, ko=True, seed=53, size=36)}
    <div class="abs" style="left:110px;top:930px;font-size:46px;line-height:1.7">
      📍 서울 마포구 양화로18안길 40, 4층<br>🎄 크리스마스 · 송년회 · 생일파티
    </div>
    {wave(330, 1060, 330)}
    <div class="abs note" style="left:850px;top:910px;transform:rotate(-8deg);font-size:44px">좋은사람들과<br>더 특별한<br>시간 ♡</div>
    {d("heart", 960, 800, 60, "var(--pink)", 14)}

    <div class="abs paper" style="left:70px;top:1100px;width:880px;height:130px;background:var(--yellow);transform:rotate(-1deg);
      clip-path:{torn(54, 6)};display:flex;align-items:center;gap:22px;padding:0 44px">
      <div style="width:70px;height:70px;border-radius:20px;border:6px solid #e0457b;display:flex;align-items:center;justify-content:center;
        font-family:var(--en);font-size:48px;color:#e0457b;line-height:1">@</div>
      <div id="handle" style="font-family:var(--en);font-size:58px;line-height:1;white-space:nowrap;border-bottom:6px solid #e0457b;padding-bottom:4px">mmeerryy_hood</div>
      <div style="margin-left:auto;font-size:34px;white-space:nowrap">예약 문의는 <span style="border:4px solid #e0457b;border-radius:50%;padding:2px 12px;font-family:var(--en)">DM</span> ✉️</div>
    </div>
    {snowman(890, 1150, 165)}
    {d("star", 120, 1250, 56, "var(--gold)", -6)}
    {d("heart", 760, 1260, 56, "var(--pink)", 10)}"""


def build(d_):
    return [
        cover(d_),
        text_card("ABOUT", "이런 곡이에요", d_["about"], "알고 들으면<br>더 좋아요 ♡", 1, 21),
        text_card("STORY", "곡에 얽힌 이야기", d_["story"], "TMI<br>주의! ☺", 2, 22),
        mood(d_),
        merryhood(d_),  # 항상 마지막
    ]


def page(content):
    return (f'<!doctype html><html lang="ko"><head><meta charset="utf-8">'
            f'<link rel="stylesheet" href="style.css"></head><body>{ROUGH}{common_decor()}{content}</body></html>')


def render(d_, out_dir):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    tmp = TPL / "_render.html"
    paths, tag_pos = [], None
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        from layouts_countdown import build as build_countdown
        for i, content in enumerate(build_countdown(d_), 1):
            tmp.write_text(page(content), encoding="utf-8")
            pg.goto(tmp.resolve().as_uri())
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(300)
            path = out / f"{i:02d}.png"
            pg.screenshot(path=str(path))
            paths.append(path)
            h = pg.query_selector("#handle")
            if h:  # 마지막 카드: 인스타 사진 태그 좌표(0~1) 계산
                bb = h.bounding_box()
                tag_pos = (round((bb["x"] + bb["width"] / 2) / 1080, 3), round((bb["y"] + bb["height"] / 2) / 1350, 3))
        b.close()
    tmp.unlink(missing_ok=True)
    return paths, tag_pos


if __name__ == "__main__":
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    paths, tag = render(data, sys.argv[2] if len(sys.argv) > 2 else "out")
    for p in paths:
        print("saved:", p)
    print("merryhood tag position (x, y):", tag)
