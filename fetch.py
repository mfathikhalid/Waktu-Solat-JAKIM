import requests
import json
import time

# jakim_zones = ['KDH02']

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
data = {}

for zone in jakim_zones:
  params = {
    'r':'esolatApi/TakwimSolat',
    'period': 'month',
    'zone': zone
  }
  
  print(f"Fetching data for : {zone}")
  response = requests.get(url, params=params)
  json_response = response.json()
  
  if response.status_code == 200:
    print(f"Fetch data success : {zone}")
    data[zone] = json_response['prayerTime']
    time.sleep(2)
  else:
    print(f"Fetch data failed : {zone}")
    
with open('data_month.json', 'w') as json_file:
  print("Writing data_month.json")
  json.dump(data, json_file, indent=4)
  print("Finished writing data_month.json")