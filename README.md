# 教習自動予約システム

とある自動車学校の教習自動予約システムにて自動予約をするためのプログラムです。

## 必要条件
1. Python 3.9.17 以上をインストールする
1. `$ pip install -r requirements.txt` を実行する
1. 適切なバージョンのchromedriver.exeを任意のディレクトリに配置する
1. .envファイルに以下の情報を記載する

     - OBICNET_URL: 教習自動予約システムのURL
     - CHROMEDRIVER_PATH: chromedriver.exeのパス
     - STUDENT_ID: 教習生番号
     - PASSWORD: パスワード

