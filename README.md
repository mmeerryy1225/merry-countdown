# merry-countdown 🎄

@m.eeeeeeeerry 크리스마스 카운트다운 카드뉴스 자동 게시

- `posts/YYYY-MM-DD/` : 그날 카드 01~05.jpg, caption.txt, meta.json
- 매일 09:50 KST(GitHub 지연 감안 ≈10시) `publish.py`가 그날 폴더를 인스타그램 캐러셀로 게시
- 수동 실행: Actions → "크리스마스 카운트다운 자동 게시" → Run workflow (dry_run=1 이면 점검만)
- 토큰: Settings → Secrets → `IG_ACCESS_TOKEN`
