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

# 결과 : 목표 사이트의 1페이지부터 10페이지까지 크롤링을 처리한다.

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

def start_parser(d):
    # 기존 크롤링 순서와 동일
    html = d.page_source
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.findAll('div', {"class": "content"})

    for div in divs:
        tr_tags = div.tbody.findAll('tr')
        for tr in tr_tags:
            tr_tags = tr.findAll('td')

            result = ''
            for td in tr_tags:
                result += td.text + ' | '
            print result

def click_number(d, page):
    print '======================================='
    paging = d.find_element_by_class_name('paging')
    lis = paging.find_elements_by_tag_name('li')
    click = lis[page].find_element_by_tag_name('a')
    click.click()
    d.implicitly_wait(3)

options = webdriver.ChromeOptions()
options.add_argument('--headless') # ui가 없는 우분투 환경에서의 webdriver 사용
options.add_argument('--no-sandbox')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36") # 마치 실제 유저인것 같은 페이크처리
options.add_argument("lang=ko_KR") # 한국어!
driver = webdriver.Chrome('/home/ubuntu/pythonAPI/chromedriver', chrome_options=options)

driver.get('http://www.sportstoto.co.kr/toto/storeInfo/listAction.do')
driver.implicitly_wait(3)

start_parser(driver)

for index in range(1, 10): # 2페이지부터 10페이지까지의 루프
    click_number(driver, index)
    start_parser(driver)