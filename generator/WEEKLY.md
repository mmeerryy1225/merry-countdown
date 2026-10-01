# 매주 카드 제작 절차 (수요일 예약 작업용)

크리스마스 카운트다운(@m.eeeeeeeerry) 다음 주 7일치 카드를 만들어 `posts/`에 올리는 절차.
게시는 `.github/workflows/publish.yml`이 매일 09:50 KST에 자동으로 한다. 이 절차는 **카드 제작만** 한다.

## 0. 범위 정하기
- `posts/` 안 가장 마지막 날짜 폴더의 **다음 날부터 7일**을 만든다. (12/25 이후는 만들지 않는다)
- 이미 `posts/`에 있는 날짜는 절대 덮어쓰지 않는다. 특히 `.posted` 파일이 있는 폴더는 건드리지 않는다.

## 1. 내용 쓰기 → `generator/days/YYYY-MM-DD.json`
- 날짜별 원본은 `generator/calendar.csv` 한 줄: situation(표지 공감 상황), scene(장면 형식), bgm_title/artist/year, mission, merryhood_level(강/중/약).
- 형식과 말투는 `generator/content_week2.py`를 그대로 따라 한다 (새 주차는 `content_weekN.py`로 만들어 실행해도 됨).
- 필드: dday, date("10.16"), weekday, cover, cover_note, scene_title(9자 이하), scene_note, scene, bgm{title,artist,year,reason}, mission{todo[2], cta}, merryhood_line, caption, tags("#D70 #키워드").
- scene 종류와 csv의 장면 형식 매핑:
  - 단톡방 → `{"type":"chat", ...}` / 메신저(회사) → chat + `"style":"work"` (메시지 5~6개 이하, 길면 아래 메모를 가림)
  - 캘린더·예약 화면 → `{"type":"calendar","year","month","circle":[],"cross":[],"fill":[],"labels":{}}`
  - 메모장/체크리스트/검색 기록/알람 기록/장바구니/플레이리스트/투표 → `{"type":"list","style":"memo|checklist|search|alarm|cart|playlist|vote", "title", "sub", "items":[...]}` (항목 5개)
  - 사진 → `{"type":"photo","photos":[2개]}` / 사진첩 → photo + `"style":"album"` (9칸)
  - 날씨 앱 → `{"type":"weather", ...}`
- `<em>강조</em>`, `<br>`만 HTML 허용.
- merryhood_level: 강 = 마지막 카드 문구에서 장소·예약을 직접 언급 / 약 = 분위기만 가볍게.

## 2. 지켜야 할 것
- **가사 금지.** 곡 제목·아티스트·연도만. csv의 BGM을 그대로 쓰고, 다른 곡으로 바꾸지 않는다.
- 다이어트·체중, 특정 실존 인물·브랜드 비방, 특정 메신저 앱 브랜드 흉내 금지.
- 실제 날짜와 요일이 맞는지 확인 (요일은 csv weekday 기준).

## 3. 렌더링 → 확인 → 내보내기
```bash
cd generator
python batch.py 2026-10-16 2026-10-22      # out/날짜/01~05.png + caption.txt + preview.png
python export_posts.py 2026-10-16 2026-10-22  # ../posts/날짜/ 로 jpg·caption·meta 복사
```
- **반드시 7일치 02.png(공감 장면)와 01.png를 눈으로 확인**: 글자가 패널 밖으로 넘치거나 아래 손메모·하단 핸들을 가리면 내용을 줄이고 다시 렌더링.

## 4. 저장소에 올리기
- 커밋 메시지: `N주차 카드 추가 (MM/DD~MM/DD, D-xx~D-yy)`
- `generator/days/*.json`, 새 `content_weekN.py`, `posts/날짜/`를 함께 커밋 후 main에 push.

## 5. 사용자에게 보고
- 7일 × 5장을 한 장으로 모은 미리보기(세로줄 = 하루) 이미지를 보내고,
- 날짜별 공감 상황과 BGM 한 줄 요약, "고칠 날이 있으면 말씀해 주세요"로 마무리.
- 사용자는 매일 게시 후 스토리에 BGM 음악을 직접 붙인다 (캡션의 🎧 줄 참고).
