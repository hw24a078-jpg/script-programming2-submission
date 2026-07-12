import os
from pathlib import Path

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://dench.mklab.osakac.ac.jp/script-pg/"
cache_file = Path("last_script_03.txt")

try:
    response = requests.get(url, verify=False, timeout=15)
    response.raise_for_status()
    current_content = response.text.strip()
except requests.exceptions.RequestException as e:
    print(f"通信エラー: {e}")
    raise SystemExit(1)

if not os.path.exists(cache_file):
    cache_file.write_text(current_content, encoding="utf-8")
    print("初回取得完了（差分なし）")
else:
    previous_content = cache_file.read_text(encoding="utf-8").strip()

    if current_content != previous_content:
        print("更新が検出されました！")
        print("前回:", previous_content)
        print("今回:", current_content)
        cache_file.write_text(current_content, encoding="utf-8")
    else:
        print("変更はありません。")
