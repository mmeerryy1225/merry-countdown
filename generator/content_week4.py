"""4주차(D-63~D-57) 하루치 데이터 → days/YYYY-MM-DD.json"""
import json
from pathlib import Path

W = [
 dict(date_iso="2026-10-23", dday=63, date="10.23", weekday="금",
  cover="핼러윈 코스튬 <em>직구</em>했는데<br>배송 예정일이<br><em>11월</em>이란다.", cover_note="핼러윈 끝나고 오는 코스튬 🎃",
  scene_title="배송 예정 11월", scene_note="핼러윈 지나고<br>도착 예정 ✍️",
  scene={"type": "list", "style": "cart", "title": "장바구니 (5)", "items": [
      {"text": "마녀 망토 (해외직구)", "right": "11/12 도착 😱", "highlight": True},
      {"text": "호박 머리띠 🎃", "right": "11/10 도착"},
      {"text": "검정 가디건 (망토 대신)", "right": "내일 도착", "checked": True},
      {"text": "마녀 모자 (국내배송)", "right": "모레 도착", "checked": True},
      {"text": "빗자루 소품 🧹", "right": "고민 중…"}]},
  bgm={"title": "Santa Claus Is Comin' to Town", "artist": "스탠더드 캐럴", "year": 1934,
       "reason": "택배는 늦어도<br><em>산타는 제때 온다</em>는 노래."},
  mission={"todo": ["'내일 도착'만 골라서 다시 담기", "직구 코스튬은 내년 핼러윈용으로"], "cta": "직구 배송 기다리는 친구,<br><em>태그하고 같이 기다려요</em> 👇"},
  merryhood_line="코스튬은 늦어도<br><em>파티</em>는 제때 시작해요 🎃",
  caption="D-63 · 코스튬 직구했는데 배송이 11월 📦\n핼러윈 끝나고 도착하는 코스튬… 주말 전에 받을 수 있는 걸로 다시 골라요.\n직구 기다리는 친구 태그 👇", tags="#D63 #해외직구"),

 dict(date_iso="2026-10-24", dday=62, date="10.24", weekday="토",
  cover="핼러윈 파티 <em>D-7.</em><br>근데 아직<br><em>장소</em>가 안 정해졌다.", cover_note="일주일 남았는데요? 😱",
  scene_title="장소 미정 D-7", scene_note="이번 주가<br>마지노선 ✍️",
  scene={"type": "chat", "room": "핼러윈 준비방 (5)", "messages": [
      {"divider": "10월 24일 토요일"},
      {"who": "다은", "text": "얘들아 핼러윈 일주일 남았다", "time": "오후 3:10"},
      {"who": "준호", "text": "장소 정했어??", "time": "오후 3:12"},
      {"who": "다은", "text": "아직…ㅎㅎ", "time": "오후 3:12"},
      {"who": "준호", "text": "토요일이라 금방 찰 텐데", "time": "오후 3:15"},
      {"me": True, "text": "오늘 안에 내가 예약할게!", "time": "오후 3:18", "unread": 4}]},
  bgm={"title": "Deck the Halls", "artist": "웨일스 전통 캐럴", "year": "",
       "reason": "'홀을 꾸미자'는 노래,<br>근데 <em>홀부터</em> 구해야 함."},
  mission={"todo": ["장소 후보 2곳 오늘 문의 넣기", "단톡방에 예약 마감일 공지하기"], "cta": "장소 아직 미정인 단톡방 친구,<br><em>여기서 소환</em> 👇"},
  merryhood_line="핼러윈 파티 장소 급구?<br><em>메리후드</em> 예약은 DM 🎃",
  caption="D-62 · 핼러윈 D-7, 장소 미정 😱\n일주일 남았는데 아직 장소가 없다면 오늘이 마지노선이에요.\n장소 정해야 할 단톡방 친구 태그 👇", tags="#D62 #핼러윈파티"),

 dict(date_iso="2026-10-25", dday=61, date="10.25", weekday="일",
  cover="단풍 보러 갔는데<br>찍어 온 건<br><em>사람 뒤통수</em>뿐.", cover_note="단풍은 어디 갔지 🍁",
  scene_title="뒤통수 컬렉션", scene_note="단풍보다<br>사람이 많았다 ✍️",
  scene={"type": "photo", "style": "album", "title": "오늘 찍은 사진", "photos": [
      {"emoji": "👥", "bg": "#e8dccb"}, {"emoji": "👥", "bg": "#dfe7ee"}, {"emoji": "🚗", "bg": "#ffe2c4"},
      {"emoji": "👥", "bg": "#e8dccb"}, {"emoji": "🍁", "bg": "#ffd9a8", "highlight": True, "caption": "건진 1장"}, {"emoji": "👥", "bg": "#dfe7ee"},
      {"emoji": "🍢", "bg": "#ffe0d6"}, {"emoji": "👥", "bg": "#e8dccb"}, {"emoji": "👥", "bg": "#dfe7ee"}]},
  bgm={"title": "Christmas Tree Farm", "artist": "Taylor Swift", "year": 2019,
       "reason": "단풍 다음은 트리,<br><em>크리스마스 풍경</em> 미리 보기."},
  mission={"todo": ["사진첩에서 베스트 컷 한 장 고르기", "그 사진으로 프사 바꾸기"], "cta": "같이 뒤통수만 찍고 온 친구,<br><em>태그하고 추억 소환</em> 👇"},
  merryhood_line="다음엔 사람 말고<br><em>우리끼리</em> 사진 찍어요 📸",
  caption="D-61 · 단풍 보러 가서 뒤통수만 찍었다 🍁\n건진 사진 딱 한 장… 그 한 장으로 프사 바꾸기 미션!\n같이 다녀온 친구 태그 👇", tags="#D61 #단풍"),

 dict(date_iso="2026-10-26", dday=60, date="10.26", weekday="월",
  cover="크리스마스 <em>두 달</em> 전.<br>내 캘린더 속<br>연말 약속은 <em>0개.</em>", cover_note="12월이 텅텅 🫥",
  scene_title="텅 빈 12월", scene_note="약속 칸이<br>너무 넓다 ✍️",
  scene={"type": "calendar", "year": 2026, "month": 12, "circle": [25], "cross": [], "fill": [],
         "labels": {"25": "크리스마스🎄", "31": "올해 끝"}},
  bgm={"title": "Last Christmas", "artist": "Wham!", "year": 1984,
       "reason": "작년처럼 보내기 싫다면<br><em>올해는 미리</em> 약속 잡기."},
  mission={"todo": ["12월 주말 중 하루 골라 약속 넣기", "같이 보낼 친구한테 먼저 연락하기"], "cta": "12월 약속 아직 없는 친구,<br><em>여기서 먼저 잡아요</em> 👇"},
  merryhood_line="12월 주말은 금방 차요,<br><em>메리후드</em> 예약은 DM으로 🎄",
  caption="D-60 · 크리스마스 두 달 전, 연말 약속 0개 🗓\n12월 주말 하나만 미리 찜해 두세요. 두 달 금방 가요.\n12월에 볼 친구 태그 👇", tags="#D60 #연말약속"),

 dict(date_iso="2026-10-27", dday=59, date="10.27", weekday="화",
  cover="<em>'단풍 보러 가자'</em><br>했던 약속,<br>결국 아무도 안 갔다.", cover_note="단풍 다 떨어지는 중 🍂",
  scene_title="흐지부지 3주째", scene_note="다음 약속은<br>날짜부터 ✍️",
  scene={"type": "chat", "room": "단풍 원정대 (4)", "messages": [
      {"divider": "10월 3일 토요일"},
      {"who": "수아", "text": "이번 달에 단풍 보러 가자!!", "time": "오후 9:20"},
      {"who": "민재", "text": "콜 날짜만 정해", "time": "오후 9:22"},
      {"divider": "10월 27일 화요일"},
      {"me": True, "text": "얘들아 단풍 다 지겠다…", "time": "오후 8:40", "unread": 3},
      {"me": True, "text": "11월에 첫눈 보러 갈래?", "time": "오후 8:41", "unread": 3}]},
  bgm={"title": "Fairytale of New York", "artist": "The Pogues", "year": 1987,
       "reason": "엇갈린 약속도<br><em>연말엔 다시</em> 이어 볼 수 있으니까."},
  mission={"todo": ["흐지부지된 약속 하나 다시 꺼내기", "이번엔 날짜부터 박기"], "cta": "약속만 하고 잠수 탄 친구,<br><em>태그로 소환</em> 👇"},
  merryhood_line="미뤄 둔 약속,<br><em>연말 파티</em>로 한 번에 갚기 🎉",
  caption="D-59 · '단풍 보러 가자' 그 약속 🍂\n결국 아무도 안 갔죠… 흐지부지된 약속 하나, 오늘 다시 살려 봐요.\n그때 그 친구 태그 👇", tags="#D59 #약속"),

 dict(date_iso="2026-10-28", dday=58, date="10.28", weekday="수",
  cover="팀장님이 <em>송년회 장소</em><br>알아보라고 하셨다.<br><em>왜 나야?</em>", cover_note="막내도 아닌데요 🥲",
  scene_title="송년회 담당 당첨", scene_note="칭찬인지<br>일 폭탄인지 ✍️",
  scene={"type": "chat", "style": "work", "room": "기획팀 (7)", "messages": [
      {"divider": "10월 28일 수요일"},
      {"who": "팀장님", "text": "송년회 장소 좀 알아봐 줄래요?", "time": "오전 10:05"},
      {"me": True, "text": "넵…! 저요?", "time": "오전 10:07", "unread": 6},
      {"who": "팀장님", "text": "응 감각 있잖아 ㅎㅎ", "time": "오전 10:08"},
      {"who": "박 대리", "text": "오 기대할게요 👍", "time": "오전 10:09"},
      {"me": True, "text": "후보 3곳 정리해 드릴게요", "time": "오전 10:12", "unread": 6}]},
  bgm={"title": "Wonderful Christmastime", "artist": "Paul McCartney", "year": 1979,
       "reason": "떠밀려 맡았어도<br><em>근사한 송년회</em> 만들어 보자."},
  mission={"todo": ["장소 후보 3곳 비교표 만들기", "인원·예산·날짜부터 확인하기"], "cta": "송년회 담당 된 동료,<br><em>태그해서 응원</em> 👇"},
  merryhood_line="비교표 1번 후보는<br><em>홍대 메리후드</em>, 예약은 DM 📋",
  caption="D-58 · 송년회 장소, 왜 나야? 💼\n갑자기 송년회 담당 됐다면 후보 3곳 비교표부터 시작해요.\n송년회 담당 된 동료 태그 👇", tags="#D58 #송년회"),

 dict(date_iso="2026-10-29", dday=57, date="10.29", weekday="목",
  cover="<em>핼러윈 분장</em><br>연습하다가 거울 보고<br><em>현타</em> 왔다.", cover_note="이게 맞나… 🧛",
  scene_title="분장 전/후", scene_note="본 게임엔<br>나아지겠지 ✍️",
  scene={"type": "photo", "photos": [
      {"emoji": "🙂", "bg": "#d6f5b0", "caption": "분장 전"},
      {"emoji": "🧛", "bg": "#ffd6e5", "caption": "분장 후 (?)"}]},
  bgm={"title": "Christmas (Baby Please Come Home)", "artist": "Darlene Love", "year": 1963,
       "reason": "현타 온 밤엔<br><em>목청껏 캐럴</em> 한 곡이 약."},
  mission={"todo": ["분장 전/후 사진 남겨 두기", "친구한테 보내고 솔직한 평 듣기"], "cta": "분장 연습 같이 할 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="완성된 분장은<br><em>파티룸</em>에서 제대로 뽐내요 🧛",
  caption="D-57 · 핼러윈 분장 연습하다 현타 🧛\n그래도 전/후 사진은 꼭 남겨 두기. 나중엔 다 추억이에요.\n분장 같이 할 친구 태그 👇", tags="#D57 #핼러윈분장"),
]

out = Path("days"); out.mkdir(exist_ok=True)
for day in W:
    iso = day.pop("date_iso")
    p = out / f"{iso}.json"
    p.write_text(json.dumps(day, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", iso)
