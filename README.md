# 自己学習 Python マップピン出力システム

ダウンロードした日本郵便の東京都の郵便番号が格納されたCSVデータから地図にマップピンを表示するPythonシステムです。


## 動作の流れ

- pandasでCSVデータの読み取り
- zipcloudで郵便番号から住所へ変更
- 国土地理院住所検索APIで住所を経緯度に変更、foliumへの情報引き渡し
  -  住所文字列を渡すと `[経度, 緯度]` 形式で座標が返されます
  - foliumで地図にマーカーを置くために `[緯度, 経度]` の順に変換しています
- foliumで地図とマップピンの生成
- 最後にこの地図をHTML形式で保存


## ファイル構成

- `index.html` : 軽量版地図（トップページ）
- `map_full.html` : 全データ表示版フル地図
- `経緯度マップピン.py` : 地図生成用 Python コード
- `csv版/13TOKYO.CSV` : 元データ CSV ファイル


## 結果確認

1. 軽量版地図は GitHub Pages トップページで表示されます：
   [軽量版地図](https://kasai1214.github.io/python-learning/)

2. フル地図は以下からアクセス (読み込みに非常に時間がかかります) :
   [フル地図](https://kasai1214.github.io/python-learning/map_full.html)
