"""7주차(D-42~D-36) 하루치 데이터 → days/YYYY-MM-DD.json"""
import json
from pathlib import Path

W = [
 dict(date_iso="2026-11-13", dday=42, date="11.13", weekday="금",
  cover="13일의 금요일인데<br><em>연말 약속</em>이 확정됐다.<br>오히려 좋아.", cover_note="불길한 날? 우린 럭키 🍀",
  scene_title="드디어 확정", scene_note="확정 공지에<br>박수 이모지 폭발 ✍️",
  scene={"type": "chat", "room": "연말엔 우리 (5)", "messages": [
      {"divider": "11월 13일 금요일"},
      {"who": "서연", "text": "투표 마감! 12월 19일 토요일로 확정 🎉", "time": "오후 6:30"},
      {"who": "준호", "text": "13일의 금요일에 확정이라니ㅋㅋ", "time": "오후 6:32"},
      {"who": "다은", "text": "오히려 좋아 👏👏", "time": "오후 6:33"},
      {"me": True, "text": "캘린더에 바로 넣었다!", "time": "오후 6:35", "unread": 4}]},
  bgm={"title": "Happy Xmas (War Is Over)", "artist": "John Lennon & Yoko Ono", "year": 1971,
       "reason": "날짜가 정해졌으니<br><em>올해도 다 같이</em> 모이는 거다."},
  mission={"todo": ["확정된 약속 캘린더에 바로 넣기", "장소 예약까지 오늘 끝내기"], "cta": "약속 확정된 친구들,<br><em>여기 태그로 출석</em> 👇"},
  merryhood_line="날짜 확정됐으면<br>장소는 <em>메리후드</em>, 예약은 DM 📅",
  caption="D-42 · 13일의 금요일, 연말 약속 확정 🍀\n불길한 날이라던데 우리한텐 럭키데이. 캘린더에 바로 넣어요.\n약속 확정된 친구 태그 👇", tags="#D42 #13일의금요일"),

 dict(date_iso="2026-11-14", dday=41, date="11.14", weekday="토",
  cover="올해 <em>첫 붕어빵</em> 발견.<br>팥 vs 슈크림,<br>당신의 선택은?", cover_note="고민하다 둘 다 삼 🐟",
  scene_title="올해 첫 붕어빵", scene_note="결국 반반으로<br>샀다 ✍️",
  scene={"type": "photo", "photos": [
      {"emoji": "🐟", "bg": "#ffd6e5", "caption": "팥 붕어빵 3마리"},
      {"emoji": "🍮", "bg": "#d6f5b0", "caption": "슈크림 붕어빵 3마리"}]},
  bgm={"title": "Cozy Little Christmas", "artist": "Katy Perry", "year": 2018,
       "reason": "따끈한 붕어빵처럼<br><em>포근한</em> 겨울 주말."},
  mission={"todo": ["붕어빵 파는 곳 친구한테 공유하기", "팥 vs 슈크림 투표 올리기"], "cta": "붕어빵 같이 사 먹을 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="따끈한 간식 들고<br><em>포근한 연말</em> 보내요 ☕",
  caption="D-41 · 올해 첫 붕어빵 발견 🐟\n팥이냐 슈크림이냐, 댓글로 투표해 주세요!\n붕어빵 같이 먹을 친구 태그 👇", tags="#D41 #붕어빵"),

 dict(date_iso="2026-11-15", dday=40, date="11.15", weekday="일",
  cover="D-40.<br>크리스마스 당일에<br><em>약속 없는 사람 손?</em>", cover_note="🙋 저요 저요",
  scene_title="손 들어 보세요", scene_note="손 든 사람끼리<br>모이기로 했다 ✍️",
  scene={"type": "chat", "room": "동네 친구들 (6)", "messages": [
      {"divider": "11월 15일 일요일"},
      {"who": "유나", "text": "크리스마스 당일 약속 없는 사람 손", "time": "오후 2:10"},
      {"who": "재민", "text": "🙋", "time": "오후 2:11"},
      {"who": "하은", "text": "🙋🙋", "time": "오후 2:11"},
      {"who": "유나", "text": "그럼 우리끼리 파티하자!", "time": "오후 2:13"},
      {"me": True, "text": "나도 🙋 끼워 줘!", "time": "오후 2:15", "unread": 5}]},
  bgm={"title": "Blue Christmas", "artist": "Elvis Presley", "year": 1957,
       "reason": "쓸쓸한 크리스마스는<br><em>올해로 끝.</em>"},
  mission={"todo": ["이브·당일 같이 보낼 사람 찾기", "손 든 사람끼리 단톡방 만들기"], "cta": "크리스마스에 약속 없는 친구,<br><em>여기서 손 들어요</em> 🙋"},
  merryhood_line="손 든 사람끼리 모이는 날,<br><em>메리후드</em>에서 파티해요 🎄",
  caption="D-40 · 크리스마스 당일 약속 없는 사람 손? 🙋\n손 든 사람끼리 모이면 그게 바로 크리스마스 파티예요.\n같이 손 들 친구 태그 👇", tags="#D40 #크리스마스약속"),

 dict(date_iso="2026-11-16", dday=39, date="11.16", weekday="월",
  cover="친구가 연말 파티<br><em>드레스코드</em>를<br>정하자고 한다.", cover_note="옷장부터 열어 봄 👗",
  scene_title="드레스코드 회의", scene_note="빨강으로 거의<br>확정 분위기 ✍️",
  scene={"type": "chat", "room": "연말 파티 준비방 (5)", "messages": [
      {"divider": "11월 16일 월요일"},
      {"who": "지수", "text": "파티 드레스코드 정하자!!", "time": "오후 8:02"},
      {"who": "민혁", "text": "빨강 어때? 크리스마스니까 🎅", "time": "오후 8:04"},
      {"who": "소윤", "text": "난 초록 니트 있음 🎄", "time": "오후 8:05"},
      {"me": True, "text": "빨강 아니면 초록으로 하자!", "time": "오후 8:09", "unread": 4}]},
  bgm={"title": "Santa Baby", "artist": "Eartha Kitt", "year": 1953,
       "reason": "드레스코드 맞춰 입고<br><em>반짝반짝</em> 차려입는 날."},
  mission={"todo": ["드레스코드 컬러 하나 정하기", "옷장에서 그 컬러 아이템 찾기"], "cta": "드레스코드 같이 맞출 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="드레스코드 맞췄으면,<br>사진은 <em>메리후드</em>에서 📸",
  caption="D-39 · 연말 파티 드레스코드 정하기 👗\n빨강이냐 초록이냐, 한 가지 컬러만 정해도 사진이 확 달라져요.\n드레스코드 맞출 친구 태그 👇", tags="#D39 #드레스코드"),

 dict(date_iso="2026-11-17", dday=38, date="11.17", weekday="화",
  cover="회사 송년회<br><em>장기자랑</em> 공지.<br>신입은 필참이래.", cover_note="제가요…? 😳",
  scene_title="장기자랑 공지", scene_note="일단 후보곡부터<br>골라 보기로 ✍️",
  scene={"type": "chat", "style": "work", "room": "전체 공지 (24)", "messages": [
      {"divider": "11월 17일 화요일"},
      {"who": "총무팀", "text": "송년회 장기자랑 신청받습니다~", "time": "오전 10:00"},
      {"who": "총무팀", "text": "올해 신입분들은 필참입니다 😊", "time": "오전 10:01"},
      {"who": "이 대리", "text": "작년엔 제가 했죠… 화이팅", "time": "오전 10:05"},
      {"me": True, "text": "넵…! 준비해 보겠습니다", "time": "오전 10:08", "unread": 23}]},
  bgm={"title": "Christmas Wrapping", "artist": "The Waitresses", "year": 1981,
       "reason": "바쁜 연말에도<br><em>신나게</em> 한 곡 준비하기."},
  mission={"todo": ["장기자랑 후보곡 3개 뽑기", "같이 나갈 동기 한 명 섭외하기"], "cta": "장기자랑 같이 나갈 동기,<br><em>여기서 섭외</em> 👇"},
  merryhood_line="장기자랑 연습할 곳 필요하면<br><em>메리후드</em> 생각해 주세요 🎤",
  caption="D-38 · 송년회 장기자랑, 신입은 필참 🎤\n후보곡 3개만 뽑아 두면 반은 끝난 거예요. 같이 나갈 동기도 꼭 섭외!\n장기자랑 동지 태그 👇", tags="#D38 #장기자랑"),

 dict(date_iso="2026-11-18", dday=37, date="11.18", weekday="수",
  cover="수능 시즌.<br>수험생 동생한테<br><em>뭐 사 주지?</em>", cover_note="누나 마음 언니 마음 📚",
  scene_title="응원 장바구니", scene_note="제일 중요한 건<br>응원 한마디 ✍️",
  scene={"type": "list", "style": "cart", "title": "장바구니 (5)", "items": [
      {"text": "찹쌀떡 세트 🍡", "right": "15,900원", "checked": True},
      {"text": "핫팩 20개입", "right": "9,900원", "checked": True},
      {"text": "무릎 담요", "right": "12,900원", "checked": True},
      {"text": "초콜릿 한 상자 🍫", "right": "8,900원", "checked": True},
      {"text": "응원 손편지 ✉️", "right": "마음만큼", "highlight": True}]},
  bgm={"title": "It's the Most Wonderful Time of the Year", "artist": "Andy Williams", "year": 1963,
       "reason": "시험 끝나면<br><em>제일 멋진 계절</em>이 기다린다."},
  mission={"todo": ["응원 메시지 하나 보내기", "시험 끝나는 날 맛있는 거 약속하기"], "cta": "응원이 필요한 수험생 친구,<br><em>여기 태그</em> 📚"},
  merryhood_line="시험 끝난 날엔<br><em>신나는 연말</em>이 기다려요 ✨",
  caption="D-37 · 수능 시즌, 수험생 응원하기 📚\n선물도 좋지만 제일 힘이 되는 건 응원 한마디예요.\n응원하고 싶은 수험생 태그 👇", tags="#D37 #수능응원"),

 dict(date_iso="2026-11-19", dday=36, date="11.19", weekday="목",
  cover="퇴근길,<br>거리에 <em>트리 불빛</em>이<br>처음 켜졌다.", cover_note="갑자기 연말 실감 ✨",
  scene_title="첫 트리 점등", scene_note="퇴근길이<br>조금 덜 피곤했다 ✍️",
  scene={"type": "photo", "photos": [
      {"emoji": "🎄", "bg": "#ffd6e5", "caption": "퇴근길 첫 트리 불빛"},
      {"emoji": "✨", "bg": "#d6f5b0", "caption": "반짝이는 거리"}]},
  bgm={"title": "Christmas Lights", "artist": "Coldplay", "year": 2010,
       "reason": "퇴근길에 켜진 불빛,<br><em>연말이 시작됐다</em>는 신호."},
  mission={"todo": ["트리 불빛 찍어서 스토리 올리기", "보고 싶은 친구한테 사진 보내기"], "cta": "트리 보러 같이 갈 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="반짝이는 연말,<br><em>우리만의 파티</em>로 마무리해요 🎄",
  caption="D-36 · 퇴근길, 첫 트리 불빛 🎄\n거리에 불빛 켜지는 순간 연말이 실감 나요. 찍은 사진 스토리에 올려 주세요!\n트리 보러 갈 친구 태그 👇", tags="#D36 #크리스마스트리"),
]

out = Path("days"); out.mkdir(exist_ok=True)
for day in W:
    iso = day.pop("date_iso")
    p = out / f"{iso}.json"
    if (Path("..") / "posts" / iso).exists():
        raise SystemExit(f"posts/{iso} already exists")
    p.write_text(json.dumps(day, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", iso)
