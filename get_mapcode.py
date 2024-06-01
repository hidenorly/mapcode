import requests
import sys

def get_mapcode(latitude, longitude):
    # ポストするデータを準備
    data = {
        "t": "jpndeg",
        "jpn_lat": str(latitude),
        "jpn_lon": str(longitude)
    }
    
    # リクエストを送信
    response = requests.post("https://saibara.sakura.ne.jp/map/convgeo.cgi", data=data)
    
    # レスポンスからMapcodeを抽出
    mapcode = response.text.split('name="mapcode" value="')[1].split('"')[0]
    
    return mapcode

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 get_mapcode.py latitude longitude")
        sys.exit(1)
    
    latitude = float(sys.argv[1])
    longitude = float(sys.argv[2])
    
    mapcode = get_mapcode(latitude, longitude)
    print("Mapcode:", mapcode)
