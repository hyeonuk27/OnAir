## EC2 시간 설정

> https://mosei.tistory.com/entry/AWS-EC2-Linux-%EC%84%9C%EB%B2%84-%ED%95%9C%EA%B5%AD%ED%91%9C%EC%A4%80%EC%8B%9C%EA%B0%84%EC%9C%BC%EB%A1%9C-%EB%B3%80%EA%B2%BD%ED%95%98%EA%B8%B0?category=1189099

+ `sudo su - root` : 루트 계정 접속
+ `sudo rm /etc/localtime` : 기존 미국시간 삭제
+ `sudo ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime` : 서울의 시간으로 설정

+ `reboot` : 인스턴스 재시작

+ `date` : 현재 시각 확인
