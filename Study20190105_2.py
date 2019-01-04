# coding=utf-8

# ==========================#
# 파이썬 스터디
# 크롤링 연습 3
# ==========================#

import requests
from bs4 import BeautifulSoup

rq = requests.get("http://www.sportstoto.co.kr/toto/storeInfo/listAction.do")
html = rq.text

soup = BeautifulSoup(html, 'html.parser')
divs = soup.findAll('div', {"class" : "content"})

# 스포츠 토토 사이트에서 판매점의 리스트를 가져온다.
# 하지만 1페이지만 가져올 수 있고 URL에는 페이지가 표시되어있지 않아서 추가적인 크롤링이 불가하기 때문에
# 다른방법을 추가로 사용해야 할 것 같다.

for div in divs:
    trTags = div.tbody.findAll('tr')
    for tr in trTags:
        tdTags = tr.findAll('td')
        for td in tdTags:
            print td.text
        print '---'


    # td = trData.findAll('td')
    # print td


    # for title in titles:
    #     print title
    #     print title.next_sibling