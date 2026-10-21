"""5주차(D-56~D-50) 하루치 데이터 → days/YYYY-MM-DD.json"""
import json
from pathlib import Path

W = [
 dict(date_iso="2026-10-30", dday=56, date="10.30", weekday="금",
  cover="핼러윈 전날.<br><em>'홍대 갈 사람?'</em><br>근데 사람 엄청 많겠지?", cover_note="벌써 걱정되는 인파 😵",
  scene_title="홍대 갈까 말까", scene_note="결국 우리끼리<br>모이기로 했다 ✍️",
  scene={"type": "chat", "room": "핼러윈 원정대 (5)", "messages": [
      {"divider": "10월 30일 금요일"},
      {"who": "유나", "text": "내일 홍대 갈 사람?? 🎃", "time": "오후 8:10"},
      {"who": "재현", "text": "사람 엄청 많을 듯…", "time": "오후 8:12"},
      {"who": "유나", "text": "그럼 그냥 우리끼리 놀까", "time": "오후 8:13"},
      {"me": True, "text": "찬성 장소 내가 찾을게!", "time": "오후 8:15", "unread": 4}]},
  bgm={"title": "Sleigh Ride", "artist": "The Ronettes", "year": 1963,
       "reason": "붐비는 거리 말고<br><em>우리끼리 신나게</em> 달릴 준비."},
  mission={"todo": ["붐비는 거리 대신 모일 곳 정하기", "단톡방에 장소 후보 공유하기"], "cta": "핼러윈 같이 보낼 친구,<br><em>여기서 불러 주세요</em> 👇"},
  merryhood_line="북적이는 거리 대신<br><em>메리후드</em>에서 우리끼리 🎃",
  caption="D-56 · 핼러윈 전날, 홍대 갈까 말까 🎃\n붐비는 거리보다 우리끼리 편하게 모이는 게 더 재밌을지도.\n핼러윈 같이 보낼 친구 태그 👇", tags="#D56 #핼러윈"),

 dict(date_iso="2026-10-31", dday=55, date="10.31", weekday="토",
  cover="핼러윈 당일.<br>근데 진짜 궁금하다.<br><em>내일부터 캐럴</em> 틀어도 되는 거지?", cover_note="진지하게 묻는 중 🤔",
  scene_title="새벽의 검색 기록", scene_note="12시 땡 하면<br>바로 튼다 ✍️",
  scene={"type": "list", "style": "search", "title": "최근 검색어", "items": [
      {"text": "캐럴 언제부터 틀어도 됨", "highlight": True},
      {"text": "11월 1일 캐럴 실화", "right": "10.31"},
      {"text": "핼러윈 끝나면 크리스마스?", "right": "10.31"},
      {"text": "캐럴 플레이리스트 추천", "right": "10.30"},
      {"text": "크리스마스 D-day 계산", "right": "10.29"}]},
  bgm={"title": "Jingle Bells", "artist": "전통 캐럴", "year": 1857,
       "reason": "자정 땡 하면 틀 <em>첫 곡</em>은<br>역시 이 노래."},
  mission={"todo": ["오늘 밤 12시 땡 하면 캐럴 재생하기", "첫 곡 미리 골라 두기"], "cta": "자정에 같이 캐럴 틀 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="핼러윈 다음은<br><em>크리스마스 파티</em> 차례 🎄",
  caption="D-55 · 핼러윈 당일, 근데 캐럴은 내일부터? 🎃➡️🎄\n오늘 밤 12시 땡 하면 캐럴 재생, 같이 해요.\n자정에 캐럴 틀 친구 태그 👇", tags="#D55 #핼러윈"),

 dict(date_iso="2026-11-01", dday=54, date="11.01", weekday="일",
  cover="<em>11월 1일.</em><br>드디어 캐럴을<br><em>당당하게</em> 틀어도 되는 날.", cover_note="오늘부터 캐럴 합법 🎶",
  scene_title="캐럴 시즌 개막", scene_note="오늘 하루 종일<br>반복 재생 ✍️",
  scene={"type": "list", "style": "playlist", "title": "2026 캐럴 시즌", "sub": "11월 1일부터 재생 중", "items": [
      {"text": "All I Want for Christmas Is You", "highlight": True},
      {"text": "Jingle Bells"},
      {"text": "Sleigh Ride"},
      {"text": "Last Christmas"},
      {"text": "Winter Wonderland"}]},
  bgm={"title": "All I Want for Christmas Is You", "artist": "Mariah Carey", "year": 1994,
       "reason": "11월 1일 <em>공식 개막곡</em>은<br>역시 이 곡."},
  mission={"todo": ["오늘 첫 캐럴 듣고 스토리에 올리기", "올해 캐럴 플레이리스트 만들기"], "cta": "오늘 캐럴 같이 들을 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="캐럴 크게 틀고 놀 곳,<br><em>여기</em> 있어요 🎶",
  caption="D-54 · 11월 1일, 캐럴 시즌 개막 🎶\n이제 당당하게 틀어도 돼요. 오늘 첫 캐럴은 뭐 들었어요?\n캐럴 같이 들을 친구 태그 👇", tags="#D54 #캐럴시즌"),

 dict(date_iso="2026-11-02", dday=53, date="11.02", weekday="월",
  cover="올해 남은 주말을<br>세어 봤다.<br><em>고작 8번.</em>", cover_note="생각보다 적다 😳",
  scene_title="남은 주말 8번", scene_note="12월까지 합쳐도<br>8번뿐이라니 ✍️",
  scene={"type": "calendar", "year": 2026, "month": 11, "circle": [7, 14, 21, 28], "cross": [1], "fill": [2],
         "labels": {"2": "오늘", "7": "1번", "28": "4번"}},
  bgm={"title": "One More Sleep", "artist": "Leona Lewis", "year": 2013,
       "reason": "하루하루 세다 보면<br><em>금방 크리스마스.</em>"},
  mission={"todo": ["남은 주말에 보고 싶은 사람 이름 적기", "그중 한 명한테 먼저 연락하기"], "cta": "남은 주말 같이 보낼 친구,<br><em>여기서 찜해요</em> 👇"},
  merryhood_line="남은 주말 8번 중 하루,<br><em>메리후드</em> 예약은 DM으로 🗓",
  caption="D-53 · 올해 남은 주말, 고작 8번 🗓\n보고 싶은 사람 이름부터 적어 봐요. 생각보다 금방 차요.\n남은 주말에 볼 친구 태그 👇", tags="#D53 #남은주말"),

 dict(date_iso="2026-11-03", dday=52, date="11.03", weekday="화",
  cover="<em>'연말에 보자'</em> 단톡방 3개.<br>날짜 잡힌 방은<br><em>0개.</em>", cover_note="말만 무성한 연말 🙃",
  scene_title="보자고만 한다", scene_note="오늘은 내가<br>투표 올린다 ✍️",
  scene={"type": "chat", "room": "대학 동기 모임 (7)", "messages": [
      {"divider": "9월 2일 수요일"},
      {"who": "민지", "text": "연말에 꼭 보자!!", "time": "오후 10:40"},
      {"who": "현우", "text": "ㅇㅇ 무조건", "time": "오후 10:41"},
      {"divider": "11월 3일 화요일"},
      {"me": True, "text": "그 연말이 왔다 🗳 날짜 투표 고고", "time": "오후 7:20", "unread": 6}]},
  bgm={"title": "Merry Christmas Everyone", "artist": "Shakin' Stevens", "year": 1985,
       "reason": "<em>다 같이</em> 모이자고<br>외치는 노래."},
  mission={"todo": ["제일 오래된 단톡방에 날짜 투표 올리기", "투표 마감일까지 정하기"], "cta": "'연말에 보자'만 한 친구,<br><em>태그로 소환</em> 👇"},
  merryhood_line="날짜 잡혔으면 장소는<br><em>홍대 파티룸 메리후드</em>로 🎉",
  caption="D-52 · '연말에 보자' 방 3개, 날짜 잡힌 방 0개 🙃\n제일 오래된 단톡방에 오늘 날짜 투표 하나 올려 봐요.\n그 단톡방 친구 태그 👇", tags="#D52 #연말약속"),

 dict(date_iso="2026-11-04", dday=51, date="11.04", weekday="수",
  cover="송년회 <em>회비</em>를<br>얼마 걷을지 정하다가<br><em>싸울 뻔했다.</em>", cover_note="돈 얘기는 어려워 😅",
  scene_title="회비 정하기 대작전", scene_note="예산부터 정하니<br>평화가 왔다 ✍️",
  scene={"type": "chat", "room": "송년회 준비방 (6)", "messages": [
      {"divider": "11월 4일 수요일"},
      {"who": "서진", "text": "회비 5만 원 어때?", "time": "오후 9:02"},
      {"who": "도현", "text": "너무 비싼데ㅠ 3만?", "time": "오후 9:03"},
      {"who": "서진", "text": "그럼 뭐 먹어…", "time": "오후 9:04"},
      {"me": True, "text": "1인 예산부터 정하자 🙏", "time": "오후 9:06", "unread": 5}]},
  bgm={"title": "Feliz Navidad", "artist": "José Feliciano", "year": 1970,
       "reason": "다투기 직전엔<br><em>신나는 캐럴</em>로 분위기 전환."},
  mission={"todo": ["1인당 예산부터 먼저 정하기", "예산 안에서 장소·메뉴 고르기"], "cta": "회비 담당 총무 친구,<br><em>태그해서 응원</em> 👇"},
  merryhood_line="인원 나눠 내기 좋은<br><em>메리후드</em>, 견적은 DM으로 💸",
  caption="D-51 · 송년회 회비로 싸울 뻔 💸\n얼마 걷을지보다 1인당 예산부터 정하면 훨씬 평화로워요.\n회비 총무 친구 태그 👇", tags="#D51 #송년회"),

 dict(date_iso="2026-11-05", dday=50, date="11.05", weekday="목",
  cover="<em>D-50.</em><br>올해 목표 달성률을<br>확인해 봤다.", cover_note="음… 😶",
  scene_title="올해 목표 점검", scene_note="하나는 아직<br>할 수 있다 ✍️",
  scene={"type": "list", "style": "memo", "title": "2026 올해 목표", "items": [
      {"text": "책 12권 읽기", "right": "3권", "strike": True},
      {"text": "매일 아침 일찍 일어나기", "strike": True},
      {"text": "여행 한 번 가기", "right": "완료!"},
      {"text": "외국어 공부", "right": "2주 함", "dim": True},
      {"text": "보고 싶은 사람 다 만나기", "highlight": True}]},
  bgm={"title": "Step Into Christmas", "artist": "Elton John", "year": 1973,
       "reason": "남은 50일,<br><em>가볍게 한 걸음씩.</em>"},
  mission={"todo": ["아직 늦지 않은 목표 하나 골라 보기", "50일 동안 할 만큼만 쪼개기"], "cta": "올해 목표 같이 점검할 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="남은 50일,<br><em>즐거운 연말</em>로 채워요 ✨",
  caption="D-50 · 올해 목표 달성률 확인 😶\n다 못 해도 괜찮아요. 아직 늦지 않은 목표 하나만 골라 봐요.\n목표 같이 점검할 친구 태그 👇", tags="#D50 #올해목표"),
]

out = Path("days"); out.mkdir(exist_ok=True)
for day in W:
    iso = day.pop("date_iso")
    p = out / f"{iso}.json"
    if Path("../posts", iso).exists():
        raise SystemExit(f"{iso} already in posts/, refusing")
    p.write_text(json.dumps(day, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", iso)
