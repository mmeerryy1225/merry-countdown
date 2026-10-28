"""6주차(D-49~D-43) 하루치 데이터 → days/YYYY-MM-DD.json"""
import json
from pathlib import Path

W = [
 dict(date_iso="2026-11-06", dday=49, date="11.06", weekday="금",
  cover="금요일 저녁,<br><em>연말 모임 장소</em>만<br>2시간째 검색 중.", cover_note="눈이 빠질 것 같다 👀",
  scene_title="2시간째 검색", scene_note="결국 처음 본 곳이<br>제일 좋았다 ✍️",
  scene={"type": "list", "style": "search", "title": "최근 검색어", "items": [
      {"text": "연말 모임 장소 추천", "right": "오후 7:10"},
      {"text": "10명 모일 수 있는 곳", "right": "오후 7:42"},
      {"text": "홍대 파티룸 후기", "right": "오후 8:15"},
      {"text": "파티룸 12월 예약 마감", "right": "오후 8:51"},
      {"text": "그냥 처음 본 데로 할까", "right": "오후 9:08", "highlight": True}]},
  bgm={"title": "Mistletoe", "artist": "Justin Bieber", "year": 2011,
       "reason": "검색창 닫고<br><em>설레는 연말</em>만 생각하기."},
  mission={"todo": ["장소 후보를 3개로 줄이기", "단톡방에 후보 3개 올리기"], "cta": "장소 검색 같이 할 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="2시간 검색 끝,<br>후보 1번은 <em>메리후드</em>로 📍",
  caption="D-49 · 연말 모임 장소 2시간째 검색 중 🔍\n후보는 딱 3개로 줄이고, 나머지는 단톡방에 맡겨요.\n장소 고민 같이 할 친구 태그 👇", tags="#D49 #연말모임"),

 dict(date_iso="2026-11-07", dday=48, date="11.07", weekday="토",
  cover="갑자기 추워졌다.<br>옷장 깊숙이 있던<br><em>패딩 소환.</em>", cover_note="어제랑 다른 세상 🥶",
  scene_title="하루 만에 겨울", scene_note="패딩 지퍼 끝까지<br>올렸다 ✍️",
  scene={"type": "weather", "place": "서울 마포구", "now": "3°", "icon": "🥶", "desc": "맑고 추움",
         "hi": "8°", "lo": "-1°",
         "hourly": [["9시", "0°", "🌤"], ["12시", "5°", "☀️"], ["15시", "8°", "☀️"], ["18시", "4°", "🌤"], ["21시", "1°", "🌙"]],
         "alert": "한파 주의 · 패딩 꺼낼 시간"},
  bgm={"title": "White Christmas", "artist": "Bing Crosby", "year": 1942,
       "reason": "찬 바람 불기 시작하면<br><em>하얀 크리스마스</em> 기대 시작."},
  mission={"todo": ["패딩 주머니에서 작년 영수증 찾기", "목도리도 같이 꺼내 두기"], "cta": "벌써 패딩 입은 친구,<br><em>자수하세요</em> 👇"},
  merryhood_line="추운 날엔<br><em>따뜻한 실내 파티</em>가 최고 ☕",
  caption="D-48 · 갑자기 패딩 소환 🧥\n주머니에서 작년 영수증 나온 사람 손! 작년의 나는 뭘 샀을까요.\n벌써 패딩 입은 친구 태그 👇", tags="#D48 #패딩"),

 dict(date_iso="2026-11-08", dday=47, date="11.08", weekday="일",
  cover="단톡방에서 누군가<br><em>'시크릿 산타 하자!'</em><br>라고 했다.", cover_note="갑자기 두근두근 🎁",
  scene_title="시크릿 산타 결성", scene_note="장소도 이참에<br>정해 버렸다 ✍️",
  scene={"type": "chat", "room": "우리끼리 연말 (6)", "messages": [
      {"divider": "11월 8일 일요일"},
      {"who": "민지", "text": "올해 시크릿 산타 하자!! 🎅", "time": "오후 4:12"},
      {"who": "현우", "text": "오 좋다 제비뽑기 누가 함?", "time": "오후 4:14"},
      {"who": "민지", "text": "선물 교환은 연말 파티 때!", "time": "오후 4:15"},
      {"me": True, "text": "제비뽑기 내가 만들게!", "time": "오후 4:20", "unread": 5}]},
  bgm={"title": "Santa Tell Me", "artist": "Ariana Grande", "year": 2014,
       "reason": "내 산타는 누구일까,<br><em>두근두근</em> 기다리는 노래."},
  mission={"todo": ["시크릿 산타 제비뽑기 만들기", "선물 교환할 날짜·장소 정하기"], "cta": "시크릿 산타 같이 할 친구,<br><em>여기서 모집</em> 👇"},
  merryhood_line="선물 교환 파티는<br><em>메리후드</em>에서, 예약은 DM 🎁",
  caption="D-47 · 시크릿 산타 하자! 🎅\n제비뽑기 만드는 사람이 오늘의 총대예요. 선물 교환 날짜도 같이 정해요.\n시크릿 산타 같이 할 친구 태그 👇", tags="#D47 #시크릿산타"),

 dict(date_iso="2026-11-09", dday=46, date="11.09", weekday="월",
  cover="회사 <em>송년회 날짜</em><br>공지가 떴다.<br>하필 금요일.", cover_note="2차 각이다… 🫠",
  scene_title="송년회 공지 떴다", scene_note="2차는 미리<br>정해 두는 걸로 ✍️",
  scene={"type": "chat", "style": "work", "room": "전체 공지 (24)", "messages": [
      {"divider": "11월 9일 월요일"},
      {"who": "총무팀", "text": "올해 송년회는 12월 18일(금)입니다", "time": "오전 9:05"},
      {"who": "김 과장", "text": "금요일이면 2차 각이네요 ㅎㅎ", "time": "오전 9:08"},
      {"who": "총무팀", "text": "2차는 자율입니다~", "time": "오전 9:10"},
      {"me": True, "text": "넵 확인했습니다!", "time": "오전 9:12", "unread": 23}]},
  bgm={"title": "Thank God It's Christmas", "artist": "Queen", "year": 1984,
       "reason": "송년회 지나면<br><em>진짜 크리스마스</em>가 온다."},
  mission={"todo": ["그날 2차 갈지 말지 미리 정하기", "다음 날 아침 일정 비워 두기"], "cta": "금요일 송년회 같이 갈 동료,<br><em>태그해서 작전 회의</em> 👇"},
  merryhood_line="2차는 우리끼리<br><em>편한 곳</em>에서 할까요 🎉",
  caption="D-46 · 송년회 공지, 하필 금요일 📢\n2차 갈지 말지 오늘 미리 정해 두면 그날이 편해요.\n송년회 같이 갈 동료 태그 👇", tags="#D46 #송년회"),

 dict(date_iso="2026-11-10", dday=45, date="11.10", weekday="화",
  cover="빼빼로데이 전날 밤,<br>편의점 앞<br><em>대란</em> 현장.", cover_note="남은 건 한 박스뿐 😱",
  scene_title="편의점 앞 대란", scene_note="마지막 한 박스<br>겨우 건졌다 ✍️",
  scene={"type": "photo", "photos": [
      {"emoji": "🏪", "bg": "#ffd6e5", "caption": "밤 11시 편의점 앞"},
      {"emoji": "🍫", "bg": "#d6f5b0", "caption": "마지막 한 박스 득템"}]},
  bgm={"title": "Rockin' Around the Christmas Tree", "artist": "Brenda Lee", "year": 1958,
       "reason": "편의점 대란도<br><em>신나게</em> 뚫고 지나가기."},
  mission={"todo": ["챙겨 줄 사람 리스트 체크하기", "내일 아침에 건넬 순서 정하기"], "cta": "빼빼로 챙겨 줄 친구,<br><em>미리 태그</em> 👇"},
  merryhood_line="빼빼로 다음은<br><em>연말 파티</em> 준비 🎄",
  caption="D-45 · 빼빼로데이 전날 편의점 대란 🏪\n챙겨 줄 사람 리스트, 빠진 사람 없는지 한 번 더 체크!\n빼빼로 줄 친구 미리 태그 👇", tags="#D45 #빼빼로데이"),

 dict(date_iso="2026-11-11", dday=44, date="11.11", weekday="수",
  cover="빼빼로데이.<br>받은 건 <em>0개,</em><br>준 건 5개.", cover_note="이게 맞나… 🥲",
  scene_title="받은 건 0개", scene_note="내가 나한테<br>사 주기로 했다 ✍️",
  scene={"type": "chat", "room": "찐친 5인방 (5)", "messages": [
      {"divider": "11월 11일 수요일"},
      {"who": "서연", "text": "빼빼로 고마워 🥹", "time": "오후 12:30"},
      {"who": "준호", "text": "나도 잘 먹을게!!", "time": "오후 12:41"},
      {"who": "다은", "text": "근데 넌 몇 개 받았어?", "time": "오후 12:45"},
      {"me": True, "text": "…0개 ㅎㅎ", "time": "오후 12:50", "unread": 4}]},
  bgm={"title": "Christmas (Baby Please Come Home)", "artist": "Darlene Love", "year": 1963,
       "reason": "0개여도 괜찮아,<br><em>크리스마스</em>가 오고 있으니까."},
  mission={"todo": ["나한테도 하나 사 주기", "준 친구들한테 맛있었는지 물어보기"], "cta": "빼빼로 0개 동지,<br><em>여기 모여요</em> 👇"},
  merryhood_line="주는 기쁨 아는 우리,<br><em>연말 파티</em>도 같이해요 💌",
  caption="D-44 · 빼빼로데이, 받은 건 0개 🍫\n준 사람이 진짜 승자예요. 오늘은 나한테도 하나 사 주기!\n빼빼로 0개 동지 태그 👇", tags="#D44 #빼빼로데이"),

 dict(date_iso="2026-11-12", dday=43, date="11.12", weekday="목",
  cover="시크릿 산타 선물 예산,<br><em>1만 원 vs 3만 원</em><br>논쟁 발발.", cover_note="단톡방 분위기 심각 😤",
  scene_title="예산 다수결", scene_note="결국 2만 원으로<br>합의했다 ✍️",
  scene={"type": "list", "style": "vote", "title": "시크릿 산타 예산", "sub": "6명 참여 · 오늘 밤 마감", "items": [
      {"text": "1만 원 (부담 없이)", "right": "2표", "bar": 33},
      {"text": "2만 원 (딱 중간)", "right": "3표", "bar": 50, "highlight": True},
      {"text": "3만 원 (제대로)", "right": "1표", "bar": 17},
      {"text": "금액 상관없음", "right": "0표", "bar": 0, "dim": True},
      {"text": "손편지면 충분", "right": "0표", "bar": 0, "dim": True}]},
  bgm={"title": "Underneath the Tree", "artist": "Kelly Clarkson", "year": 2013,
       "reason": "선물 가격보다<br><em>트리 아래 모이는 게</em> 중요."},
  mission={"todo": ["예산 투표 올리고 다수결로 끝내기", "정해진 예산으로 선물 후보 3개 찾기"], "cta": "예산 논쟁 중인 친구,<br><em>태그해서 투표 독려</em> 👇"},
  merryhood_line="선물 교환할 장소는<br><em>여기서</em> 정해요 🎁",
  caption="D-43 · 시크릿 산타 예산 논쟁 💸\n길어지면 투표로 끝내요. 다수결이 평화를 지킵니다.\n예산 논쟁 중인 친구 태그 👇", tags="#D43 #시크릿산타"),
]

out = Path("days"); out.mkdir(exist_ok=True)
for day in W:
    iso = day.pop("date_iso")
    p = out / f"{iso}.json"
    if Path("../posts", iso).exists():
        raise SystemExit(f"{iso} already in posts/, refusing")
    p.write_text(json.dumps(day, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", iso)
