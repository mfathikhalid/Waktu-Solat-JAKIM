import requests
import json
import time
import os
import datetime

current_my = datetime.datetime.now().strftime("%m-%Y")

data_dir = "data"
if os.path.isdir(data_dir) == False:
    # Create data directory if it doesn't exist
    print("Creating data directory")
    os.makedirs(data_dir, exist_ok=True)

jakim_zones = [
  'JHR01', 'JHR02', 'JHR03', 'JHR04',
  'KDH01', 'KDH02', 'KDH03', 'KDH04', 'KDH05', 'KDH06', 'KDH07',
  'KTN01', 'KTN02',
  'MLK01',
  'NGS01', 'NGS02', 'NGS03',
  'PHG01', 'PHG02', 'PHG03', 'PHG04', 'PHG05', 'PHG06',
  'PLS01',
  'PNG01',
  'PRK01', 'PRK02', 'PRK03', 'PRK04', 'PRK05', 'PRK06', 'PRK07',
  'SBH01', 'SBH02', 'SBH03', 'SBH04', 'SBH05', 'SBH06', 'SBH07', 'SBH08', 'SBH09',
  'SGR01', 'SGR02', 'SGR03',
  'SWK01', 'SWK02', 'SWK03', 'SWK04', 'SWK05', 'SWK06', 'SWK07', 'SWK08', 'SWK09',
  'TRG01', 'TRG02', 'TRG03', 'TRG04',
  'WLY01', 'WLY02'
]

url = "https://www.e-solat.gov.my/index.php"

for zone in jakim_zones:

    zone_dir = os.path.join(data_dir, zone)
    file_path = os.path.join(zone_dir, f"{current_my}.json")
    
    if os.path.isdir(zone_dir) == False:
        # Create data directory if it doesn't exist
        print(f"Creating {zone} directory")
        os.makedirs(zone_dir, exist_ok=True)
        
    print(f"Fetching data ({zone})")
    params = {
        'r': 'esolatApi/TakwimSolat',
        'period': 'month',
        'zone': zone
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        print(f"Fetch data success ({zone})")
        json_response = response.json()
        
        if os.path.isfile(file_path) == False:
          print("File not found, creating new file")
          with open(file_path, 'w') as file:
              json.dump(json_response['prayerTime'], file, indent=4)
              print("Write to file success")
        else:
          print("File exists")
    else:
        print(f"Fetch data failed ({zone})")
    
    # Sleep for 2 seconds to avoid hitting the server too hard
    time.sleep(2)