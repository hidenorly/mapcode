#   Copyright 2024 hidenorly
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


import requests
import sys

def get_mapcode(latitude, longitude):
    data = {
        "t": "jpndeg",
        "jpn_lat": str(latitude),
        "jpn_lon": str(longitude)
    }

    # Thank you so much for hosting this web service
    response = requests.post("https://saibara.sakura.ne.jp/map/convgeo.cgi", data=data)
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
