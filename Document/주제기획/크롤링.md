[TOC]
# Selenium을 활용한 크롤링 방법
> Windows 기준

### ChromeDriver 설치
- 아래와 같은 경로(도움말 > Chrome 정보)로 들어가서 크롬 버전을 확인한다.

![chrome-info](https://i.imgur.com/olJgljK.png)
![chrome-version](https://i.imgur.com/krI45nv.png)

- 아래 다운로드 링크로 들어가서 크롬 버전과 동일한 드라이버를 다운로드 한다.

    - [크롬 드라이버 다운로드](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    
- 크롬 드라이버 압축을 푼다(압축 푼 폴더 위치를 잘 기억해둬야 한다)

<br>

### 라이브러리 설치

```bash
pip install selenium
pip install beautifulsoup4
```
<br>

### 서버 접속

``` python
# 창 띄워지는지 테스트 할 코드
from selenium import webdriver
# 괄호 안에 크롬드라이버의 위치를 넣는다.
driver = webdriver.Chrome('C:/Temp/chromedriver')
# 자동으로 크롬 창을 띄워서 구글에 접속하게 한다.
driver.get('http://www.google.com/ncr')
```

<br>

### beautifulSoup을 이용해서 요소 가져오기

- beautifulSoup을 이용하기 위해서는 CSS 선택자를 이해하고 있는 것이 도움이 된다.
- 개발자 도구를 이용해서 크롤링할 요소를 찾아내서 명시한 후 사용한다.

<br>

### tab 이동해서 작업하기

- 셀레니움으로 처음에 테스트를 할 때, 어떤 요소를 클릭하고 새로운 탭으로 결과가 보여진다면 그 .탭으로 현재 위치를 변경해주는 작업이 필요하다.

```python
# 최근 열린 탭으로 전환
change_tab = driver.window_handles[-1]
driver.switch_to.window(change_tab)<br>
```
