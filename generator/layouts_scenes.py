"""2번 '공감 장면' 카드의 장면 템플릿: chat / calendar / list / photo / weather
각 함수는 패널 영역(대략 x 90~990, y 230~1030)에 들어갈 HTML을 돌려준다."""
import calendar as _cal
from render_cards import t, torn, d

# ───────── 단톡방 / 메신저 ─────────
CHAT_CSS = """
.chat{position:absolute;left:90px;top:225px;width:900px;background:#dfe7ee;color:var(--ink);border-radius:34px;
  padding:0 0 28px;transform:rotate(-1.5deg);box-shadow:0 14px 0 rgba(0,0,0,.28);overflow:hidden}
.chat .bar{background:#c9d4de;padding:20px 34px;font-size:36px;display:flex;justify-content:space-between}
.chat .bar small{font-size:30px;color:#5c6670}
.chat .list{padding:6px 34px 0}
.crow{display:flex;gap:16px;margin-top:14px;align-items:flex-start}
.crow.me{justify-content:flex-end;align-items:flex-end}
.ava{width:64px;height:64px;border-radius:22px;display:flex;align-items:center;justify-content:center;font-size:34px;flex:none}
.who{font-size:26px;color:#4a545c;margin:0 0 6px 4px}
.line{display:flex;align-items:flex-end;gap:10px}
.bub{background:#fff;padding:12px 24px;border-radius:8px 24px 24px 24px;font-size:35px;line-height:1.35;max-width:560px;word-break:keep-all}
.bub.mine{background:var(--yellow);border-radius:24px 8px 24px 24px}
.meta{font-size:24px;color:#6b747c;display:flex;flex-direction:column;align-items:flex-end;white-space:nowrap}
.unread{color:#e0a400;font-size:28px}
.cdiv{text-align:center;margin:22px 0 2px}
.cdiv span{background:rgba(0,0,0,.12);color:#3e474e;padding:8px 26px;border-radius:999px;font-size:28px}
.chat.work{background:#e9e6f2}.chat.work .bar{background:#d6d1e6}
"""
PALETTE = ["#ffc2dc", "#c6f36a", "#ffe9a0", "#b9e3ff", "#ffd1a8"]


def chat(s):
    rows, colors = [], {}
    for m in s["messages"]:
        if m.get("divider"):
            rows.append(f'<div class="cdiv"><span>{t(m["divider"])}</span></div>')
        elif m.get("me"):
            read = f'<span class="unread">{m["unread"]}</span>' if m.get("unread") else ""
            rows.append(f'<div class="crow me"><div class="meta">{read}<span>{t(m.get("time",""))}</span></div>'
                        f'<div class="bub mine">{t(m["text"])}</div></div>')
        else:
            col = colors.setdefault(m["who"], PALETTE[len(colors) % len(PALETTE)])
            rows.append(f'<div class="crow"><div class="ava" style="background:{col}">{t(m["who"][0])}</div>'
                        f'<div><div class="who">{t(m["who"])}</div><div class="line"><div class="bub">{t(m["text"])}</div>'
                        f'<div class="meta"><span>{t(m.get("time",""))}</span></div></div></div></div>')
    cls = "chat work" if s.get("style") == "work" else "chat"
    return (f'<style>{CHAT_CSS}</style><div class="{cls}"><div class="bar"><span>{t(s["room"])}</span><small>≡</small></div>'
            f'<div class="list">{"".join(rows)}</div></div>')


# ───────── 캘린더 ─────────
MONTHS = ["", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]


