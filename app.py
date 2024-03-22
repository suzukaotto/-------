import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
KEY = os.environ['KEY']

url = 'https://openapi.gg.go.kr/TfcacdStat'
params = {
    'KEY'    : KEY,
    'Type'   : 'json',
    'pIndex' : 1,
    'pSize'  : 100
}

response      = requests.get(url, params)
json_response = json.loads(response.text)
Tfcacd_list = json_response['TfcacdStat'][1]['row']

for Tfcacd in Tfcacd_list:
    if Tfcacd['SIGUN_NM'] != '용인시':
        continue
    
    print(f"집계년도={Tfcacd['SUM_YY']}, 발생건수(건)={Tfcacd['OCCUR_CNT']}, 사망자수(명)={Tfcacd['DPRS_CNT']}, 부상자수(명)={Tfcacd['INJPSN_CNT']}")