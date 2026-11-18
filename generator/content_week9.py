"""9주차(D-28~D-22) 하루치 데이터 → days/YYYY-MM-DD.json"""
import json
from pathlib import Path

W = [
 dict(date_iso="2026-11-27", dday=28, date="11.27", weekday="금",
  cover="블랙프라이데이.<br>선물 사려다 결국<br><em>내 것만</em> 샀다.", cover_note="선물은… 다음 세일에 🙈",
  scene_title="선물은 어디에", scene_note="선물 하나는<br>꼭 결제하기로 ✍️",
  scene={"type": "list", "style": "cart", "title": "장바구니 (5)", "items": [
      {"text": "내 겨울 코트 🧥", "right": "결제 완료", "checked": True},
      {"text": "내 털 부츠 👢", "right": "결제 완료", "checked": True},
      {"text": "내 니트 목도리 🧣", "right": "결제 완료", "checked": True},
      {"text": "내 핸드크림 세트", "right": "결제 완료", "checked": True},
      {"text": "엄마 선물 🎁", "right": "아직 담기만…", "highlight": True}]},
  bgm={"title": "8 Days of Christmas", "artist": "Destiny's Child", "year": 2001,
       "reason": "선물 받는 상상은 신나는데,<br><em>주는 쪽</em>도 해 봐야지."},
  mission={"todo": ["장바구니 속 선물 하나는 꼭 결제하기", "받을 사람 이름 옆에 적어 두기"], "cta": "블프에 자기 것만 산 친구,<br><em>자수하세요</em> 👇"},
  merryhood_line="산 선물은 아껴 뒀다가<br><em>연말 파티</em>에서 짠 🎁",
  caption="D-28 · 블랙프라이데이, 결국 내 것만 🛍\n선물 사려고 들어갔다가 내 장바구니만 꽉 찼다면… 오늘 선물 하나는 꼭 결제해요.\n같이 자수할 친구 태그 👇", tags="#D28 #블랙프라이데이"),

 dict(date_iso="2026-11-28", dday=27, date="11.28", weekday="토",
  cover="<em>첫눈 예보</em>에<br>단톡방이 난리 났다.", cover_note="진짜 오는 거지? ❄️",
  scene_title="첫눈 대기 중", scene_note="첫눈 오면 바로<br>사진 보내기 약속 ✍️",
  scene={"type": "chat", "room": "눈 오면 만나 (4)", "messages": [
      {"divider": "11월 28일 토요일"},
      {"who": "하은", "text": "오늘 밤 첫눈 온대!!!", "time": "오후 4:10"},
      {"who": "준서", "text": "헐 진짜? 창문 열어 놓음", "time": "오후 4:12"},
      {"who": "하은", "text": "첫눈 오면 바로 사진 보내기 ❄️", "time": "오후 4:13"},
      {"me": True, "text": "콜!! 먼저 보내는 사람이 승", "time": "오후 4:15", "unread": 3}]},
  bgm={"title": "첫 눈", "artist": "EXO", "year": 2013,
       "reason": "창밖만 보게 되는 날,<br><em>첫눈 기다리는</em> 설렘."},
  mission={"todo": ["첫눈 오면 바로 사진 보내기 약속", "첫눈 오는 날 만날 사람 정하기"], "cta": "첫눈 사진 보내 줄 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="첫눈 오는 밤엔<br>따뜻한 <em>실내 파티</em>로 ☃️",
  caption="D-27 · 첫눈 예보에 단톡방 난리 ❄️\n첫눈 오면 제일 먼저 사진 보내는 사람이 승! 다들 창문 보고 있죠?\n첫눈 사진 보내 줄 친구 태그 👇", tags="#D27 #첫눈"),

 dict(date_iso="2026-11-29", dday=26, date="11.29", weekday="일",
  cover="11월 마지막 주말.<br><em>트리를 꺼낼까</em><br>말까.", cover_note="박스 앞에서 고민 30분 🎄",
  scene_title="꺼낼까 말까", scene_note="결국 오늘<br>꺼내기로 했다 ✍️",
  scene={"type": "photo", "photos": [
      {"emoji": "📦", "bg": "#ffd6e5", "caption": "베란다 속 트리 박스"},
      {"emoji": "🎄", "bg": "#d6f5b0", "caption": "꺼내면 이렇게 될 예정"}]},
  bgm={"title": "Deck the Halls", "artist": "웨일스 전통 캐럴", "year": "",
       "reason": "'집을 꾸미자'는 노래,<br>오늘이 바로 <em>그날.</em>"},
  mission={"todo": ["오늘 트리 박스 꺼내기", "전구 불 들어오는지 미리 확인하기"], "cta": "아직 트리 안 꺼낸 친구,<br><em>여기 태그로 재촉</em> 👇"},
  merryhood_line="트리 꾸미는 재미는<br><em>다 같이</em> 모여서 두 배 🎄",
  caption="D-26 · 트리, 꺼낼까 말까 🎄\n11월 마지막 주말, 박스 앞에서 고민 중이라면 오늘 꺼내는 걸로!\n아직 트리 안 꺼낸 친구 태그 👇", tags="#D26 #트리"),

 dict(date_iso="2026-11-30", dday=25, date="11.30", weekday="월",
  cover="내일부터 <em>12월.</em><br>올해가 진짜<br>끝나 간다.", cover_note="11월 어디 갔어 😶",
  scene_title="11월 끝", scene_note="고마웠던 사람<br>한 명 떠올리기 ✍️",
  scene={"type": "calendar", "year": 2026, "month": 11, "circle": [30],
         "cross": list(range(1, 30)), "fill": [],
         "labels": {"30": "마지막 날"}},
  bgm={"title": "12월의 기적", "artist": "EXO", "year": 2013,
       "reason": "남은 한 달에도<br><em>작은 기적</em> 하나쯤은."},
  mission={"todo": ["11월에 고마웠던 사람 한 명한테 연락하기", "12월에 꼭 할 일 하나 정하기"], "cta": "11월에 고마웠던 친구,<br><em>여기 태그해서 인사</em> 👇"},
  merryhood_line="고마운 사람들이랑<br><em>12월 파티</em> 어때요? 🎉",
  caption="D-25 · 내일부터 12월 🗓\n올해가 진짜 끝나 가요. 11월에 고마웠던 사람한테 오늘 한마디 보내 봐요.\n고마웠던 친구 태그 👇", tags="#D25 #11월마지막날"),

 dict(date_iso="2026-12-01", dday=24, date="12.01", weekday="화",
  cover="<em>12월 1일.</em> 진짜 시작이다.<br>어드벤트 캘린더<br>첫 칸 오픈!", cover_note="오늘부터 하루 한 칸 🎁",
  scene_title="첫 칸 오픈", scene_note="하루에 위시<br>하나씩 적기 ✍️",
  scene={"type": "calendar", "year": 2026, "month": 12, "circle": [25], "cross": [], "fill": [1],
         "labels": {"1": "첫 칸🎁", "25": "크리스마스🎄"}},
  bgm={"title": "미리 메리 크리스마스", "artist": "아이유", "year": 2011,
       "reason": "12월 첫날엔<br><em>미리 인사</em>부터."},
  mission={"todo": ["오늘부터 하루 하나씩 연말 위시 적기", "첫 번째 위시 지금 적기"], "cta": "어드벤트 캘린더 같이 열 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="연말 위시에<br><em>다 같이 파티</em> 한 줄 추가 ✨",
  caption="D-24 · 12월 1일, 진짜 시작 🎁\n어드벤트 캘린더 첫 칸 오픈! 오늘부터 하루 하나씩 연말 위시 적어 봐요.\n같이 칸 열 친구 태그 👇", tags="#D24 #12월"),

 dict(date_iso="2026-12-02", dday=23, date="12.02", weekday="수",
  cover="트리 설치 인증 vs<br><em>아직 박스에 있는</em> 트리.", cover_note="여러분은 어느 쪽? 🤔",
  scene_title="트리 인증 대결", scene_note="박스 쪽이 나라는 건<br>비밀 ✍️",
  scene={"type": "photo", "photos": [
      {"emoji": "🎄", "bg": "#d6f5b0", "caption": "친구네 (완벽)"},
      {"emoji": "📦", "bg": "#ffd6e5", "caption": "우리 집 (박스째)"}]},
  bgm={"title": "Christmas Tree Farm", "artist": "Taylor Swift", "year": 2019,
       "reason": "트리 농장 같은 집,<br><em>올해는 우리 집도.</em>"},
  mission={"todo": ["트리 사진 올리고 친구 태그하기", "박스파라면 오늘 저녁 꺼내기"], "cta": "트리 인증 기다리는 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="트리 꾸밀 시간 없다면,<br>이미 꾸며진 <em>파티룸</em>으로 🎄",
  caption="D-23 · 트리 인증 vs 아직 박스 📦\n벌써 트리 완성한 사람, 아직 박스째인 사람 다 모여요.\n트리 사진 올리고 친구 태그 👇", tags="#D23 #트리인증"),

 dict(date_iso="2026-12-03", dday=22, date="12.03", weekday="목",
  cover="<em>'연말에 한번 보자'</em><br>올라온 지 3일째.<br>아무도 날짜를 안 잡는다.", cover_note="이러다 내년 됨 😇",
  scene_title="날짜는 누가?", scene_note="결국 내가<br>투표 올렸다 ✍️",
  scene={"type": "chat", "room": "대학 동기들 (6)", "messages": [
      {"divider": "11월 30일 월요일"},
      {"who": "서연", "text": "연말에 한번 보자~", "time": "오후 9:20"},
      {"who": "지호", "text": "ㅇㅇ 보자 보자", "time": "오후 9:24"},
      {"divider": "12월 3일 목요일"},
      {"me": True, "text": "📊 날짜 투표 올렸어! 오늘까지!", "time": "오후 7:30", "unread": 5},
      {"me": True, "text": "@민규 @유나 너네도 투표해", "time": "오후 7:31", "unread": 5}]},
  bgm={"title": "All I Want for Christmas Is You", "artist": "Mariah Carey", "year": 1994,
       "reason": "올해 크리스마스엔<br><em>다 같이 모이는 것</em>만 있으면 돼."},
  mission={"todo": ["단톡방에 날짜 투표 올리기", "답 없는 친구 태그하기"], "cta": "'연말에 보자'만 하고 조용한 친구,<br><em>여기 태그로 소환</em> 👇"},
  merryhood_line="날짜 잡혔으면 장소는<br><em>메리후드</em>, 예약은 DM 🎄",
  caption="D-22 · '연말에 한번 보자' 3일째 😇\n날짜는 아무도 안 잡는다면? 오늘 투표 올리는 사람이 총대예요.\n답 없는 친구 태그 👇", tags="#D22 #연말모임"),
]

out = Path("days"); out.mkdir(exist_ok=True)
for day in W:
    iso = day.pop("date_iso")
    p = out / f"{iso}.json"
    if (Path("..") / "posts" / iso).exists():
        raise SystemExit(f"posts/{iso} already exists")
    p.write_text(json.dumps(day, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", iso)