def calendar(s):
    y, m = s["year"], s["month"]
    weeks = _cal.Calendar(firstweekday=6).monthdayscalendar(y, m)
    circ, cross, fill = set(s.get("circle", [])), set(s.get("cross", [])), set(s.get("fill", []))
    labels = {int(k): v for k, v in s.get("labels", {}).items()}
    cells = ""
    for w in weeks:
        for i, day in enumerate(w):
            if not day:
                cells += '<div class="cc"></div>'; continue
            col = "#e0457b" if i == 0 else "#3b6fd6" if i == 6 else "var(--ink)"
            bg = "background:rgba(255,240,122,.9);" if day in fill else ""
            mark = d("heart", -6, -14, 92, "#e0457b", 0, 6) if day in circ else ""
            x = ('<svg class="doodle" viewBox="0 0 100 100" style="left:14px;top:4px;width:70px;height:70px" fill="none" '
                 'stroke="#8a948e" stroke-width="7" stroke-linecap="round" filter="url(#rough)"><path d="M15 15 L85 85 M85 15 L15 85"/></svg>'
                 if day in cross else "")
            lab = f'<div class="lab">{t(labels[day])}</div>' if day in labels else ""
            cells += f'<div class="cc" style="{bg}"><span style="color:{col}">{day}</span>{x}{mark}{lab}</div>'
    rows = len(weeks)
    ch = 520 // rows
    heads = "".join(f'<div style="color:{"#e0457b" if i==0 else "#3b6fd6" if i==6 else "#4a545c"}">{w}</div>' for i, w in enumerate("일월화수목금토"))
    return f"""<style>
      .cal{{position:absolute;left:90px;top:225px;width:900px;padding:34px 40px 26px;transform:rotate(-1.2deg);color:var(--ink)}}
      .cal .top{{display:flex;align-items:baseline;gap:22px;margin-bottom:14px}}
      .cal .mo{{font-family:var(--heavy);font-size:84px;line-height:1}}
      .cal .en{{font-family:var(--en);font-size:44px;color:#e0457b}}
      .cal .hd{{display:grid;grid-template-columns:repeat(7,1fr);font-size:30px;text-align:center;padding-bottom:10px;border-bottom:3px solid var(--ink)}}
      .cal .gr{{display:grid;grid-template-columns:repeat(7,1fr);grid-auto-rows:{ch}px}}
      .cc{{position:relative;border-bottom:2px solid rgba(20,32,26,.15);padding:10px 0 0 16px;font-size:36px}}
      .cc span{{position:relative;z-index:1}}
      .cc .lab{{position:absolute;left:4px;right:4px;bottom:8px;font-size:22px;line-height:1.1;text-align:center;
        background:var(--lime);border-radius:6px;padding:4px 2px;transform:rotate(-3deg);word-break:keep-all}}
    </style>
    <div class="cal paper" style="clip-path:{torn(61, 1.2)}">
      <div class="top"><div class="mo">{m}월</div><div class="en">{MONTHS[m]} {y}</div></div>
      <div class="hd">{heads}</div><div class="gr">{cells}</div>
    </div>"""


# ───────── 메모 / 검색 / 알람 / 장바구니 / 체크리스트 / 플레이리스트 / 투표 ─────────
THEMES = {
    "memo": dict(bg="#fff6b8", fg="var(--ink)", icon="📝", lined=True),
    "checklist": dict(bg="#fff6b8", fg="var(--ink)", icon="✅", lined=True),
    "search": dict(bg="#ffffff", fg="var(--ink)", icon="🔍", lined=False),
    "alarm": dict(bg="#1c2430", fg="#f3f5f7", icon="⏰", lined=False),
    "cart": dict(bg="#ffffff", fg="var(--ink)", icon="🛒", lined=False),
    "playlist": dict(bg="#1c2430", fg="#f3f5f7", icon="🎧", lined=False),
    "vote": dict(bg="#ffffff", fg="var(--ink)", icon="🗳️", lined=False),
}


def list_(s):
    st = s.get("style", "memo"); th = THEMES[st]
    items = ""
    for it in s["items"]:
        left = ""
        if st in ("checklist", "cart"):
            left = (f'<div class="bx">{"✔" if it.get("checked") else ""}</div>')
        elif st == "search":
            left = '<div class="ic">🔍</div>'
        elif st == "playlist":
            left = '<div class="ic">▶</div>'
        txt = t(it["text"])
        if it.get("strike"):
            txt = f'<s>{txt}</s>'
        right = ""
        if st == "alarm":
            on = not it.get("off")
            right = f'<div class="tg {"on" if on else ""}"><i></i></div>'
        elif it.get("right"):
            right = f'<div class="rt">{t(it["right"])}</div>'
        bar = ""
        if st == "vote":
            bar = f'<div class="vb"><i style="width:{it.get("bar",0)}%"></i></div>'
        dim = "opacity:.45;" if it.get("dim") else ""
        hl = "background:rgba(198,243,106,.55);border-radius:12px;" if it.get("highlight") else ""
        items += f'<div class="li" style="{dim}{hl}">{left}<div class="tx">{txt}{bar}</div>{right}</div>'
    query = f'<div class="q">🔍 {t(s["query"])}</div>' if s.get("query") else ""
    lines = ("background-image:repeating-linear-gradient(transparent 0 110px,rgba(20,32,26,.12) 110px 112px);" if th["lined"] else "")
    return f"""<style>
      .lst{{position:absolute;left:100px;top:235px;width:880px;padding:52px 56px 46px;transform:rotate(-1.2deg);
        background:{th['bg']};color:{th['fg']};border-radius:30px;box-shadow:0 14px 0 rgba(0,0,0,.28)}}
      .lst .hd{{display:flex;align-items:center;gap:18px;font-size:56px;margin-bottom:8px}}
      .lst .sub{{font-size:32px;opacity:.6;margin-bottom:22px}}
      .lst .q{{font-size:36px;padding:18px 28px;border-radius:999px;background:rgba(0,0,0,.07);margin-bottom:22px}}
      .lst .body{{{lines}}}
      .li{{display:flex;align-items:center;gap:22px;min-height:112px;padding:6px 14px;font-size:46px;line-height:1.3;word-break:keep-all}}
      .li .tx{{flex:1}} .li s{{text-decoration-thickness:4px;text-decoration-color:#e0457b}}
      .li .bx{{width:50px;height:50px;border:5px solid currentColor;border-radius:10px;display:flex;align-items:center;justify-content:center;
        font-size:34px;color:#e0457b;flex:none}}
      .li .ic{{font-size:32px;opacity:.7;flex:none}}
      .li .rt{{font-size:40px;opacity:.75;white-space:nowrap}}
      .tg{{width:96px;height:54px;border-radius:999px;background:#56606b;position:relative;flex:none}}
      .tg i{{position:absolute;left:6px;top:6px;width:42px;height:42px;border-radius:50%;background:#fff}}
      .tg.on{{background:#7bd88f}} .tg.on i{{left:48px}}
      .vb{{height:18px;border-radius:999px;background:rgba(0,0,0,.08);margin-top:10px}}
      .vb i{{display:block;height:100%;border-radius:999px;background:var(--pink)}}
    </style>
    <div class="lst"><div class="hd">{th['icon']} {t(s['title'])}</div>
      {f'<div class="sub">{t(s["sub"])}</div>' if s.get('sub') else ''}{query}<div class="body">{items}</div></div>"""


