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

# 결과 : 1페이지부터 322페이지까지의 크롤링

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

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
            print '======================================='
            return


def click_page_number(d, page):
    paging = d.find_element_by_class_name('paging')
    lis = paging.find_elements_by_tag_name('li')
    click = lis[page].find_element_by_tag_name('a')
    click.click()
    d.implicitly_wait(3)

def get_page_length(d):
    paging = d.find_element_by_class_name('paging')
    lis = paging.find_elements_by_tag_name('li')
    return len(lis)

## 1페이지부터 10페이지까지 크롤링을 합니다.
def page_parsing_logic(d):
    start_parser(d) # 1페이지 크롤링
    for i in range(1, get_page_length(d)):  # 2페이지부터 10페이지까지의 루프
        click_page_number(d, i)
        start_parser(d)

options = webdriver.ChromeOptions()
options.add_argument('--headless') # ui가 없는 우분투 환경에서의 webdriver 사용
options.add_argument('--no-sandbox')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36") # 마치 실제 유저인것 같은 페이크처리
options.add_argument("lang=ko_KR") # 한국어!
driver = webdriver.Chrome('/home/ubuntu/pythonAPI/chromedriver', chrome_options=options)

driver.get('http://www.sportstoto.co.kr/toto/storeInfo/listAction.do')
driver.implicitly_wait(3)
page_parsing_logic(driver)

# '>' 클릭 후 이동
driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[2]/fieldset/div/a[1]').click()
driver.implicitly_wait(3)
page_parsing_logic(driver)

# '>' 클릭 후 이동
doMoveNextPage = True
while doMoveNextPage:
    try:
        driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[2]/fieldset/div/a[3]').click()
        driver.implicitly_wait(3)
        page_parsing_logic(driver)
        doMoveNextPage = True
    except NoSuchElementException:
        doMoveNextPage = False
        print '크롤링 종료'

print 'while end'