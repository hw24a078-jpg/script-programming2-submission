import os
import requests            # Webサイトへのリクエスト（アクセス）を行うためのライブラリ
import urllib3             # HTTP通信を制御する低レベルライブラリ（requestsの下層で使われる）

# 自己署名証明書による警告を表示させないようにする設定
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# チェック対象のURL（更新を監視したいWebページ）
url = "https://dench.mklab.osakac.ac.jp/script-pg/"

# 前回取得したページの内容を保存するためのファイル名
cache_file = "last_script_03.txt"

try:
    # 証明書の検証を無効にしてWebページを取得（自己署名証明書に対応するため）
    response = requests.get(url, verify=False)
    response.raise_for_status()
    current_content = response.text.strip()
except requests.exceptions.RequestException as e:
    print(f"通信エラー: {e}")
    exit(1)

if not os.path.exists(cache_file):
    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(current_content)
    print("初回取得完了（差分なし）")
else:
    with open(cache_file, "r", encoding="utf-8") as f:
        previous_content = f.read().strip()

    if current_content != previous_content:
        print("更新が検出されました！")
        print("前回:", previous_content)
        print("今回:", current_content)
        with open(cache_file, "w", encoding="utf-8") as f:
            f.write(current_content)
    else:
        print("変更はありません。")
