# On : Air 오늘의 항공 정보 분석 서비스 ✈️ 



## 👥 팀원 소개

![banner-long](Document/IMG/banner-long.png)



#### 알고 타자! 믿고 타자! 같이 타자!

> 위드 코로나(With-Corona) 시행에 대한 기대감과 함께 해외여행 계획을 짜고 있는 사람들이 늘고 있다. On:Air(온에어)는 이러한 기대감에 힘입어 실제 이용객이 항공사를 선택하고, 평가하는 데 도움을 줄 수 있도록 개발되었다.
>
> 
>
> On-Air(온에어)는 빅데이터를 활용하여 소비자가 항공사 별 서비스 품질을 시각화한 통합 웹 서비스이다. 데이터를 가공, 분석하여 지연률, 결항률 통계를 시각화하여 제공하며 현재 운행중인 비행기의 지연 시간을 다각도로 예측하여 예비 이용객이 참고할 수 있도록 하였다. 또한 항공사에 대한 리뷰를 남기고 리뷰를 기반으로 한 실사용자의 항공사 별 평가를 감정 분석하여 제공한다.



## 목차

- [1️⃣ 프로젝트 소개](#1️⃣-프로젝트-소개)
  - [📋 기술 스택](#📋 기술 스택)
  - [🎨 컨셉 디자인](#🎨 컨셉 디자인)
- [2️⃣ 프로젝트 구조](#2️⃣ 프로젝트 구조)
  - Backend
  - Frontend
- 프로젝트 산출물
- 프로젝트 결과물



## 1️⃣ 프로젝트 소개



### <center>https://j5a203.p.ssafy.io</center>



1. 일정 : 2021-08-30 ~ 2021-10-08 (총 6주)

- Sub1 : 2021-08-30 ~ 2021-09-03 (1주)
- Sub2 : 2021-09-06 ~ 2021-09-17 (2주)
- Sub3 : 2021-09-20 ~ 2021-10-08 (🔥 NOW 🔥)

2. 팀원

|                                                              |                                                              |                                                              |                                                              |                                                              |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                          **박지우**                          |                          **김채은**                          |                          **김현욱**                          |                          **나승호**                          |                          **안수빈**                          |
| [![Github](./Document/IMG/GitHub-Mark-64px.png)](https://github.com/nu1997) | [![Github](./Document/IMG/GitHub-Mark-64px.png)](https://github.com/chenni0531) | [![Github](./Document/IMG/GitHub-Mark-64px.png)](https://github.com/hyeonuk27) | [![Github](./Document/IMG/GitHub-Mark-64px.png)](https://github.com/qlfflwls5) | [![Github](./Document/IMG/GitHub-Mark-64px.png)](https://github.com/axxsxbxx) |
|                기획<br />디자인<br />통계, DB                |                   기획<br />머신러닝(분석)                   |                   기획<br />머신러닝(분석)                   |                   기획<br />머신러닝(예측)                   |                       기획<br />크롤링                       |



### 📋 기술 스택

1. 이슈관리 : Jira
2. 형상관리 : Gitlab
3. 커뮤니케이션 : Mattetmost, Notion. Slack
4. 개발 환경
   - OS : Windows 10
   - IDE
     - Visual Studio Code 1.58
     - UI/UX : Adobe XD
   - Database : MySQL Workbench 8.0.22
   - Server : AWS EC2 (MobaXterm)
     - Ubuntu 20.04.2 LTS
     - Docker 20.10.7
5. 상세 사용
   - Backend
     - Django 3.2.7
   - Frontend
     - HTML5, CSS3, JavaScript(ES6)
     - Vue 2.6.11, Vuex 3.4.0
   - AWS EC2



### 🎨 컨셉 디자인

![디자인-2](./Document/2_Definition/3_Design/1_Art/IMG/d-1.png)

![디자인-2](./Document/2_Definition/3_Design/1_Art/IMG/d-2.png)



## 2️⃣ 프로젝트 구조

#### - Back

```
server
  ├── accounts
  │   ├── models
  │   ├── views
  │   ├── serializers
  │   └── urls
  │
  ├── airlines
  │   ├── models
  │   ├── views
  │   ├── serializers
  │   └── urls
  │
  ├── hadoop
  │
  └── server 
  ├── statistics
  ├── predict_models
  └── npl
```

#### - Front

```
client
├── node_modules
├── public
└── src
	├── assets
  │ 	
	├── common
	│ 	└── modules
	├── components
  │   ├── airline
  │   ├── auth
  │   ├── main
  │   ├── page
  │   │   ├── Footer
  │   │   └── Navbar
  │   └── profile
  │    
	└── views
		├── airline
		├── login
		├── main
		└── profile
```



## 3️⃣ 프로젝트 산출물

> 기술  및 운영 관련 문서

- [Architecture]((Document/2_Definition/1_Architecture))
  
  - MySQL 연결
  - EC2 시간 설정
  - AWS EC2에 Spark 설치
  
- Analysis

  - [예측분석](Document/3_Development/2_Analysis/AirlineAnalysis)
  - [크롤링](Document/3_Development/2_Analysis/DataCrawling)
  - [감성분석](Document/3_Development/2_Analysis/ReviewAnalysis)

- [Deploy](Document/5_Deployment/1_AutoDeploy)

  ##### --- 추가중입니다

## 4️⃣ 프로젝트 결과물

[기획 발표](Document/1_Concept/Presentation)

