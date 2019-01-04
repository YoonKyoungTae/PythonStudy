# coding=utf-8

#==========================#
# 파이썬 스터디
# 크롤링 연습 2
#==========================#

import requests
from bs4 import BeautifulSoup

def get_subjects():
    subjects = []
    # http 요청
    rq = requests.get("https://basicenglishspeaking.com/daily-english-conversation-topics/")
    html = rq.text
    soup = BeautifulSoup(html, 'html.parser')

    #div 태그에 class가 su-column-inner su-clearfix인 데이터들을 가져올 수 있다.
    divs = soup.findAll('div', {"class" : "su-column-inner su-clearfix"})

    print divs[0].findAll('a')[0]

    # for div in divs:
    #     sources = div.findAll('a')
    #     for source in sources:
    #         data = source.text
    #         subjects.append(data)

    return subjects

results = get_subjects()

for result in results:
    print result

# divs = soup.select('div > a')
#
# for div in divs:
#     print divs