# ───────── 사진 (폴라로이드 / 사진첩 그리드) ─────────
def photo(s):
    if s.get("style") == "album":
        tiles = ""
        for p in s["photos"]:
            ring = "outline:8px solid var(--pink);outline-offset:-8px;" if p.get("highlight") else ""
            tiles += (f'<div style="background:{p.get("bg","#cfe3d6")};{ring}display:flex;align-items:center;justify-content:center;'
                      f'font-size:96px;position:relative">{p["emoji"]}'
                      + (f'<div style="position:absolute;bottom:10px;left:0;right:0;text-align:center;font-size:26px;color:var(--ink)">{t(p["caption"])}</div>' if p.get("caption") else "")
                      + '</div>')
        return f"""<div class="abs" style="left:110px;top:240px;width:860px;padding:30px;background:#fff;border-radius:30px;
          transform:rotate(-1.2deg);box-shadow:0 14px 0 rgba(0,0,0,.28);color:var(--ink)">
          <div style="font-size:40px;margin:0 0 20px 6px">🖼 {t(s.get('title','사진첩'))}</div>
          <div style="display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:205px;gap:10px">{tiles}</div></div>"""
    n = len(s["photos"])
    pos = {1: [(250, 250, -3)], 2: [(110, 270, -6), (520, 330, 5)], 3: [(80, 250, -7), (560, 230, 6), (330, 560, -2)]}[n]
    w = 520 if n == 1 else 440 if n == 2 else 400
    out = ""
    for (x, y, r), p in zip(pos, s["photos"]):
        out += (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;padding:24px 24px 0;background:#fbfaf6;'
                f'transform:rotate({r}deg);box-shadow:0 14px 0 rgba(0,0,0,.3);color:var(--ink)">'
                f'<div style="height:{w-48}px;background:{p.get("bg","#cfe3d6")};display:flex;align-items:center;justify-content:center;'
                f'font-size:{int(w*.36)}px">{p["emoji"]}</div>'
                f'<div style="font-family:var(--pen);font-size:46px;text-align:center;padding:16px 0 20px;line-height:1.05">{t(p.get("caption",""))}</div></div>'
                f'<div class="abs" style="left:{x + w//2 - 70}px;top:{y-22}px;width:140px;height:44px;background:rgba(198,243,106,.85);'
                f'transform:rotate({r+4}deg)"></div>')
    return out


# ───────── 날씨 ─────────
def weather(s):
    hourly = "".join(f'<div style="text-align:center"><div style="font-size:28px;opacity:.75">{t(h[0])}</div>'
                     f'<div style="font-size:64px;margin:14px 0">{h[2]}</div><div style="font-size:40px">{t(h[1])}</div></div>'
                     for h in s["hourly"])
    return f"""<div class="abs" style="left:100px;top:232px;width:880px;padding:42px 56px;border-radius:40px;
      background:linear-gradient(160deg,#5aa2e8,#2f6fc0);color:#fff;transform:rotate(-1.2deg);box-shadow:0 14px 0 rgba(0,0,0,.28)">
      <div style="font-size:40px">📍 {t(s['place'])}</div>
      <div style="display:flex;align-items:center;gap:30px;margin-top:10px">
        <div style="font-family:var(--heavy);font-size:200px;line-height:1">{t(s['now'])}</div>
        <div style="font-size:150px">{s['icon']}</div></div>
      <div style="font-size:40px;margin-top:6px">{t(s['desc'])} · 최고 {t(s['hi'])} / 최저 {t(s['lo'])}</div>
      <div style="display:grid;grid-template-columns:repeat({len(s['hourly'])},1fr);margin-top:34px;padding-top:28px;
        border-top:2px solid rgba(255,255,255,.35)">{hourly}</div>
      {f'<div style="margin-top:30px;padding:22px 30px;border-radius:20px;background:rgba(255,255,255,.18);font-size:38px;word-break:keep-all">⚠️ {t(s["alert"])}</div>' if s.get('alert') else ''}
    </div>"""


SCENES = {"chat": chat, "calendar": calendar, "list": list_, "photo": photo, "weather": weather}


def render_scene(s):
    return SCENES[s["type"]](s)
