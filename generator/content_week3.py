"""3주차(D-70~D-64) 하루치 데이터 → days/YYYY-MM-DD.json"""
import json
from pathlib import Path

W = [
 dict(date_iso="2026-10-16", dday=70, date="10.16", weekday="금",
  cover="불금인데 결국 집.<br><em>크리스마스 영화</em>만<br>계속 찾아보는 중.", cover_note="10월인데 벌써요? 🎬",
  scene_title="불금의 검색 기록", scene_note="결국 한 편도<br>못 골랐다 ✍️",
  scene={"type": "list", "style": "search", "title": "최근 검색어", "items": [
      {"text": "크리스마스 영화 추천", "right": "오후 9:02"},
      {"text": "혼자 보기 좋은 연말 영화", "right": "오후 9:15"},
      {"text": "크리스마스 영화 순위", "right": "오후 9:40"},
      {"text": "10월에 캐럴 이상함?", "right": "오후 10:03"},
      {"text": "크리스마스 영화 OST", "right": "오후 10:31", "highlight": True}]},
  bgm={"title": "Have Yourself a Merry Little Christmas", "artist": "Judy Garland", "year": 1944,
       "reason": "옛날 영화 속에서 태어난<br><em>원조 크리스마스 영화 곡.</em>"},
  mission={"todo": ["올해 볼 크리스마스 영화 리스트 저장하기", "12월에 같이 볼 친구 한 명 정하기"], "cta": "크리스마스 영화 같이 볼 친구,<br><em>여기 태그해 주세요</em> 👇"},
  merryhood_line="영화는 집에서도 좋지만<br><em>같이 보면</em> 더 좋아요 🎬",
  caption="D-70 · 불금인데 결국 집 🎬\n크리스마스 영화 검색만 1시간째… 여러분의 인생 크리스마스 영화는 뭐예요?\n같이 볼 친구 태그 👇", tags="#D70 #크리스마스영화"),

 dict(date_iso="2026-10-17", dday=69, date="10.17", weekday="토",
  cover="<em>핼러윈 코스튬</em><br>뭐 할지 단톡방<br>회의 시작.", cover_note="회의만 3시간째 🎃",
  scene_title="코스튬 대책 회의", scene_note="날짜부터 정하자<br>얘들아 ✍️",
  scene={"type": "chat", "room": "핼러윈 준비방 (5)", "messages": [
      {"divider": "10월 17일 토요일"},
      {"who": "다은", "text": "올해 코스튬 뭐 할 거야??", "time": "오후 2:10"},
      {"who": "준호", "text": "난 무조건 호박 🎃", "time": "오후 2:12"},
      {"who": "다은", "text": "근데 우리 어디서 모여?", "time": "오후 2:15"},
      {"who": "준호", "text": "날짜도 아직 안 정했잖아ㅋㅋ", "time": "오후 2:16"},
      {"me": True, "text": "파티룸 빌리자! 내가 알아볼게", "time": "오후 2:20", "unread": 4}]},
  bgm={"title": "Run Rudolph Run", "artist": "Chuck Berry", "year": 1958,
       "reason": "핼러윈 지나면 바로 연말,<br><em>신나게 달려 볼</em> 시간."},
  mission={"todo": ["핼러윈 모임 날짜부터 정하기", "코스튬은 날짜 정한 다음에 고민"], "cta": "코스튬 회의만 하는 단톡방 친구,<br><em>여기서 소환</em> 👇"},
  merryhood_line="핼러윈 파티 장소는<br><em>메리후드</em>, 예약은 DM 🎃",
  caption="D-69 · 핼러윈 코스튬 회의 시작 🎃\n코스튬 정하기 전에 날짜부터! 우리 단톡방은 아직 회의 중…\n핼러윈 같이 놀 친구 태그 👇", tags="#D69 #핼러윈"),

 dict(date_iso="2026-10-18", dday=68, date="10.18", weekday="일",
  cover="생활용품점에<br><em>크리스마스 코너</em>가 생겼다.<br>10월인데?", cover_note="근데 벌써 설렘 🎄",
  scene_title="10월의 트리 코너", scene_note="구경만 하려다<br>오너먼트 샀다 ✍️",
  scene={"type": "photo", "photos": [
      {"emoji": "🎄", "bg": "#d6f5b0", "caption": "벌써 트리 코너"},
      {"emoji": "✨", "bg": "#ffe9a0", "caption": "오너먼트 1개 득템"}]},
  bgm={"title": "Rockin' Around the Christmas Tree", "artist": "Brenda Lee", "year": 1958,
       "reason": "트리 코너 앞에서<br><em>괜히 신나는</em> 그 기분."},
  mission={"todo": ["올해 트리 장식 하나 미리 사 두기", "작년 장식 어디 뒀는지 찾아 보기"], "cta": "벌써 트리 장식 산 친구,<br><em>자수하세요</em> 👇"},
  merryhood_line="트리 앞에서 찍는 사진,<br><em>연말</em>에 같이 찍어요 📸",
  caption="D-68 · 10월인데 벌써 크리스마스 코너 🎄\n구경만 하려다가 오너먼트 하나 사 버렸어요. 여러분은 트리 언제 꺼내요?\n벌써 장식 산 친구 태그 👇", tags="#D68 #트리"),

 dict(date_iso="2026-10-19", dday=67, date="10.19", weekday="월",
  cover="친구 생일 선물 고르다가<br><em>연말 선물</em>까지<br>고민하게 됐다.", cover_note="장바구니 폭발 직전 🎁",
  scene_title="선물 장바구니", scene_note="생일 선물 사러<br>왔을 뿐인데 ✍️",
  scene={"type": "list", "style": "cart", "title": "장바구니 (5)", "items": [
      {"text": "지은 생일 선물 🎂", "right": "결제 예정", "checked": True},
      {"text": "향초 세트 (연말용)", "right": "24,900원", "checked": True},
      {"text": "엄마 목도리 🧣", "right": "32,000원"},
      {"text": "팀원 간식 박스", "right": "고민 중…"},
      {"text": "나한테 주는 선물 🎁", "right": "일단 담음", "highlight": True}]},
  bgm={"title": "Underneath the Tree", "artist": "Kelly Clarkson", "year": 2013,
       "reason": "선물보다 <em>같이 있는 사람</em>이<br>먼저 생각나는 노래."},
  mission={"todo": ["선물 줄 사람 리스트 미리 적어 두기", "생일 선물부터 먼저 결제하기"], "cta": "올해 선물 꼭 주고 싶은 친구,<br><em>태그해 주세요</em> 👇"},
  merryhood_line="선물 교환은<br><em>연말 파티</em>의 꽃 🎁",
  caption="D-67 · 생일 선물 사러 왔다가 연말 선물까지 🎁\n장바구니에 나한테 주는 선물도 하나쯤은 괜찮잖아요.\n올해 선물 주고 싶은 친구 태그 👇", tags="#D67 #선물고민"),

 dict(date_iso="2026-10-20", dday=66, date="10.20", weekday="화",
  cover="<em>일교차 15도.</em><br>아침엔 패딩,<br>낮엔 반팔.", cover_note="옷 고르다 지각할 뻔 🧥",
  scene_title="오늘의 옷 난이도", scene_note="결국 다 껴입고<br>들고 다님 ✍️",
  scene={"type": "weather", "place": "서울 마포구", "now": "7°", "icon": "🌤", "desc": "대체로 맑음", "hi": "22°", "lo": "7°",
         "hourly": [["7시", "7°", "🌫"], ["10시", "13°", "🌤"], ["13시", "21°", "☀️"], ["16시", "22°", "☀️"], ["19시", "14°", "🌙"]],
         "alert": "일교차 15도 · 외투 꼭 챙기세요"},
  bgm={"title": "Snowman", "artist": "Sia", "year": 2017,
       "reason": "아직 눈은 없지만<br><em>아침 공기</em>는 벌써 겨울."},
  mission={"todo": ["외투 하나는 꼭 챙기기", "겨울 패딩 꺼내서 바람 쐬어 두기"], "cta": "아침엔 패딩, 낮엔 반팔인 친구,<br><em>태그하고 공감</em> 👇"},
  merryhood_line="추워지면 생각나는<br><em>따뜻한 연말 모임</em> 🎄",
  caption="D-66 · 일교차 15도 🌡\n아침엔 패딩, 낮엔 반팔… 오늘 뭐 입고 나왔어요?\n같이 옷 고민하는 친구 태그 👇", tags="#D66 #일교차"),

 dict(date_iso="2026-10-21", dday=65, date="10.21", weekday="수",
  cover="회사 동기가 말했다.<br><em>'올해 송년회는<br>우리끼리 하자.'</em>", cover_note="이 말 기다렸다 🥹",
  scene_title="동기 송년회 결성", scene_note="회사 송년회보다<br>더 기대됨 ✍️",
  scene={"type": "chat", "style": "work", "room": "입사 동기 (5)", "messages": [
      {"divider": "10월 21일 수요일"},
      {"who": "민재", "text": "올해 송년회는 우리끼리 하자", "time": "오후 12:40"},
      {"who": "서연", "text": "찬성!! 진짜 오랜만이다", "time": "오후 12:41"},
      {"who": "민재", "text": "12월 금요일 중에 언제 돼?", "time": "오후 12:43"},
      {"me": True, "text": "내가 날짜 투표 올릴게!", "time": "오후 12:45", "unread": 4}]},
  bgm={"title": "Jingle Bell Rock", "artist": "Bobby Helms", "year": 1957,
       "reason": "송년회 얘기만 나와도<br><em>어깨가 들썩</em>이는 노래."},
  mission={"todo": ["동기 송년회 날짜 투표 올리기", "12월 금요일 일정 미리 비워 두기"], "cta": "올해 송년회 같이 할 동기,<br><em>여기서 소환</em> 👇"},
  merryhood_line="동기 송년회 장소,<br><em>메리후드</em>로 예약 DM 🎉",
  caption="D-65 · '올해 송년회는 우리끼리 하자' 💼\n회사 송년회 말고, 진짜 편한 사람들끼리 하는 송년회.\n같이 할 동기 태그 👇", tags="#D65 #송년회"),

 dict(date_iso="2026-10-22", dday=64, date="10.22", weekday="목",
  cover="<em>핼러윈 파티</em> 초대를<br>받았는데<br>입을 게 없다.", cover_note="옷장 앞에서 멍… 👻",
  scene_title="코스튬 급구", scene_note="옷장이 답이다<br>(아마도) ✍️",
  scene={"type": "chat", "room": "대학 친구들 (6)", "messages": [
      {"divider": "10월 22일 목요일"},
      {"who": "유나", "text": "핼러윈 파티 다들 오는 거지?", "time": "오후 8:05"},
      {"who": "유나", "text": "드레스코드는 코스튬 필수 👻", "time": "오후 8:05"},
      {"who": "현우", "text": "나 이미 준비 끝남ㅋㅋ", "time": "오후 8:10"},
      {"me": True, "text": "나 입을 게 없는데…?", "time": "오후 8:14", "unread": 5}]},
  bgm={"title": "Christmas Wrapping", "artist": "The Waitresses", "year": 1981,
       "reason": "준비 하나도 못 한 사람의<br><em>연말 주제가.</em>"},
  mission={"todo": ["옷장에 있는 걸로 코스튬 하나 만들어 보기", "소품 하나만 사서 포인트 주기"], "cta": "코스튬 아직 못 정한 친구,<br><em>태그하고 같이 고민</em> 👇"},
  merryhood_line="코스튬 완성하면<br><em>파티룸</em>에서 사진 남겨요 🎃",
  caption="D-64 · 핼러윈 초대받았는데 입을 게 없다 👻\n옷장 속 옷으로 코스튬 만들기 도전! 여러분은 뭐 입어요?\n코스튬 못 정한 친구 태그 👇", tags="#D64 #핼러윈코스튬"),
]

out = Path("days"); out.mkdir(exist_ok=True)
for day in W:
    iso = day.pop("date_iso")
    p = out / f"{iso}.json"
    p.write_text(json.dumps(day, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", iso)
