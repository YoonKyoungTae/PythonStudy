# coding=utf-8

#==========================#
# 파이썬 스터디
# 크롤링 하기
# 특정 사이트를 크롤링 하여 공지사항만 출력하는 코드
#==========================#

import requests
from bs4 import BeautifulSoup

# http 요청
requests = requests.get("http://dowellcomputer.com/main.jsp")

# request에서 html 가져와서 print 한다.
html = requests.text

# html 변수는 html에 대한 text를 가지고 있다.
# print html

# HTML 소스코드를 파이썬 객체로 반환한다.
soup = BeautifulSoup(html, 'html.parser')

# <td> 태그 안쪽에 <a> 태그를 찾는다.
# <td class="tail"><a href="./notice/noticeViewForm.jsp?noticeID=4"><b>자바 기초 프로그래밍 강좌를 완강했습니다.</b></a></td>
# soup.select는 배열 형식으로 조건에 맞는 데이터들을 추출한다.
aTags = soup.select('td > a')

# 추출된 조건에 맞는 a 태그들
# print aTags

# 조건에 해당되는 태그들 중 원하는 데이터를 뽑아낸다.
for tag in aTags:

    # href 경로가 들어있는가?
    if tag.has_attr('href'):

        # href 의 값을 가져온다.
        hrefText = tag.get('href')

        # 그 값에 notice 라는 단어가 있는지 확인한다. (notice 데이터를 파싱할 것이다.)
        isContainNoticePath = hrefText.find('notice')

        # 결과가 -1 이 나오면 값이 없다는 뜻. 즉, -1이 아니면 값이 있다.
        if isContainNoticePath != -1:

            # 공지사항 데이터만 출력하게 된다.
            print(tag.text)