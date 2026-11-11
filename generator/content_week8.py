"""8주차(D-35~D-29) 하루치 데이터 → days/YYYY-MM-DD.json"""
import json
from pathlib import Path

W = [
 dict(date_iso="2026-11-20", dday=35, date="11.20", weekday="금",
  cover="불금 단톡방에 던진 질문,<br><em>'크리스마스이브에 뭐 함?'</em><br>아무도 대답이 없다.", cover_note="다들 바쁜 척 중 🙄",
  scene_title="정적의 단톡방", scene_note="결국 내가 먼저<br>제안하기로 했다 ✍️",
  scene={"type": "chat", "room": "불금엔 우리 (5)", "messages": [
      {"divider": "11월 20일 금요일"},
      {"me": True, "text": "크리스마스이브에 뭐 함?", "time": "오후 7:02", "unread": 4},
      {"me": True, "text": "…다들 어디 감?", "time": "오후 8:15", "unread": 4},
      {"who": "민재", "text": "아직 아무 계획 없음ㅋㅋ", "time": "오후 9:40"},
      {"me": True, "text": "그럼 우리끼리 파티 ㄱ?", "time": "오후 9:41", "unread": 3}]},
  bgm={"title": "Last Christmas", "artist": "Wham!", "year": 1984,
       "reason": "작년처럼 흐지부지 말고,<br><em>올해는 먼저</em> 잡기."},
  mission={"todo": ["이브 계획 먼저 단톡방에 제안하기", "날짜·장소 후보까지 같이 던지기"], "cta": "이브에 아직 계획 없는 친구,<br><em>여기 태그로 소환</em> 👇"},
  merryhood_line="이브 파티 장소는<br><em>메리후드</em>, 예약은 DM 🎄",
  caption="D-35 · '크리스마스이브에 뭐 함?' 🤫\n불금 단톡방이 조용하다면, 먼저 제안하는 사람이 이기는 거예요.\n이브 계획 없는 친구 태그 👇", tags="#D35 #크리스마스이브"),

 dict(date_iso="2026-11-21", dday=34, date="11.21", weekday="토",
  cover="파티룸 예약하려고 봤더니<br><em>12월 주말</em>이<br>거의 마감이다.", cover_note="다들 언제 예약한 거야 😱",
  scene_title="주말은 이미", scene_note="남은 날 하나<br>바로 찜했다 ✍️",
  scene={"type": "calendar", "year": 2026, "month": 12, "circle": [26],
         "cross": [5, 6, 12, 13, 19, 20], "fill": [],
         "labels": {"5": "마감", "12": "마감", "19": "마감", "26": "남은 자리!"}},
  bgm={"title": "It's Beginning to Look a Lot Like Christmas", "artist": "Michael Bublé", "year": 2011,
       "reason": "예약 화면부터<br><em>크리스마스 느낌</em> 물씬."},
  mission={"todo": ["원하는 날짜 오늘 바로 문의하기", "안 되면 평일 저녁도 후보에 넣기"], "cta": "예약 담당 맡은 친구,<br><em>여기 태그해서 재촉</em> 👇"},
  merryhood_line="12월 날짜 남았는지<br><em>메리후드 DM</em>으로 바로 물어보세요 📅",
  caption="D-34 · 12월 주말, 벌써 마감 행진 😱\n파티룸 예약은 지금이 마지막 타이밍. 원하는 날짜 있으면 오늘 바로 문의해요.\n예약 담당 친구 태그 👇", tags="#D34 #파티룸예약"),

 dict(date_iso="2026-11-22", dday=33, date="11.22", weekday="일",
  cover="연말 사진 잘 나오려고<br><em>미용실 예약</em>할까<br>고민 중.", cover_note="사진은 남으니까 💇",
  scene_title="미용실 상담", scene_note="결국 모임 전날로<br>예약 완료 ✍️",
  scene={"type": "chat", "style": "work", "room": "동네 미용실 예약 문의", "messages": [
      {"divider": "11월 22일 일요일"},
      {"me": True, "text": "12월 중순에 예약 가능할까요?", "time": "오후 2:10"},
      {"who": "원장님", "text": "연말이라 주말은 거의 찼어요ㅠ", "time": "오후 2:14"},
      {"who": "원장님", "text": "18일 금요일 저녁 한 자리 있어요!", "time": "오후 2:15"},
      {"me": True, "text": "그날로 할게요!!", "time": "오후 2:16"}]},
  bgm={"title": "Sleigh Ride", "artist": "The Ronettes", "year": 1963,
       "reason": "썰매 타듯 신나게,<br><em>연말 준비</em> 하나씩."},
  mission={"todo": ["연말 모임 전에 미용실 예약하기", "모임 날짜 다시 확인하기"], "cta": "연말 맞이 변신 계획 있는 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="예쁘게 하고 와서<br><em>연말 사진</em> 남겨요 📸",
  caption="D-33 · 연말 사진 대비, 미용실 예약 💇\n12월은 미용실도 예약 전쟁이래요. 모임 날짜 정해졌으면 미리 잡아 두기!\n같이 변신할 친구 태그 👇", tags="#D33 #연말준비"),

 dict(date_iso="2026-11-23", dday=32, date="11.23", weekday="월",
  cover="월요일인데<br>마음은 이미<br><em>12월</em>에 가 있다.", cover_note="몸만 출근함 🫠",
  scene_title="마음은 12월", scene_note="이번 주만 버티면<br>보상 있음 ✍️",
  scene={"type": "calendar", "year": 2026, "month": 11, "circle": [28],
         "cross": list(range(1, 23)), "fill": [23],
         "labels": {"23": "월요일😵", "28": "보상🎁"}},
  bgm={"title": "Jingle Bells", "artist": "전통 캐럴", "year": 1857,
       "reason": "월요일 아침에도<br><em>방울 소리</em>처럼 가볍게."},
  mission={"todo": ["이번 주 버틸 보상 하나 정하기", "달력에 보상 날짜 표시하기"], "cta": "몸만 출근한 친구,<br><em>태그하고 서로 응원</em> 👇"},
  merryhood_line="이번 주 보상은<br><em>주말 파티</em>로 🎁",
  caption="D-32 · 몸은 월요일, 마음은 12월 🗓\n이번 주 버틸 보상 하나 정해 두면 훨씬 낫더라고요.\n같이 버틸 친구 태그 👇", tags="#D32 #월요병"),

 dict(date_iso="2026-11-24", dday=31, date="11.24", weekday="화",
  cover="시크릿 산타 뽑았는데<br><em>제일 어색한 사람</em>이<br>나왔다.", cover_note="이거 어떡하죠 😅",
  scene_title="몰래 조사 중", scene_note="취향 조사는<br>007 작전처럼 ✍️",
  scene={"type": "chat", "room": "시크릿 산타 작전 (3)", "messages": [
      {"divider": "11월 24일 화요일"},
      {"me": True, "text": "나 시크릿 산타 누구 뽑았게…", "time": "오후 8:05", "unread": 2},
      {"who": "지수", "text": "설마 그 사람?ㅋㅋㅋ", "time": "오후 8:06"},
      {"me": True, "text": "응… 말 거의 안 해 봄", "time": "오후 8:06", "unread": 2},
      {"who": "현우", "text": "SNS부터 슬쩍 보자 🕵️", "time": "오후 8:08"}]},
  bgm={"title": "Mistletoe", "artist": "Justin Bieber", "year": 2011,
       "reason": "어색함도 녹이는<br><em>설레는 연말</em> 분위기."},
  mission={"todo": ["그 사람 취향 몰래 조사하기", "부담 없는 선물 후보 3개 고르기"], "cta": "시크릿 산타 같이 하는 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="시크릿 산타 공개는<br><em>연말 파티</em>에서 두근두근 🎁",
  caption="D-31 · 시크릿 산타, 하필 그 사람 😅\n어색한 사이일수록 선물 하나로 확 가까워지기도 해요. 몰래 취향 조사 시작!\n시크릿 산타 멤버 태그 👇", tags="#D31 #시크릿산타"),

 dict(date_iso="2026-11-25", dday=30, date="11.25", weekday="수",
  cover="<em>D-30!</em><br>한 달 남은 크리스마스.<br>내 계획은 아직 0.", cover_note="한 줄이라도 써 보자 ✏️",
  scene_title="텅 빈 12월", scene_note="25일에 하트 하나<br>그려 놓고 시작 ✍️",
  scene={"type": "calendar", "year": 2026, "month": 12, "circle": [25], "cross": [], "fill": [24],
         "labels": {"24": "이브", "25": "크리스마스🎄"}},
  bgm={"title": "One More Sleep", "artist": "Leona Lewis", "year": 2013,
       "reason": "한 밤씩 세다 보면<br><em>금방 크리스마스.</em>"},
  mission={"todo": ["크리스마스 계획 딱 한 줄로 정하기", "같이 보낼 사람한테 오늘 연락하기"], "cta": "계획 0인 친구,<br><em>여기 태그해서 같이 짜기</em> 👇"},
  merryhood_line="계획 한 줄 정했으면,<br>장소는 <em>메리후드</em>에 예약 DM 🎄",
  caption="D-30 · 크리스마스까지 딱 한 달 🎄\n계획이 아직 0이어도 괜찮아요. 오늘 딱 한 줄만 정해 봐요.\n같이 계획 짤 친구 태그 👇", tags="#D30 #한달전"),

 dict(date_iso="2026-11-26", dday=29, date="11.26", weekday="목",
  cover="월급 들어오자마자<br><em>장바구니</em>부터 열었다.", cover_note="통장아 미안 💸",
  scene_title="월급날 장바구니", scene_note="선물 예산은<br>따로 빼 두기로 ✍️",
  scene={"type": "list", "style": "cart", "title": "장바구니 (5)", "items": [
      {"text": "가족 선물 세트 🎁", "right": "선물 예산", "checked": True},
      {"text": "시크릿 산타 선물", "right": "2만 원 이하", "checked": True},
      {"text": "크리스마스 니트 🧶", "right": "고민 중…"},
      {"text": "트리 전구 🎄", "right": "29,900원", "checked": True},
      {"text": "나한테 주는 선물", "right": "일단 담음", "highlight": True}]},
  bgm={"title": "Rockin' Around the Christmas Tree", "artist": "Brenda Lee", "year": 1958,
       "reason": "장바구니 담는 손이<br><em>저절로 신나는</em> 노래."},
  mission={"todo": ["선물 예산부터 따로 빼 두기", "장바구니 꼭 필요한 것만 남기기"], "cta": "월급날 장바구니 연 친구,<br><em>자수하세요</em> 👇"},
  merryhood_line="선물 들고 모이는<br><em>연말 파티</em>가 기다려요 🎉",
  caption="D-29 · 월급날, 장바구니부터 열었다 💸\n선물 예산 먼저 빼 두면 마음 편하게 쇼핑할 수 있어요.\n장바구니 자수할 친구 태그 👇", tags="#D29 #월급날"),
]

out = Path("days"); out.mkdir(exist_ok=True)
for day in W:
    iso = day.pop("date_iso")
    p = out / f"{iso}.json"
    if (Path("..") / "posts" / iso).exists():
        raise SystemExit(f"posts/{iso} already exists")
    p.write_text(json.dumps(day, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", iso)
