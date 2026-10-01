"""오늘 날짜(KST)의 카드뉴스를 인스타그램에 캐러셀로 게시한다.

posts/YYYY-MM-DD/ 폴더 구성:
  01.jpg ~ 05.jpg   카드 (05 = 메리후드 카드, 항상 마지막)
  caption.txt       캡션 전문
  meta.json         {"tag_username": "mmeerryy_hood", "tag_x": 0.364, "tag_y": 0.864}
  .posted           게시 완료 표시 (중복 게시 방지, 자동 생성)

환경 변수:
  IG_ACCESS_TOKEN   인스타그램 액세스 토큰 (GitHub Secret)
  IMAGE_BASE_URL    이미지 공개 주소 앞부분 (예: https://raw.githubusercontent.com/<owner>/<repo>/main/posts)
  POST_DATE         (선택) 특정 날짜 강제 지정 YYYY-MM-DD
  DRY_RUN           (선택) "1"이면 실제 게시 없이 점검만
"""
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path

import requests

API = "https://graph.instagram.com/v22.0"
KST = dt.timezone(dt.timedelta(hours=9))


def call(method, path, **params):
    r = requests.request(method, f"{API}/{path}", params=params, timeout=60)
    data = r.json()
    if r.status_code >= 400 or "error" in data:
        raise RuntimeError(f"{method} {path} 실패: {data}")
    return data


def wait_ready(container_id, token, tries=30):
    for _ in range(tries):
        st = call("GET", container_id, fields="status_code", access_token=token)["status_code"]
        if st == "FINISHED":
            return
        if st in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"컨테이너 {container_id} 상태: {st}")
        time.sleep(5)
    raise RuntimeError(f"컨테이너 {container_id} 준비 시간 초과")


def main():
    token = os.environ["IG_ACCESS_TOKEN"]
    base = os.environ["IMAGE_BASE_URL"].rstrip("/")
    day = os.environ.get("POST_DATE") or dt.datetime.now(KST).date().isoformat()
    dry = os.environ.get("DRY_RUN") == "1"

    folder = Path("posts") / day
    if not folder.exists():
        print(f"[{day}] 게시할 폴더가 없습니다. 건너뜀.")
        return
    if (folder / ".posted").exists():
        print(f"[{day}] 이미 게시됨. 건너뜀.")
        return

    images = sorted(folder.glob("0[1-9].jpg"))
    caption = (folder / "caption.txt").read_text(encoding="utf-8")
    meta = json.loads((folder / "meta.json").read_text(encoding="utf-8"))
    if not 2 <= len(images) <= 10:
        sys.exit(f"이미지 개수 오류: {len(images)}장")

    me = call("GET", "me", fields="user_id,username", access_token=token)
    ig_id = me["user_id"]
    print(f"[{day}] 계정 @{me['username']} · 이미지 {len(images)}장")
    if dry:
        for im in images:
            print("  ", f"{base}/{day}/{im.name}")
        print("DRY_RUN: 여기서 멈춤")
        return

    # 1) 이미지별 캐러셀 아이템 컨테이너 (마지막 장에 메리후드 사진 태그)
    children = []
    for i, im in enumerate(images):
        params = dict(image_url=f"{base}/{day}/{im.name}", is_carousel_item="true", access_token=token)
        if i == len(images) - 1 and meta.get("tag_username"):
            params["user_tags"] = json.dumps([{"username": meta["tag_username"], "x": meta["tag_x"], "y": meta["tag_y"]}])
        try:
            cid = call("POST", f"{ig_id}/media", **params)["id"]
        except RuntimeError as e:
            if "user_tags" not in params:
                raise
            print("  사진 태그 실패 → 태그 없이 재시도:", e)
            params.pop("user_tags")
            cid = call("POST", f"{ig_id}/media", **params)["id"]
        children.append(cid)
        print(f"  아이템 {im.name} → {cid}")
    for cid in children:
        wait_ready(cid, token)

    # 2) 캐러셀 컨테이너
    carousel = call("POST", f"{ig_id}/media", media_type="CAROUSEL", children=",".join(children),
                    caption=caption, access_token=token)["id"]
    wait_ready(carousel, token)

    # 3) 게시
    media_id = call("POST", f"{ig_id}/media_publish", creation_id=carousel, access_token=token)["id"]
    link = call("GET", media_id, fields="permalink", access_token=token).get("permalink", "")
    print(f"[{day}] 게시 완료 ✅ {link}")
    (folder / ".posted").write_text(f"{media_id}\n{link}\n", encoding="utf-8")

    # 토큰 유효기간 연장 (60일 → 오늘부터 다시 60일)
    try:
        r = call("GET", "refresh_access_token", grant_type="ig_refresh_token", access_token=token)
        print(f"토큰 연장 완료 · 남은 기간 약 {int(r.get('expires_in', 0)) // 86400}일")
    except RuntimeError as e:
        print("토큰 연장 실패(게시에는 영향 없음):", e)


if __name__ == "__main__":
    main()
