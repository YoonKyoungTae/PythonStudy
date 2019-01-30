#-*- coding:utf-8 -*-

# ==========================#
# 파이썬 스터디
# Kakao Api 연결
# ==========================#

# 결과 : 카카오 api를 이용하여 특정 주소의 좌표를 얻어낸다.

import requests

kakao_api_url = 'https://dapi.kakao.com/v2/local/search/address.json'
address = '강원 원주시 배울로 17'
query = '?query='
headers = {'Authorization': 'KakaoAK 56165e9801eac8d7e760bd16a12304f1'}

res = requests.get(kakao_api_url + query + address, headers=headers)
json = res.json()
print json

documents = json['documents']
doc = documents[0]

print doc['x']
print doc['y']