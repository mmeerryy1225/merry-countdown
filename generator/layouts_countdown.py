"""D-day 카운트다운 카드 레이아웃: 표지 → 공감(단톡방) → 오늘의 BGM → 오늘의 미션 → 메리후드"""
from render_cards import t, torn, d, wave, tree, snowman, tape, foot, PATHS

PATHS.update({
    "arrow_down": '<path d="M50 6 C46 30 54 52 50 84 M30 66 L50 88 L70 64"/>',
    "arrow_curve": '<path d="M10 20 C40 10 70 30 78 70 M60 58 L80 74 L90 52"/>',
    "check": '<path d="M18 52 L42 76 L86 22"/>',
    "box": '<rect x="10" y="10" width="80" height="80" rx="10"/>',
    "disc": '<circle cx="50" cy="50" r="40"/><circle cx="50" cy="50" r="10"/><path d="M50 22 A28 28 0 0 1 78 50"/>',
})


def cover(c):
    return f"""
    {tape("CHRISTMAS COUNTDOWN", "lime", 90, 100, -3, seed=11)}
    <div class="abs en-note" style="left:860px;top:180px;transform:rotate(8deg);font-size:46px">Ho Ho<br>Ho! ♪</div>
    {tape(f"{c['date']} ({c['weekday']})", "yellow", 110, 215, 2, seed=12)}
    <div class="abs" style="left:96px;top:300px;font-family:var(--heavy);font-size:250px;line-height:1;letter-spacing:-.01em">D-{c['dday']}</div>
    {wave(110, 570, 560, h=36, w=10)}
    {d("crown", 690, 300, 110, "var(--gold)", 14, 6)}
    {d("spark_r", 730, 430, 80, "var(--chalk)", 0, 6)}
    <div class="abs paper" style="left:80px;top:660px;width:920px;padding:64px 64px 70px;transform:rotate(-1.5deg);clip-path:{torn(13)}">
      <div style="font-size:62px;line-height:1.45;word-break:keep-all">{t(c['cover'])}</div>
    </div>
    <div class="abs note" style="right:110px;top:1085px;transform:rotate(-6deg);font-size:58px">{t(c['cover_note'])}</div>
    {d("heart", 70, 600, 64, "var(--pink)", -12)}
    {d("star", 60, 1090, 64, "var(--gold)", -8)}
    {foot(0)}"""


def chat(c):
    """2번 공감 장면 카드 — 장면 종류(chat/calendar/list/photo/weather)에 따라 템플릿 선택"""
    from layouts_scenes import render_scene
    sc = c.get("scene") or {"type": "chat", **c["chat"]}
    title = c.get("scene_title", "이거 우리 단톡방?")
    note = c.get("scene_note") or c.get("chat_note", "")
    return f"""
    {tape(c.get("scene_tag", "REAL TALK"), "pink", 90, 100, -3, seed=21)}
    <div class="abs h1" style="left:420px;top:100px;font-size:62px;width:600px;white-space:nowrap">{t(title)}</div>
    {render_scene(sc)}
    <div class="abs note" style="left:110px;top:1065px;transform:rotate(-4deg);font-size:56px;text-align:left">{t(note)}</div>
    {d("arrow_curve", 520, 1030, 130, "var(--lime)", -95, 7)}
    {d("heart", 950, 190, 64, "var(--pink)", 14)}
    {d("star", 960, 1070, 56, "var(--gold)", -10)}
    {foot(1)}"""


