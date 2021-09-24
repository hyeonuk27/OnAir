# AWS EC2에 Spark 설치하기
## 1. Spark 다운로드
- [APACHE Spark 홈페이지](http://spark.apache.org/downloads.html)에 들어간다.
- 아래 사진에서 3번 `Download Spark` 를 클릭한다.
![spark-homepage](https://i.imgur.com/XcHZ941.png)
- HTTP 주소를 복사해둔다.
![http](https://i.imgur.com/KSpw3Yg.png)
- wget 명령으로 압축파일을 다운받는다.
```bash
$ wget https://dlcdn.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
```
- 아래 명령어를 통해 압축을 해제한다.
```bash
$ tar zxvf spark-3.1.2-bin-hadoop3.2.tgz
$ sudo mv spark-3.1.2-bin-hadoop3.2.tgz /opt/
$ sudo ln -s /opt/spark-3.1.2-bin-hadoop3.2.tgz/ /opt/spark
```
<br>

## 2. 환경변수 세팅

- Spark 홈 디렉토리를 환경변수에 세팅한다.
```bash
$ sudo vi /etc/profile.d/spark.sh
```
```shell
export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH

export PYSPARK=/usr/bin/python3
```
```bash
$ . /etc/profile
```
- 터미널 창에 `pyspark` 명령어를 입력하면 실행이 되면서 아래와 같은 터미널 창이 나온다.
![](https://i.imgur.com/gUJA0kW.png)
