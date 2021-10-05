<template>
  <div class='footer'>
    <div class='footer-container'>
      <div class="footer-onair">
        <span>알고 타자! 믿고 타자! 같이 타자!</span>
      </div>
      <div class="footer-content">
        <div class="onair-logo">
          <img src="@/assets/onair_logo.png" alt="onair-logo">
        </div>
        <div class="onair-info">
          <span class="info">
            On-Air(온에어)는 빅데이터를 활용하여 소비자가 항공사 별 서비스 품질을 시각화한 통합 웹 서비스입니다. 
            데이터를 가공, 분석하여 지연률, 결항률 통계를 시각화하여 제공하며 현재 운행중인 비행기의 지연 시간을 다각도로 예측하여 예비 이용객이 참고할 수 있도록 했습니다. 
            또한 항공사에 대한 리뷰를 남기고 리뷰를 기반으로 한 실사용자의 항공사 별 평가를 감정 분석하여 제공합니다.
          </span>
        </div>
        <div class="onair-plus">
          <p class="notion-link" 
            onclick="window.open('https://www.notion.so/jiu-park/4a14719b6de04f31bcbd932e8d2032b5')">
            CONTACT
          </p>
          <p class="copyright">Copyright ⓒ 2021<br>On:Air All rights reserved.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
  .footer {
    background-color: #EFEDF2;
    display: flex;
    justify-content: center;
  }

  .footer-container {
    text-align: left;
    width: 1100px;
  }

  .footer-content {
    display: flex;
    margin-bottom: 20px;
  }

  .footer-onair {
    font-weight: 600;
    margin-top: 30px;
    color: #3D2F6B;
  }


  .onair-logo {
    margin-top: 10px;
    margin-right: 40px;
  }

  .onair-info {
    width: 600px;
    margin-right: 40px;
    text-align: justify;
    color: #656F8C;
  }

  .info {
    font-size: 13px;
  }

  .onair-plus {
    color: #3D2F6B;
    padding-top: 30px;
    text-align: right;
  }

  .notion-link, .copyright {
    margin-bottom: 5px;
  }

  .copyright {
    font-size: 10px;
    color: #656F8C;
  }
</style>