import requests
import urllib
import folium
import pandas as pd


# ファイル読み込み
df = pd.read_csv('13TOKYO.CSV',encoding="shift_jis",header=None)

# 国土地理院API
makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="

# 郵便番号検索APIのURL
URL = 'https://zipcloud.ibsnet.co.jp/api/search'

# 郵便番号3列目をcsvから取得
postal_codes = df[2]

# drop_duplicatesで重複削除、reset_indexで行番号を降り直し
postal_codes_list = postal_codes.drop_duplicates().reset_index(drop=True)

print(postal_codes_list)
count = 0
firstcode = postal_codes_list[0]

# 一行目から地図の初期値を作成
# zipcloudで郵便番号を住所に
f_res = requests.get(URL, params={'zipcode': firstcode},timeout=10)
f_data = f_res.json()
# 検索に使う部分を抽出 (resultsが正しく現れてるかの確認のif)
if f_data["results"]:
        f_result = f_data["results"][0]
        f_address = f_result["address1"] + f_result["address2"] + f_result["address3"]

# urllib.parse.quoteで文字をURLエンコード
s_quote = urllib.parse.quote(f_address)
# URLを完成させてrequestsでhttpリクエストを送り、その結果responseに格納
f_response = requests.get(makeUrl + s_quote)
print(f'{count} "{firstcode}" "{f_address}" {f_response.json()[0]["geometry"]["coordinates"]}')
# リストのままだと2重で囲ってることになってたらしいから一旦変数変えて解決
lal = f_response.json()[0]["geometry"]["coordinates"][::-1]
# 地図を作成するためのライブラリ folium
map = folium.Map(location=f_response.json()[0]["geometry"]["coordinates"][::-1], zoom_start=10)
# マップピン
folium.Marker(location=lal,popup=s_quote).add_to(map)


# 2個目以降の書き込み
for code in postal_codes_list[1:]:
    try:
        # zipcloudで郵便番号を住所に
        res = requests.get(URL, params={'zipcode': code},timeout=10)
        data = res.json()
        # 検索に使う部分を抽出
        if data["results"]:
            result = data["results"][0]
            address = result["address1"] + result["address2"] + result["address3"]
        else:
                print(f"{code} の結果がありません")
                continue
            
        # urllib.parse.quoteで文字をURLエンコード
        s_quote = urllib.parse.quote(address)
        # URLを完成させてrequestsでhttpリクエストを送り、その結果をresponseに格納
        response = requests.get(makeUrl + s_quote)
        print(f'{count+1} "{code}" "{address}" {response.json()[0]["geometry"]["coordinates"]}')
        # リストのままだと2重で囲ってることになってたらしいから一旦変数に変えて解決
        lal = response.json()[0]["geometry"]["coordinates"][::-1]
        # マップピン
        folium.Marker(location=lal,popup=s_quote).add_to(map)
        count += 1
    except requests.exceptions.Timeout:
        print(f"タイムアウト: {code}")
        continue
    except requests.exceptions.RequestException as e:
        print(f"通信エラー: {e}")
        continue
    except Exception as e:
        print(f"その他エラー: {e}")
        continue
        

map.save("map.html")
