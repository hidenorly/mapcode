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

def get_coordinates(mapcode):
    data = {
        "t": "mapcode",
        "mapcode": mapcode
    }
    
    # Thank you so much for hosting this web service
    response = requests.post("https://saibara.sakura.ne.jp/map/convgeo.cgi", data=data)
    
    latitude = response.text.split('name="jpn_lat" value="')[1].split('"')[0]
    longitude = response.text.split('name="jpn_lon" value="')[1].split('"')[0]
    
    return latitude, longitude

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 get_coordinates.py mapcode")
        sys.exit(1)
    
    mapcode = sys.argv[1]
    
    latitude, longitude = get_coordinates(mapcode)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
