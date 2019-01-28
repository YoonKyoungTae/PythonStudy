# coding=utf-8

# ==========================#
# 파이썬 스터디
# 크롤링 연습
# 셀레니움 임포트
# 참고자료
# https://hanmaruj.tistory.com/3
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/
# ==========================#

# 결과 : 스포츠토토 사이트에서 a를 입력 후 검색하여 나온 결과를 출력한다.

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless') # ui가 없는 우분투 환경에서의 webdriver 사용
options.add_argument('--no-sandbox')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36") # 마치 실제 유저인것 같은 페이크처리
options.add_argument("lang=ko_KR") # 한국어!
driver = webdriver.Chrome('/home/ubuntu/pythonAPI/chromedriver', chrome_options=options)

driver.get('http://www.sportstoto.co.kr/toto/storeInfo/listAction.do')
driver.implicitly_wait(3)
driver.find_element_by_name('keyWord').send_keys('a') # keyWord 폼에 a를 입력한다.
driver.find_element_by_xpath('//*[@id="searchForm"]/a').click() # 크롬 개발자 도구에서 버튼 우클릭 -> xpath를 복사 할 수 있다.

# 기존 크롤링 순서와 동일
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
divs = soup.findAll('div', {"class" : "content"})

for div in divs:
    trTags = div.tbody.findAll('tr')
    for tr in trTags:
        tdTags = tr.findAll('td')
        for td in tdTags:
            print td.text
        print '---'

print divs
