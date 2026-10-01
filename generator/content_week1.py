"""1주차(D-84~D-78) 하루치 데이터 → days/YYYY-MM-DD.json"""
import json
from pathlib import Path

W = [
 dict(date_iso="2026-10-02", dday=84, date="10.02", weekday="금",
  cover="크리스마스까지 <em>84일</em> 남았다는 걸<br>방금 알았다.", cover_note="올해 벌써 이렇게 됐다고? 😮",
  scene_title="벌써 여기까지 옴", scene_note="84일… 생각보다<br>금방이다 ✍️",
  scene={"type": "calendar", "year": 2026, "month": 12, "circle": [25], "labels": {"25": "크리스마스🎄"}, "fill": [24]},
  bgm={"title": "It's Beginning to Look a Lot Like Christmas", "artist": "Michael Bublé", "year": 2011,
       "reason": "거리엔 아직 단풍인데,<br>마음은 벌써 <em>크리스마스 같아지는 중.</em>"},
  mission={"todo": ["크리스마스 카운트다운 시작하기", "같이 셀 친구 한 명 찾기"], "cta": "오늘부터 매일 하나씩,<br><em>D-DAY까지 같이 세요</em> 👇"},
  merryhood_line="84일 뒤 크리스마스,<br><em>어디서</em> 보낼지 미리 찜! 🎄",
  caption="크리스마스까지 D-84 🎄\n오늘부터 매일 하나씩, 연말 공감 카드로 같이 카운트다운해요.\n같이 셀 친구 태그 👇", tags="#D84"),

 dict(date_iso="2026-10-03", dday=83, date="10.03", weekday="토",
  cover="연휴 첫날.<br>계획은 많았는데<br>눈 떠 보니 <em>오후 2시.</em>", cover_note="그래도 연휴는 3일이니까 🙃",
  scene_title="알람 5개의 행방", scene_note="다 끄고 잤다고<br>한다 ✍️",
  scene={"type": "list", "style": "alarm", "title": "알람", "sub": "10월 3일 토요일", "items": [
      {"text": "오전 8:00 · 운동 가기 💪", "off": True}, {"text": "오전 8:10 · 진짜 일어나기", "off": True},
      {"text": "오전 9:30 · 브런치 약속?", "off": True}, {"text": "오전 11:00 · 최후의 알람", "off": True},
      {"text": "오후 2:04 · 자연 기상 ☀️"}]},
  bgm={"title": "Cozy Little Christmas", "artist": "Katy Perry", "year": 2018,
       "reason": "오늘은 그냥 이불 속이<br><em>제일 아늑한 날</em>이니까."},
  mission={"todo": ["연휴에 할 일 딱 1개만 정하기", "같이 할 친구한테 연락하기"], "cta": "아직 침대에 있는 친구,<br><em>댓글로 깨워 주세요</em> 👇"},
  merryhood_line="남은 연휴는<br><em>친구들이랑</em> 꽉 채워요 🎉",
  caption="D-83 · 연휴 첫날 🛌\n알람 5개 끄고 일어나니 오후 2시… 나만 그런 거 아니죠?\n아직 침대에 있는 친구 태그 👇", tags="#D83 #연휴"),

 dict(date_iso="2026-10-04", dday=82, date="10.04", weekday="일",
  cover="사진첩을 넘기다 깨달았다.<br>올해 친구들이랑 찍은 사진이<br><em>거의 없다.</em>", cover_note="음식 사진만 300장 🍜",
  scene_title="올해 내 사진첩", scene_note="친구 사진은<br>단 한 장 ✍️",
  scene={"type": "photo", "style": "album", "title": "2026 사진첩", "photos": [
      {"emoji": "🍜", "bg": "#ffe2c4"}, {"emoji": "☕", "bg": "#e8dccb"}, {"emoji": "🍰", "bg": "#ffd6e5"},
      {"emoji": "🌅", "bg": "#ffd9a8"}, {"emoji": "👯", "bg": "#d6f5b0", "highlight": True, "caption": "친구랑 (1장)"}, {"emoji": "🐈", "bg": "#dfe7ee"},
      {"emoji": "🍣", "bg": "#ffe0d6"}, {"emoji": "☕", "bg": "#e8dccb"}, {"emoji": "🍜", "bg": "#ffe2c4"}]},
  bgm={"title": "The Christmas Song", "artist": "Nat King Cole", "year": 1946,
       "reason": "따뜻한 노래 들으면서<br><em>보고 싶은 얼굴</em> 떠올려 보기."},
  mission={"todo": ["오랜만인 친구한테 안부 DM 보내기", "같이 사진 찍을 날 정하기"], "cta": "올해 사진 같이 못 찍은 친구,<br><em>여기 태그해요</em> 👇"},
  merryhood_line="올해 남은 사진은<br><em>다 같이</em> 찍어요 📸",
  caption="D-82 · 사진첩 정리하다가 📸\n음식 사진은 300장인데 친구랑 찍은 건 1장…\n올해 사진 같이 못 찍은 친구 태그 👇", tags="#D82 #사진첩"),

 dict(date_iso="2026-10-05", dday=81, date="10.05", weekday="월",
  cover="아직 <em>반팔</em> 입고 다니는데<br>마음은 이미 연말이다.", cover_note="날씨야 뭐 해? 🙄",
  scene_title="오늘 날씨 실화?", scene_note="근데 플레이리스트는<br>벌써 캐럴 ✍️",
  scene={"type": "weather", "place": "서울 마포구", "now": "24°", "icon": "☀️", "desc": "맑음", "hi": "26°", "lo": "15°",
         "hourly": [["9시", "17°", "🌤"], ["12시", "23°", "☀️"], ["15시", "26°", "☀️"], ["18시", "21°", "🌤"], ["21시", "17°", "🌙"]],
         "alert": "일교차 주의 · 마음속 기온은 이미 영하"},
  bgm={"title": "Let It Snow! Let It Snow! Let It Snow!", "artist": "Dean Martin", "year": 1959,
       "reason": "눈은 아직이지만<br><em>노래로 먼저</em> 내리게 하기."},
  mission={"todo": ["올해 연말 위시 하나 적기", "댓글로 공유하기"], "cta": "올해 연말에 꼭 하고 싶은 거,<br><em>댓글로 남겨 주세요</em> 👇"},
  merryhood_line="연말 위시리스트에<br><em>파티 하나</em> 추가해요 🎄",
  caption="D-81 · 낮엔 반팔, 마음은 12월 ☀️🎄\n여러분의 올해 연말 위시는 뭐예요? 댓글로 남겨 주세요 👇", tags="#D81 #가을날씨"),

 dict(date_iso="2026-10-06", dday=80, date="10.06", weekday="화",
  cover="1월에 써 둔<br>'<em>올해 목표</em>' 메모를<br>다시 열어 봤다.", cover_note="...조용히 닫았다 🫠",
  scene_title="1월의 나에게", scene_note="마지막 하나는<br>지킬 수 있다 ✍️",
  scene={"type": "list", "style": "memo", "title": "2026 올해 목표", "sub": "1월 1일 작성", "items": [
      {"text": "운동 주 3회 💪", "strike": True}, {"text": "영어 공부 매일 30분", "strike": True},
      {"text": "한 달에 책 2권 📚", "strike": True}, {"text": "저축 열심히 하기", "right": "...?"},
      {"text": "연말엔 다 같이 파티하기 🎉", "highlight": True}]},
  bgm={"title": "Step Into Christmas", "artist": "Elton John", "year": 1973,
       "reason": "목표는 몰라도<br>크리스마스엔 <em>한 발짝씩 다가가는 중.</em>"},
  mission={"todo": ["올해 목표 하나만 다시 시작하기", "나머지는 내년의 나에게 넘기기"], "cta": "목표 메모 아직 안 열어 본 친구,<br><em>태그해서 같이 반성해요</em> 👇"},
  merryhood_line="목표 하나는 꼭 지키자,<br><em>연말 파티</em>는 여기서 🎉",
  caption="D-80 · 1월의 내가 쓴 목표 📝\n하나씩 지워지는 중… 마지막 하나는 꼭 지켜요.\n같이 반성할 친구 태그 👇", tags="#D80 #올해목표"),

 dict(date_iso="2026-10-07", dday=79, date="10.07", weekday="수",
  cover="퇴근길 카페에<br>벌써 <em>겨울 시즌 메뉴</em><br>포스터가 붙었다.", cover_note="아직 10월인데요? ☕",
  scene_title="벌써 그 시즌?", scene_note="결국 다 같이<br>마시러 간다 ✍️",
  scene={"type": "chat", "room": "퇴근 메이트 (4)", "messages": [
      {"divider": "10월 7일 수요일"},
      {"who": "민지", "text": "카페에 벌써 겨울 메뉴 나옴 ㄷㄷ", "time": "오후 6:41"},
      {"who": "준호", "text": "아직 10월인데;;", "time": "오후 6:42"},
      {"who": "서연", "text": "근데 맛있어 보이는 건 인정", "time": "오후 6:42"},
      {"who": "민지", "text": "내일 같이 마시러 갈 사람?", "time": "오후 6:43"},
      {"me": True, "text": "나 나 나 🙋", "time": "오후 6:43", "unread": 1}]},
  bgm={"title": "A Holly Jolly Christmas", "artist": "Burl Ives", "year": 1964,
       "reason": "가볍게 흥얼거리기 좋은,<br><em>시즌 메뉴 같은</em> 노래."},
  mission={"todo": ["올겨울 첫 시즌 메뉴 마셔 보기", "같이 갈 친구 정하기"], "cta": "시즌 메뉴 같이 마실 친구,<br><em>댓글에 소환</em> 👇"},
  merryhood_line="따뜻한 음료 들고<br><em>연말 수다</em>는 여기서 ☕",
  caption="D-79 · 벌써 겨울 시즌 메뉴? ☕\n10월인데 마음이 급해지는 건 저만 그런가요.\n같이 마시러 갈 친구 태그 👇", tags="#D79 #시즌메뉴"),

 dict(date_iso="2026-10-08", dday=78, date="10.08", weekday="목",
  cover="남은 <em>연차</em>를 세어 봤다.<br>생각보다 많고,<br>쓸 날은 생각보다 없다.", cover_note="다 쓰고 갈 수 있을까 🤔",
  scene_title="내 연차 현황", scene_note="일단 크리스마스부터<br>찜해 둠 ✍️",
  scene={"type": "list", "style": "memo", "title": "남은 연차 계산", "sub": "10월 8일 기준", "items": [
      {"text": "남은 연차", "right": "7일"}, {"text": "10월에 쓸 날", "right": "0일"},
      {"text": "11월에 쓸 날", "right": "글쎄…"}, {"text": "12월 마감 시즌", "right": "😇"},
      {"text": "크리스마스 연차 찜 🎄", "right": "1일 ✅", "highlight": True}]},
  bgm={"title": "Driving Home for Christmas", "artist": "Chris Rea", "year": 1986,
       "reason": "연차 붙여서<br><em>어디론가 떠나는 상상</em> 중."},
  mission={"todo": ["남은 연차 크리스마스 근처에 찜하기", "같이 쉴 친구랑 날짜 맞추기"], "cta": "연차 아직 못 쓴 친구,<br><em>태그해서 같이 맞춰요</em> 👇"},
  merryhood_line="연차 쓴 날엔<br><em>파티룸</em>에서 하루 종일 🎉",
  caption="D-78 · 남은 연차 계산 중 🗓\n일단 크리스마스 근처부터 찜해 두기로.\n연차 같이 맞출 친구 태그 👇", tags="#D78 #연차"),
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
