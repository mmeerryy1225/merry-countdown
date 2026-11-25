"""10주차(D-21~D-15) 하루치 데이터 → days/YYYY-MM-DD.json"""
import json
from pathlib import Path

W = [
 dict(date_iso="2026-12-04", dday=21, date="12.04", weekday="금",
  cover="송년회 1차 끝.<br><em>'2차 어디 가?'</em><br>회의만 30분째.", cover_note="길에서 얼어 죽겠어 🥶",
  scene_title="2차 어디 가?", scene_note="다음엔 2차까지<br>미리 정하기 ✍️",
  scene={"type": "chat", "room": "불금 송년회 (5)", "messages": [
      {"divider": "12월 4일 금요일"},
      {"who": "현우", "text": "1차 끝! 2차 어디 감?", "time": "오후 10:02"},
      {"who": "다은", "text": "아무 데나~ 따뜻한 곳", "time": "오후 10:05"},
      {"who": "현우", "text": "아무 데나가 제일 어려움", "time": "오후 10:18"},
      {"who": "다은", "text": "우리 30분째 길에 서 있음", "time": "오후 10:31"},
      {"me": True, "text": "다음엔 2차까지 정하고 만나자 🙏", "time": "오후 10:33", "unread": 4}]},
  bgm={"title": "Step Into Christmas", "artist": "Elton John", "year": 1973,
       "reason": "고민은 그만,<br><em>일단 들어가고 보자</em>는 노래."},
  mission={"todo": ["2차 장소까지 미리 정해 두기", "1차 끝나는 시간도 정해 두기"], "cta": "'아무 데나~' 담당 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="1차부터 2차까지 한 곳에서,<br><em>메리후드</em> 예약은 DM 🎉",
  caption="D-21 · 송년회 2차 어디 가? 🥶\n1차 끝나고 길에서 30분 회의, 다들 한 번쯤 해 봤죠. 2차 장소는 미리 정해 두는 걸로!\n'아무 데나~' 하는 친구 태그 👇", tags="#D21 #송년회"),

 dict(date_iso="2026-12-05", dday=20, date="12.05", weekday="토",
  cover="송년회 시즌 첫 주말.<br>약속이 <em>3개</em> 겹쳤다.", cover_note="몸이 하나라서요 😵",
  scene_title="오늘만 3탕", scene_note="다 같이 한 번에<br>보면 안 될까 ✍️",
  scene={"type": "calendar", "year": 2026, "month": 12, "circle": [5], "cross": [1, 2, 3, 4], "fill": [],
         "labels": {"5": "약속×3😵", "25": "크리스마스🎄"}},
  bgm={"title": "Feliz Navidad", "artist": "José Feliciano", "year": 1970,
       "reason": "여기저기서 들리는<br><em>메리 크리스마스</em>, 오늘은 세 번."},
  mission={"todo": ["겹친 약속 하나로 합치기", "합칠 수 있는 모임끼리 날짜 맞추기"], "cta": "오늘 약속 겹친 친구,<br><em>여기 태그해서 합치기</em> 👇"},
  merryhood_line="겹친 약속 한 번에 모이기,<br><em>메리후드</em>면 다 들어가요 🎄",
  caption="D-20 · 약속 3개 겹친 토요일 😵\n송년회 시즌 첫 주말, 몸은 하나인데 약속은 셋. 합칠 수 있는 건 합쳐 봐요.\n약속 겹친 친구 태그 👇", tags="#D20 #송년회시즌"),

 dict(date_iso="2026-12-06", dday=19, date="12.06", weekday="일",
  cover="어제 송년회 후유증.<br>오늘 <em>해장</em>은<br>뭐로 하지?", cover_note="일단 누워서 생각 🫠",
  scene_title="해장 회의", scene_note="사진은 오늘 안에<br>꼭 올리기 ✍️",
  scene={"type": "chat", "room": "어제 그 멤버 (4)", "messages": [
      {"divider": "12월 6일 일요일"},
      {"who": "지민", "text": "다들 살아 있니…", "time": "오후 12:40"},
      {"who": "태오", "text": "해장 뭐 먹지 국밥? 짬뽕?", "time": "오후 12:52"},
      {"who": "지민", "text": "어제 사진 누가 찍었어?", "time": "오후 1:05"},
      {"me": True, "text": "나! 지금 올릴게 📸", "time": "오후 1:07", "unread": 3}]},
  bgm={"title": "Driving Home for Christmas", "artist": "Chris Rea", "year": 1986,
       "reason": "천천히 집으로 돌아가는<br><em>느긋한 일요일</em> 같은 노래."},
  mission={"todo": ["어제 찍은 사진 단톡방에 공유하기", "해장 메뉴 하나로 통일하기"], "cta": "어제 같이 달린 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="다음 모임은 편하게<br><em>우리끼리 파티</em>로 🎉",
  caption="D-19 · 송년회 다음 날, 해장 회의 🫠\n국밥이냐 짬뽕이냐… 그리고 어제 사진은 꼭 오늘 안에 공유해요.\n어제 같이 달린 친구 태그 👇", tags="#D19 #해장"),

 dict(date_iso="2026-12-07", dday=18, date="12.07", weekday="월",
  cover="회사 송년회 <em>장기자랑</em><br>연습 중.<br>이게 맞나?", cover_note="퇴근하고 싶다 🕺",
  scene_title="장기자랑 연습", scene_note="연습 영상은<br>나만 보기로 ✍️",
  scene={"type": "chat", "style": "work", "room": "송년회 TF (5)", "messages": [
      {"divider": "12월 7일 월요일"},
      {"who": "김 과장", "text": "오늘 6시 회의실 연습 있습니다", "time": "오후 2:10"},
      {"who": "이 대리", "text": "안무 영상 공유드려요 🎬", "time": "오후 2:12"},
      {"who": "김 과장", "text": "다들 동작 외워 오세요~", "time": "오후 2:15"},
      {"me": True, "text": "넵…! (이게 맞나…?)", "time": "오후 2:20", "unread": 4}]},
  bgm={"title": "Merry Christmas Everyone", "artist": "Shakin' Stevens", "year": 1985,
       "reason": "어색해도 다 같이 흔들면<br><em>그게 연말</em>이죠."},
  mission={"todo": ["연습 영상은 혼자만 간직하기", "끝나고 나한테 줄 보상 정하기"], "cta": "장기자랑 끌려간 동료,<br><em>여기 태그해서 응원</em> 👇"},
  merryhood_line="진짜 즐거운 연말은<br><em>편한 사람들</em>이랑 ✨",
  caption="D-18 · 송년회 장기자랑 연습 중 🕺\n이게 맞나 싶지만 일단 외우는 중… 연습 영상은 나만 보는 걸로.\n같이 끌려간 동료 태그 👇", tags="#D18 #장기자랑"),

 dict(date_iso="2026-12-08", dday=17, date="12.08", weekday="화",
  cover="<em>시크릿 산타</em> 선물,<br>아직 못 샀다.", cover_note="교환은 금요일인데 😰",
  scene_title="장바구니만 가득", scene_note="오늘 안에<br>결제한다 ✍️",
  scene={"type": "list", "style": "cart", "title": "장바구니 (5)", "items": [
      {"text": "향초 세트 🕯", "right": "고민 중…"},
      {"text": "핸드크림 3종", "right": "고민 중…"},
      {"text": "머그컵 ☕", "right": "고민 중…"},
      {"text": "수면 양말 🧦", "right": "고민 중…"},
      {"text": "시크릿 산타 선물 🎁", "right": "오늘 결제!", "highlight": True}]},
  bgm={"title": "Santa Tell Me", "artist": "Ariana Grande", "year": 2014,
       "reason": "산타한테 묻고 싶다,<br><em>뭘 사야 좋아할지.</em>"},
  mission={"todo": ["오늘 안에 주문 완료하기", "도착 날짜 꼭 확인하기"], "cta": "시크릿 산타 같이 하는 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="선물 교환은<br><em>파티룸</em>에서 두 배로 🎁",
  caption="D-17 · 시크릿 산타 선물, 아직 0개 🎁\n장바구니에만 5개째… 오늘 안에 결제하고 도착 날짜까지 확인해요.\n시크릿 산타 같이 하는 친구 태그 👇", tags="#D17 #시크릿산타"),

 dict(date_iso="2026-12-09", dday=16, date="12.09", weekday="수",
  cover="총무가 송년회<br><em>정산 엑셀</em>을 만들었다.<br>입금 안 한 사람 누구?", cover_note="총무는 다 보고 있다 👀",
  scene_title="정산의 시간", scene_note="조용히 태그만<br>했을 뿐 ✍️",
  scene={"type": "chat", "room": "송년회 정산방 (6)", "messages": [
      {"divider": "12월 9일 수요일"},
      {"who": "총무 서윤", "text": "📎 송년회 정산.xlsx", "time": "오후 6:30"},
      {"who": "총무 서윤", "text": "1인 32,000원! 오늘까지 부탁해", "time": "오후 6:31"},
      {"who": "도현", "text": "입금 완료 🙋", "time": "오후 6:40"},
      {"me": True, "text": "나도 입금했어!", "time": "오후 6:42", "unread": 4},
      {"me": True, "text": "@준호 @하린 확인 부탁 🙏", "time": "오후 6:43", "unread": 4}]},
  bgm={"title": "Thank God It's Christmas", "artist": "Queen", "year": 1984,
       "reason": "정산 끝나면<br><em>진짜 크리스마스</em> 기분 날 듯."},
  mission={"todo": ["정산 미입금자 조용히 태그하기", "총무한테 고맙다고 한마디"], "cta": "우리 모임 총무,<br><em>여기 태그해서 감사 인사</em> 👇"},
  merryhood_line="정산 깔끔한 연말 파티,<br><em>다음 모임</em>도 여기서 🎉",
  caption="D-16 · 정산 엑셀 등장 👀\n총무는 다 보고 있어요. 미입금자는 오늘 안에 조용히 입금하는 걸로!\n고생한 총무 태그해서 감사 인사 👇", tags="#D16 #정산"),

 dict(date_iso="2026-12-10", dday=15, date="12.10", weekday="목",
  cover="크리스마스 레스토랑<br>예약이 <em>전부 마감</em>됐다.", cover_note="다들 언제 예약한 거야 😱",
  scene_title="24·25일 마감", scene_note="플랜 B는<br>우리끼리 파티 ✍️",
  scene={"type": "calendar", "year": 2026, "month": 12, "circle": [], "cross": [24, 25], "fill": [10],
         "labels": {"10": "오늘", "24": "마감", "25": "마감"}},
  bgm={"title": "It's Beginning to Look a Lot Like Christmas", "artist": "Michael Bublé", "year": 2011,
       "reason": "예약은 마감이어도<br><em>크리스마스 느낌</em>은 계속."},
  mission={"todo": ["우리끼리 파티 플랜 B 세우기", "같이 보낼 사람한테 오늘 연락하기"], "cta": "레스토랑 예약 실패한 친구,<br><em>여기 태그</em> 👇"},
  merryhood_line="레스토랑 마감이라면<br><em>메리후드</em> 날짜 DM으로 문의 📅",
  caption="D-15 · 크리스마스 레스토랑, 전부 마감 😱\n그렇다면 플랜 B! 우리끼리 파티도 충분히 크리스마스예요.\n예약 실패한 친구 태그 👇", tags="#D15 #크리스마스예약"),
]

out = Path("days"); out.mkdir(exist_ok=True)
for day in W:
    iso = day.pop("date_iso")
    p = out / f"{iso}.json"
    if (Path("..") / "posts" / iso).exists():
        raise SystemExit(f"posts/{iso} already exists")
    p.write_text(json.dumps(day, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", iso)