def bgm(c):
    b = c["bgm"]
    return f"""
    {tape("TODAY'S BGM", "yellow", 90, 100, -3, seed=31)}
    {d("note", 400, 80, 80, "var(--chalk)", -10, 6)}
    <div class="abs h1" style="left:96px;top:240px;font-size:70px">오늘 같은 날엔 이 노래</div>
    {wave(100, 340, 600)}
    <div class="abs paper" style="left:90px;top:440px;width:900px;padding:60px 64px;transform:rotate(1.2deg);clip-path:{torn(32)};
      display:flex;gap:46px;align-items:center">
      <svg viewBox="0 0 100 100" style="width:210px;height:210px;flex:none">
        <circle cx="50" cy="50" r="48" fill="#14201a"/><circle cx="50" cy="50" r="38" fill="none" stroke="#2c3a33" stroke-width="2"/>
        <circle cx="50" cy="50" r="28" fill="none" stroke="#2c3a33" stroke-width="2"/>
        <circle cx="50" cy="50" r="17" fill="#ff8cc6"/><circle cx="50" cy="50" r="4" fill="#f1eee6"/></svg>
      <div>
        <div style="font-family:var(--heavy);font-size:70px;line-height:1.15;word-break:keep-all">{t(b['title'])}</div>
        <div style="margin-top:18px;font-size:38px;color:#4a545c">{t(b['artist'])} · {t(str(b['year']))}</div>
      </div>
    </div>
    {tape("선곡 이유", "lime", 100, 860, -2, ko=True, seed=33, size=38)}
    <div class="abs" style="left:100px;top:960px;width:880px;font-size:54px;line-height:1.55;word-break:keep-all">{t(b['reason'])}</div>
    {d("spark_l", 20, 520, 70, "var(--gold)", 0, 6)}
    {d("heart", 940, 860, 64, "var(--pink)", 12)}
    {d("star", 60, 1120, 60, "var(--lime)", -8)}
    {foot(2)}"""


def mission(c):
    m = c["mission"]
    items = "".join(
        f'<div style="display:flex;gap:26px;align-items:center;margin-bottom:34px">'
        f'<div style="position:relative;width:76px;height:76px;flex:none">'
        f'{d("box", 0, 0, 76, "var(--ink)", 0, 8)}{d("check", 6, -14, 84, "#e0457b", 0, 11) if i == 0 else ""}</div>'
        f'<div style="font-size:52px;line-height:1.35;word-break:keep-all">{t(s)}</div></div>'
        for i, s in enumerate(m["todo"]))
    return f"""
    {tape("TODAY'S MISSION", "lime", 90, 100, -3, seed=41)}
    {d("crown", 470, 70, 80, "var(--gold)", 12, 6)}
    <div class="abs h1" style="left:96px;top:240px;font-size:76px">오늘 이것만 하자</div>
    {wave(100, 345, 540)}
    <div class="abs paper" style="left:80px;top:450px;width:920px;padding:70px 64px 40px;transform:rotate(-1deg);clip-path:{torn(42)};
      background:var(--yellow)">{items}</div>
    <div class="abs" style="left:96px;top:870px;width:880px;font-size:60px;line-height:1.45;word-break:keep-all">{t(m['cta'])}</div>
    {d("arrow_down", 460, 1040, 120, "var(--pink)", 0, 8)}
    {d("arrow_down", 320, 1060, 84, "var(--lime)", -14, 7)}
    {d("arrow_down", 620, 1060, 84, "var(--gold)", 14, 7)}
    {d("heart", 940, 260, 64, "var(--pink)", 12)}
    {d("star", 940, 980, 60, "var(--gold)", 8)}
    {foot(3)}"""


def merryhood(c):
    return f"""
    {tape(f"D-{c['dday']} × MERRYHOOD", "lime", 90, 100, -3, seed=51, size=44)}
    {d("crown", 40, 40, 70, "var(--lime)", -14, 6)}
    <div class="abs en-note" style="left:850px;top:150px;transform:rotate(10deg);font-size:46px">Let's<br>party! ♪</div>
    <div class="abs" style="left:96px;top:250px;width:900px;font-size:74px;line-height:1.35;word-break:keep-all">{t(c['merryhood_line'])}</div>
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


def build(c):
    return [cover(c), chat(c), bgm(c), mission(c), merryhood(c)]  # 메리후드는 항상 마지막
