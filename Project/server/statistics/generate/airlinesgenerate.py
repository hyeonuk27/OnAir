import pandas as pd
from pandas.io.parsers import read_csv

import random, string

def make_random_id():
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(13))

df = read_csv('./statistics_data.csv')
df = df['airline'].drop_duplicates().reset_index(drop=True)
df = pd.DataFrame(df, columns=['airline'])
df = df.rename(columns = {'airline': 'name'})

"""
0,아시아나항공
1,대한항공
2,진에어
3,티웨이항공
4,에어서울
5,중국동방항공
6,중국남방항공
7,제주항공
8,독일항공
9,프랑스항공
10,유나이티드항공
11,델타항공
12,네덜란드항공
13,에미레이트항공
14,카타르항공
15,아메리칸항공
"""

id = [ make_random_id() for _ in range(16) ]

profile_url = [
    'https://flyasiana.com/C/pc/image/sub/img_ci_english.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/KoreanAir_logo.svg/1280px-KoreanAir_logo.svg.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/JinAir.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/TWayAirlines.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/AirSeoul.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/ChinaEasternAirlines.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/ChinaSouthernAirlines.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/JejuAirNew.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/Lufthansa_02.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/AirFrance.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/UnitedAirlines.png',
    'https://w7.pngwing.com/pngs/416/132/png-transparent-delta-air-lines-direct-flight-airline-codeshare-agreement-state-security-investigations-service-angle-text-triangle.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/KLM.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/Emirates2.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/QatarAirways.png',
    'https://www.tripadvisor.co.kr/img2/flights/airlines/logos/100x100/AmericanAirlines.png'
]
address = [
    'No 47 Osae-Dong, Gangseo-gu, 서울 157-713',
    'Korean Air Operations Center, 1370 Gonghang-Dong, 서울 157712',
    '453, Gonghang-daero, Gangseo-gu, 서울 157-841',
    'Seongdong-0169, Haneul-gil, Gangseo-gu, 서울',
    '76, SaemunanRo Jongro Gu, 서울',
    '2nd Floor Citibank Tower, No. 33 Shanghai Huayuanshiqiao Road, 상하이 중국 201202',
    '278 Jichang Road, 광저우 중국 510405',
    '312-1 Yon-Dong, 제주 63000',
    'Von-Gablenz- Strasse 2-6, 쾰른 노스라인-웨스트팔리아 독일 50679',
    '45 rue de Paris, Roissy-en-France 프랑스 95 747',
    '233 S. Wacker Drive, 시카고, IL 60606',
    '1030 Delta Blvd, 애틀랜타, GA 30354',
    'Amsterdamseweg 55, 암스텔펜 네덜란드 1182 GP',
    'PO Box 686, 두바이 아랍에미리트',
    'Qatar Airways Tower Airport Road, 도하 카타르',
    '4333 Amon Carter Boulevard, 포트 워스, TX 76155-2605'
]
phone_number = [
    '02-2669-8000',
    '1588-2001',
    '1600-6200',
    '1688-8686',
    '1800-8100',
    '+86 95530',
    '+86 95539',
    '1599-1500',
    '+49 69 86799799',
    '+33 3654',
    '+1 800-864-8331',
    '+1 800-221-1212',
    '+31 20 474 7747',
    '+971 600 555555',
    '+974 4023 0000',
    '+1 800-433-7300'
]
site_url = [
    'https://flyasiana.com/C/US/KO/index',
    'http://www.koreanair.com/',
    'http://www.jinair.com/',
    'https://www.twayair.com/',
    'https://flyairseoul.com/',
    'http://www.flychinaeastern.com/',
    'http://www.csair.com/',
    'http://www.jejuair.net/',
    'http://www.lufthansa.com/',
    'http://www.airfrance.com/',
    'http://www.united.com/',
    'https://www.delta.com/',
    'http://www.klm.com/',
    'http://www.emirates.com/',
    'http://www.qatarairways.com/',
    'https://www.aa.com/'
]
corona_url = [
    'https://flyasiana.com/C/US/KO/contents/stay-safe-with-oz',
    'https://www.koreanair.com/global/en/about/news/travel_info/2020_03_covid/',
    'https://www.jinair.com/company/announce/announceView?anceSeq=21258&searchWord=&searchKey=&page=1',
    'https://www.twayair.com/app/customerCenter/notice',
    'https://flyairseoul.com/CW/en/noticeList.do',
    'https://us.ceair.com/en/',
    'https://global.csair.com/',
    'https://www.jejuair.net/jejuair/kr/event/safeHealthy.do',
    'https://www.lufthansa.com/xx/en/flight-information.html',
    'https://www.airfrance.us/US/en/common/page_flottante/hp/news-air-traffic-air-france.htm?_ga=2.8073783.483960263.1584621588-331937894.1584621588',
    'https://www.united.com/ual/en/us/fly/travel/notices.html',
    'https://www.delta.com/us/en/coronavirus-update-center/overview?Log=1&mkcpgn=sezzzggusabspribd&clickid=_k_CjwKCAjwsMzzBRACEiwAx4lLGygzDI5b8sjmc1HQZ4Jyiy5DVmqwQyPpC1Idei5gkgxSnJxcLfqtzRoCJYAQAvD_BwE_k_&tracking_id=284x10598556&ad_id=425479292874&s_kwcid=TC%7Cdelta%7C%7CS%7Ce%7C425479292874&campaign=9617149371&adgroup=99126258916&gclid=CjwKCAjwsMzzBRACEiwAx4lLGygzDI5b8sjmc1HQZ4Jyiy5DVmqwQyPpC1Idei5gkgxSnJxcLfqtzRoCJYAQAvD_BwE',
    'https://www.klm.com/travel/us_en/prepare_for_travel/up_to_date/flight_update/index.htm',
    'https://www.emirates.com/us/english/help/travel-updates/#3515',
    'https://www.qatarairways.com/en/travel-alerts/COVID-19-update.html',
    'https://www.aa.com/i18n/travel-info/coronavirus-updates.jsp',
]

is_skyteam =[
    0,
    1,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    0,
    0
]
is_star = [
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    0
]
is_oneworld = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1
]

df['id'] = id
df['profile_url'] = profile_url
df['address'] = address
df['phone_number'] = phone_number
df['site_url'] = site_url
df['corona_url'] = corona_url
df['is_skyteam'] = is_skyteam
df['is_star'] = is_star
df['is_oneworld'] = is_oneworld

df.to_csv('../airlines.csv')