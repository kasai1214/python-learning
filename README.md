# 自己学習 Python マップピン出力システム

ダウンロードした日本郵便の東京都の郵便番号が格納された CSV データから地図にマップピンを表示する Python システムです。


## 動作の流れ

- pandas で CSV データの読み取り
- zipcloud で郵便番号から住所へ変更
- 国土地理院住所検索APIで住所を経緯度に変更、folium への情報引き渡し
  -  住所文字列を渡すと `[経度, 緯度]` 形式で座標が返されます
  - folium で地図にマーカーを置くために `[緯度, 経度]` の順に変換しています
- folium で地図とマップピンの生成
- 最後にこの地図を HTML 形式で保存


## ファイル構成

- `index.html` : 軽量版地図 (トップページ用、マップピン7個のみ) 
- `map_full.html` : 完全版地図 (全データ表示)
- `経緯度マップピン.py` : 地図生成用 Python コード
- `csv版/13TOKYO.CSV` : 元データ CSV ファイル


## 結果確認

1. 軽量版地図は GitHub Pages トップページで表示されます：
   [軽量版地図](https://kasai1214.github.io/python-learning/)

2. 完全版地図は以下からアクセス (読み込みに非常に時間がかかります) :
   [完全版地図](https://kasai1214.github.io/python-learning/map_full.html)
