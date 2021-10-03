<template>
  <div class="review-container">
    <div class="anaylsis-preview">
      <h5 class="text-start">#키워드 #키워드 #키워드 #키워드 #키워드 #키워드</h5>
      <div class="review-head">
        <p class="review-head-total"> 
          총 운항횟수 
          <span class="review-numbers">
            {{ airlineInfo.total_flight }}</span> 회
        </p>
        <p class="review-head-delay-rate">
          평균 지연률 
          <span class="review-numbers">
            {{ (airlineInfo.total_delayed / airlineInfo.total_flight * 100).toFixed(2) }}</span> %
        </p>
        <p class="review-head-cancel-rate">
          평균 결항률 
          <span class="review-numbers">
            {{ (airlineInfo.total_canceled / airlineInfo.total_flight * 100).toFixed(2) }}</span> %
        </p>
      </div>
      <div class="review-body">
        <charts :options="reviewChartOptions" />
      </div>
      <div>
        워드클라우드
      </div>
      <div>
        긍부정비율
      </div>
      <div class="review-rate-container">
        <div>
          상세 별점
        </div>
        <div>
          리뷰 파이차트
        </div>
      </div>
      <div>
        리뷰 리스트
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReviewTab',
  props: ['airlineInfo'],
  data () {
    return {
        reviewChartOptions: {
          chart: {
              type: 'bar',
              height: 100,
              width: 1000,
          },
          title: {
            text: null
          },
          xAxis: {
            visible: false,
            categories: ['지연건수']
          },
          yAxis: {
            visible: false,
          },
          tooltip: {
              pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
              shared: false
          },
          plotOptions: {
              bar: {
                  stacking: 'percent'
              }
          },
          legend: {
              enabled: false
          },
          credits: {
              enabled: false
          },
          exporting: {
              enabled: false
          },
          series: [{
              name: '30분 내 출발',
              data: [this.airlineInfo.under_30]
          }, {
              name: '30분 초과 60분 내 출발',
              data: [this.airlineInfo.under_60]
          }, {
              name: '60분 이상 지연',
              data: [this.airlineInfo.over_60]
          }],
        },
      }
  },
}
</script>

<style>
  .review-container {
    height: auto;
    min-height: 1000px;
  }

  .review-preview {
    max-width: 1000px;
  }

  .review-numbers {
    background-color: #3D2F6B;
    border-radius: 70%;
    color: white;
    display: inline-block;
    font-weight: 400;
    padding: 8px 0px 7px 0px;
    width: 40px;
    height: 40px;
    text-align: center;
    top: -10px;
  }

  .review-head {
    display: grid;
    padding: 10px;
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 5px 10px;
    grid-auto-rows: min-content;
    font-size: 14px;
  }

  .review-head-total {
    grid-column: 1;
    grid-row: 1;
    width: 180px;
  }

  .review-head-delay-rate {
    grid-column: 2;
    grid-row: 1;
    width: 280px;
  }
  
  .review-head-cancel-rate {
    grid-column: 3;
    grid-row: 1;
    width: 280px;
  }

  .review-rate-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 30px;
    grid-auto-rows: min-content;
  }

  .review-rate-details {
    grid-column: 1;
    grid-row: 1;
  }

  .review-rate-chart {
    grid-column: 2;
    grid-row: 1;
  }
</style>