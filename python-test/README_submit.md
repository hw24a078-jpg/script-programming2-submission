# スクリプトプログラミング演習2 提出まとめ

## 内容

- `01.py`: 気象庁 CSV (`kobe.csv`) を pandas で読み込み、matplotlib で平均気温グラフを `temperature.png` に出力する。
- `02.py`: 同じデータを Plotly でインタラクティブ HTML (`temperature.html`) に出力する。
- `web_scraping.py`: 授業資料 07 の URL を取得し、前回取得内容との差分を `last_script_03.txt` で判定する。
- `Jenkinsfile`: 3本のプログラムをステージごとに実行し、成果物を保存する Pipeline 定義。
- `jenkins_python_tasks.sh`: Jenkins のフリースタイルジョブから3本を一括実行するスクリプト。
- `requirements.txt`: 必要ライブラリ一覧。

## 実行方法

```bash
cd python-test
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 01.py
python3 02.py
python3 web_scraping.py
```

## Jenkins Pipeline で実行する場合（推奨）

1. 新規ジョブで「Pipeline」を選ぶ。
2. Definition を「Pipeline script from SCM」にする。
3. Script Path に `Jenkinsfile` を指定する。
4. 「ビルド実行」を押す。

リポジトリのルートがこの課題フォルダで、`python-test` がその中にある場合は、
Script Path を `python-test/Jenkinsfile` にする。収録済みのJenkinsfileが実行フォルダを
自動判定するため、ZIP展開直下とリポジトリ直下のどちらでも利用できる。

実行後、Jenkins のビルド画面に次の成果物が保存される。

- `temperature.png`
- `temperature.html`
- `last_script_03.txt`

## Jenkins フリースタイルジョブで実行する場合

「ビルド手順を追加」→「シェルの実行」に次を設定する。

```bash
chmod +x jenkins_python_tasks.sh
./jenkins_python_tasks.sh
```

続いて「ビルド後の処理」→「成果物を保存」で、次を指定する。

```text
temperature.png,temperature.html,last_script_03.txt
```

既存の `venv` と分けるため、Pipeline は `.venv-jenkins`、一括実行スクリプトは
標準で `.venv-submit` を使う。

## 出力物

- `temperature.png`
- `temperature.html`
- `last_script_03.txt`
- `run_log.txt`
