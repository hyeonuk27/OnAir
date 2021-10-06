<template>
  <div class="footer">
    <div class="footer-container">
      <div style="display: flex;">
        <div class="onair-logo">
          <img style="width: 130px;" src="@/assets/onair_logo.png" alt="onair-logo">
        </div>
        <div class="footer-router">
          <span @click="moveToMain">HOME</span>
          <span onclick="window.open('https://www.notion.so/jiu-park/Data-Set-80694d9e510240ef83c5e34fc55e838a')">데이터</span>
          <span onclick="window.open('https://www.notion.so/jiu-park/980d4c75b284483381cf7999f966879c')">분석도구</span>
          <span onclick="window.open('https://www.notion.so/jiu-park/1-1-a743d46205e643a88856cf847c644078')">고객센터</span>
        </div>
        <div class="onair-plus">
          <p class="notion-link">
            <span style="cursor: pointer;" onclick="window.open('https://www.notion.so/jiu-park/8d8a98436ed448d38bc4381f707df3b5')">CONTACT US</span>
          </p>
        </div>
      </div>
      <div class="footer-onair">
        <span>알고 타자! 믿고 타자! 같이 타자!</span>
      </div>
      <div class="footer-content">
        <img class="footer-favicon" src="@/assets/favicon.png" alt="onair-favicon">
        <div class="onair-info">
          <span class="info">
            On-Air(온에어)는 빅데이터를 활용하여 소비자가 항공사 별 서비스 품질을 시각화한 통합 웹 서비스입니다. 
            데이터를 가공, 분석하여 지연률, 결항률 통계를 시각화하여 제공하며 현재 운행중인 비행기의 지연 시간을 다각도로 예측하여 예비 이용객이 참고할 수 있도록 했습니다. 
            또한 항공사에 대한 리뷰를 남기고 리뷰를 기반으로 한 실사용자의 항공사 별 평가를 감정 분석하여 제공합니다.
          </span>
        </div>
      </div>
      <p class="copyright">Copyright ⓒ 2021<br>On:Air All rights reserved.</p>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Footer',
  methods: {
    ...mapActions([
      'setDeparture',
      'setArrival'
    ]),
    moveToMain: function () {
      if (this.$route.path !== '/') {
        this.setDeparture([])
        this.setArrival([])
        this.$router.push({ name:'Main' })
      }
    },
  }
}
</script>

<style>
.copyright {
  color: #656F8C;
  font-size: 10px;
  margin-top: 10px;
  text-align: right;
}
.footer {
  background-color: #EFEDF2;
  display: flex;
  justify-content: center;
  padding: 30px 0px 30px 0px;
}
.footer-container {
  text-align: left;
  width: 1100px;
}
.footer-content {
  display: flex;
  margin-bottom: 20px;
}
.footer-favicon {
  margin-left: 25px;
  object-fit: cover; 
  width: 72px; 
}
.footer-onair {
  color: #3D2F6B;
  font-size: 14px;
  font-weight: 600;
  margin-left: 220px;
}
.footer-router {
  margin-bottom: 30px;
  margin-left: 50px;
  padding-top: 23px;
}
.footer-router span {
  cursor: pointer;
  margin-right: 143px;
}
.info {
  font-size: 13px;
}
.notion-link, .copyright {
  margin-bottom: 5px;
}
.onair-info {
  color: #656F8C;
  margin-left: 123px;
  text-align: justify;
}
.onair-logo {
  margin-right: 40px;
  margin-top: 10px;
}

.onair-plus {
  color: #3D2F6B;
  padding-top: 23px;
  text-align: right;
}




</style>