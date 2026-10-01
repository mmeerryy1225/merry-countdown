"""2주차(D-77~D-71) 하루치 데이터 → days/YYYY-MM-DD.json"""
import json
from pathlib import Path

W = [
 dict(date_iso="2026-10-09", dday=77, date="10.09", weekday="금",
  cover="쉬는 날인데<br>단톡방이 <em>너무 조용하다.</em>", cover_note="다들 뭐 하는 거야 🤔",
  scene_title="읽은 사람 0명", scene_note="다들 자는 중이라고<br>믿고 싶다 ✍️",
  scene={"type": "chat", "room": "찐친 6인방 (6)", "messages": [
      {"divider": "10월 8일 목요일"},
      {"who": "지훈", "text": "내일 쉬는 날이다 ㅎㅎ", "time": "오후 11:40"},
      {"who": "예린", "text": "다들 내일 뭐 함?", "time": "오후 11:52"},
      {"divider": "10월 9일 금요일"},
      {"me": True, "text": "얘들아 오늘 뭐 해?", "time": "오후 1:15", "unread": 5},
      {"me": True, "text": "나 심심해…", "time": "오후 3:02", "unread": 5}]},
  bgm={"title": "크리스마스니까", "artist": "젤리피쉬", "year": 2012,
       "reason": "조용한 단톡방에<br><em>먼저 말 거는 용기</em> 충전용."},
  mission={"todo": ["단톡방에 '오늘 뭐 해?' 먼저 보내기", "답장 온 친구랑 바로 약속 잡기"], "cta": "오늘 연락 없는 그 친구,<br><em>여기서 불러 주세요</em> 👇"},
  merryhood_line="다 같이 쉬는 날엔<br><em>다 같이</em> 모여요 🎉",
  caption="D-77 · 쉬는 날인데 단톡방이 조용하다 📵\n먼저 '오늘 뭐 해?' 보내는 사람이 이기는 거예요.\n연락 없는 친구 태그 👇", tags="#D77 #한글날"),

 dict(date_iso="2026-10-10", dday=76, date="10.10", weekday="토",
  cover="친구 결혼식에서 만난 동창들.<br>헤어지면서 나온 말,<br><em>'연말에 한번 보자!'</em>", cover_note="이번엔 진짜일까? 🤞",
  scene_title="이번엔 진짜다", scene_note="총대 메는 사람이<br>꼭 한 명 있다 ✍️",
  scene={"type": "chat", "room": "고3 2반 동창 (8)", "messages": [
      {"divider": "10월 10일 토요일"},
      {"who": "수빈", "text": "오늘 너무 반가웠다ㅠㅠ", "time": "오후 6:20"},
      {"who": "수빈", "text": "연말에 한번 보자!!", "time": "오후 6:22"},
      {"who": "하린", "text": "콜 무조건 🙋", "time": "오후 6:22"},
      {"who": "도윤", "text": "ㅇㅋ 날짜는 누가 잡음?", "time": "오후 6:25"},
      {"me": True, "text": "내가 투표 올릴게!", "time": "오후 6:31", "unread": 7}]},
  bgm={"title": "Happy Xmas (War Is Over)", "artist": "John Lennon & Yoko Ono", "year": 1971,
       "reason": "오랜만에 모인 얼굴들,<br><em>올해가 가기 전에</em> 한 번 더."},
  mission={"todo": ["그 자리에서 날짜 후보 2개 던지기", "투표 마감일까지 정하기"], "cta": "'연말에 보자'만 하고 사라진 친구,<br><em>태그로 소환</em> 👇"},
  merryhood_line="동창회 날짜 잡혔으면,<br><em>장소</em>는 여기서 🎉",
  caption="D-76 · '연말에 한번 보자!' 🥂\n이번엔 진짜 보자고요. 총대는 오늘 이 글 본 사람이 메는 걸로.\n동창회 단톡방 친구 태그 👇", tags="#D76 #동창회"),

 dict(date_iso="2026-10-11", dday=75, date="10.11", weekday="일",
  cover="<em>전기장판</em>을 꺼냈다.<br>이불 밖은 위험한 계절 개막.", cover_note="오늘 밖에 안 나감 🛌",
  scene_title="일요일의 장바구니", scene_note="결국 트리까지<br>담았다고 한다 ✍️",
  scene={"type": "list", "style": "cart", "title": "장바구니 (5)", "items": [
      {"text": "전기장판 (2인용)", "right": "39,900원", "checked": True},
      {"text": "극세사 이불 세트", "right": "59,000원", "checked": True},
      {"text": "수면 양말 3켤레 🧦", "right": "9,900원", "checked": True},
      {"text": "귤 5kg 🍊", "right": "19,900원", "checked": True},
      {"text": "크리스마스 트리 🎄", "right": "고민 중…", "highlight": True}]},
  bgm={"title": "Winter Wonderland", "artist": "스탠더드 캐럴", "year": 1934,
       "reason": "이불 속에서 듣는<br><em>겨울 왕국</em> 미리 보기."},
  mission={"todo": ["겨울 이불 꺼내서 세탁 돌리기", "귤 한 박스 들이기"], "cta": "벌써 전기장판 꺼낸 친구,<br><em>자수하세요</em> 👇"},
  merryhood_line="이불 밖으로 나올 이유,<br><em>연말 파티</em> 하나면 충분 🎉",
  caption="D-75 · 전기장판 개시 🛌\n이불 밖은 위험해 시즌, 다들 장바구니에 뭐 담았어요?\n벌써 전기장판 꺼낸 친구 태그 👇", tags="#D75 #전기장판"),

 dict(date_iso="2026-10-12", dday=74, date="10.12", weekday="월",
  cover="월요병인데<br>크리스마스까지 <em>74일</em>이라는 사실<br>하나로 버틴다.", cover_note="버티는 중… 🫠",
  scene_title="하루씩 지우는 중", scene_note="X 치는 맛으로<br>산다 ✍️",
  scene={"type": "calendar", "year": 2026, "month": 10, "cross": list(range(1, 12)), "fill": [12],
         "labels": {"12": "월요병😵", "31": "핼러윈🎃"}},
  bgm={"title": "It's the Most Wonderful Time of the Year", "artist": "Andy Williams", "year": 1963,
       "reason": "월요일 아침이라도<br><em>제일 멋진 계절</em>이 오고 있으니까."},
  mission={"todo": ["이번 주 기대되는 일 하나 만들기", "달력에 X 치면서 버티기"], "cta": "월요병 같이 이겨낼 친구,<br><em>태그하고 서로 응원</em> 👇"},
  merryhood_line="이번 주 버틴 보상,<br><em>주말 파티</em>로 받기 🎁",
  caption="D-74 · 월요병 vs 크리스마스 🗓\n하루씩 X 치면서 버티는 중. 이번 주도 화이팅!\n같이 버틸 친구 태그 👇", tags="#D74 #월요병"),

 dict(date_iso="2026-10-13", dday=73, date="10.13", weekday="화",
  cover="벌써 <em>연말 모임 장소</em>를<br>알아보는 친구 vs<br>아무 생각 없는 나.", cover_note="J랑 P의 차이 😇",
  scene_title="우리 중 J 한 명", scene_note="J 친구 덕분에<br>올해도 산다 ✍️",
  scene={"type": "chat", "room": "연말 준비위원회 (4)", "messages": [
      {"divider": "10월 13일 화요일"},
      {"who": "소희", "text": "얘들아 연말 장소 미리 알아봤어", "time": "오후 7:02"},
      {"who": "소희", "text": "📎 홍대 파티룸 비교표.xlsx", "time": "오후 7:02"},
      {"who": "태민", "text": "벌써??? 10월인데???", "time": "오후 7:05"},
      {"who": "소희", "text": "12월 주말은 금방 마감이래", "time": "오후 7:06"},
      {"me": True, "text": "난 메뉴만 정할게 🙋", "time": "오후 7:10", "unread": 3}]},
  bgm={"title": "8 Days of Christmas", "artist": "Destiny's Child", "year": 2001,
       "reason": "크리스마스를 <em>하루라도 길게</em><br>즐기고 싶은 J의 마음."},
  mission={"todo": ["연말 모임 장소 후보 저장해 두기", "J 친구한테 고맙다고 말하기"], "cta": "우리 모임의 J 친구,<br><em>여기 태그해서 칭찬</em> 👇"},
  merryhood_line="J 친구 비교표에<br><em>메리후드</em>도 넣어 주세요 📋",
  caption="D-73 · 우리 모임의 J 📋\n10월에 벌써 연말 장소 비교표 만드는 친구, 꼭 한 명 있죠.\n그 친구 태그해서 칭찬해 주세요 👇", tags="#D73 #연말모임"),

 dict(date_iso="2026-10-14", dday=72, date="10.14", weekday="수",
  cover="회사에서 벌써<br><em>'올해 마무리'</em>라는 말이<br>나오기 시작했다.", cover_note="아직 10월 중순인데요? 😶",
  scene_title="벌써 연말 모드", scene_note="10월에 올해를<br>마무리하라니 ✍️",
  scene={"type": "chat", "style": "work", "room": "마케팅팀 (6)", "messages": [
      {"divider": "10월 14일 수요일"},
      {"who": "팀장님", "text": "다들 올해 마무리 슬슬 준비합시다", "time": "오전 9:30"},
      {"who": "박 대리", "text": "넵 알겠습니다!", "time": "오전 9:31"},
      {"who": "팀장님", "text": "그리고 송년회 장소도 미리 좀…", "time": "오전 9:33"},
      {"me": True, "text": "넵…! (벌써…?)", "time": "오전 9:35", "unread": 4}]},
  bgm={"title": "Thank God It's Christmas", "artist": "Queen", "year": 1984,
       "reason": "마무리는 아직이지만,<br><em>크리스마스는 오고 있으니까.</em>"},
  mission={"todo": ["올해 끝내야 할 일 3개만 적기", "나머지는 과감히 내년으로"], "cta": "벌써 송년회 담당 된 친구,<br><em>태그해서 위로</em> 👇"},
  merryhood_line="팀 송년회 장소 고민,<br><em>여기서</em> 끝내요 🎉",
  caption="D-72 · 벌써 '올해 마무리'? 💼\n10월 중순에 연말 모드 들어간 회사, 우리만 그런 거 아니죠?\n송년회 담당 된 동료 태그 👇", tags="#D72 #직장인공감"),

 dict(date_iso="2026-10-15", dday=71, date="10.15", weekday="목",
  cover="<em>니트</em>를 처음 꺼낸 날.<br>작년 니트는 보풀이 한가득.", cover_note="작년의 나 뭐 했니 🧶",
  scene_title="니트 시즌 개막", scene_note="결국 새 니트<br>주문했다 ✍️",
  scene={"type": "photo", "photos": [
      {"emoji": "🧶", "bg": "#ffd6e5", "caption": "작년 니트 (보풀 MAX)"},
      {"emoji": "🛒", "bg": "#d6f5b0", "caption": "새 니트 장바구니"}]},
  bgm={"title": "Santa Baby", "artist": "Eartha Kitt", "year": 1953,
       "reason": "산타한테 슬쩍<br><em>새 니트</em> 부탁해 보는 노래."},
  mission={"todo": ["보풀 제거기 장바구니에 담기", "올해 크리스마스 니트 미리 고르기"], "cta": "보풀 니트 같이 입는 친구,<br><em>태그하고 공감</em> 👇"},
  merryhood_line="새 니트 입고<br><em>연말 파티</em> 사진 찍으러 와요 📸",
  caption="D-71 · 니트 시즌 개막 🧶\n작년 니트 꺼냈더니 보풀이… 올해 크리스마스 니트는 뭐 입을 거예요?\n보풀 니트 동지 태그 👇", tags="#D71 #니트"),
]

CLOSING = """
━━━━━━━━━━
🎄 연말 파티는 홍대 파티룸 메리후드에서
📍 마포구 양화로18안길 40, 4층
👉 @mmeerryy_hood · 예약 문의는 DM

#크리스마스카운트다운 {tags} #연말 #크리스마스 #캐럴추천 #공감 #홍대파티룸 #파티룸 #연말파티 #메리후드"""

out = Path("days"); out.mkdir(exist_ok=True)
for day in W:
    iso = day.pop("date_iso")
    (out / f"{iso}.json").write_text(json.dumps(day, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", iso)
