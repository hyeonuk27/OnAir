<template>
  <div class="review-container">
    <div class="review-preview">
      <h5 class="text-start">
        <ReviewKeyword :airlineId="airlineId"/>
      </h5>
      <div class="review-head">
        <p class="review-head-total">
          {{ airlineInfo.name }} 총 운항횟수
          <span style="background-color: #3D2F6B;" class="review-numbers"> {{ airlineInfo.total_flight }}</span> 회
        </p>
        <p class="review-head-delay-rate">
          {{ airlineInfo.name }} 평균 지연률
          <span style="background-color: #B9A6C9;" class="review-numbers">
            {{ (airlineInfo.total_delayed / airlineInfo.total_flight * 100).toFixed(2) }}</span> %
        </p>
        <p class="review-head-cancel-rate">
          {{ airlineInfo.name }} 평균 결항률
          <span style="background-color: #B9A6C9;" class="review-numbers">
            {{ (airlineInfo.total_canceled / airlineInfo.total_flight * 100).toFixed(2) }}</span> %
        </p>
      </div>
      <div class="review-body">
        <charts :options="reviewChartOptions" />
      </div>
      <div>
        <ReviewWordcloud :airlineId="airlineId"/>
      </div>

      <div class="review-rate-container">
        <div class="review-rate-left">
          <div class="review-sentiment">
            <ReviewSentiment :airlineId="airlineId"/>
          </div>
          <div class="review-rate-detail">
            <ReviewScore :airlineId="airlineId"/>
          </div>
        </div>
        <div class="review-rate-right">
          <div class="review-rate-chart">
            <ReviewScoreChart 
            :chartData="chartData"
            />
          </div>
        </div>
      </div>
      <div>
        <!-- 리뷰 작성 버튼 -->
        <ReviewCreateButton
          :airlineId="airlineId"
          :arrivalId="arrivalId"
          :arrivalName="arrivalName"
        />
      </div>
      <div>
        <!-- 리뷰 리스트 -->
        <ReviewList :airlineId="airlineId" />
      </div>
    </div>
  </div>
</template>

<script>
import ReviewKeyword from "@/components/airline/reviews/ReviewKeyword";
import ReviewWordcloud from "@/components/airline/reviews/ReviewWordcloud";
import ReviewSentiment from "@/components/airline/reviews/ReviewSentiment";
import ReviewScore from "@/components/airline/reviews/ReviewScore";
import ReviewScoreChart from "@/components/airline/reviews/ReviewScoreChart";
import ReviewCreateButton from "@/components/airline/reviews/ReviewCreateButton";
import ReviewList from "@/components/airline/reviews/ReviewList";

export default {
  name: "ReviewTab",
  props: ["airlineInfo", "airlineId", "arrivalId", "arrivalName", 'chartData'],
  components: {
    ReviewKeyword,
    ReviewWordcloud,
    ReviewSentiment,
    ReviewScore,
    ReviewScoreChart,
    ReviewCreateButton,
    ReviewList,
  },
  data() {
    return {
      reviewChartOptions: {
        chart: {
          type: "bar",
          height: 120,
          width: 1000
        },
        colors: [
          '#3D2F6B', '#B9A6C9', '#B81F5A'
        ], 
        credits: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        title: {
          text: null,
        },
        xAxis: {
          visible: false,
          categories: [this.airlineInfo.name + '의 지연 데이터'],
        },
        yAxis: {
          visible: false,
          reversedStacks: false,
        },
        tooltip: {
          pointFormat:
            '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.2f}%)<br/>',
          shared: false,
        },
        plotOptions: {
          bar: {
            stacking: "percent",
          },
        },
        legend: {
          enabled: true,
        },
        series: [
          {
            name: "30분 내 출발",
            data: [this.airlineInfo.under_30],
          },
          {
            name: "30분 초과 60분 내 출발",
            data: [this.airlineInfo.under_60],
          },
          {
            name: "60분 이상 지연",
            data: [this.airlineInfo.over_60],
          },
        ],
      },
    };
  },
};
</script>

<style scoped>
.review-container {
  height: auto;
  min-height: 1000px;
}

.review-preview {
  max-width: 1000px;
}

.review-numbers {
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
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 5px 10px;
  grid-auto-rows: min-content;
  font-size: 14px;
  font-weight: bold;
}

.review-head-total {
  grid-column: 1;
  grid-row: 1;
}

.review-head-delay-rate {
  grid-column: 2;
  grid-row: 1;
}

.review-head-cancel-rate {
  grid-column: 3;
  grid-row: 1;
}

.review-rate-container {
  display: grid;
  grid-template-columns: 450px 450px;
  grid-template-rows: 1fr 2fr;
  grid-gap: 20px;
  padding: 20px;
  border: 1px solid rgba(180, 180, 180, 0.658);
  margin-bottom: 25px;
}

.review-rate-left {
  grid-column: 1;
  grid-row: 1 / 3;
}

.review-rate-right {
  grid-column: 2;
  grid-row: 1 / 3;
}

.review-rate-detail {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 340px;
}

.review-sentiment {
  display: flex;
  justify-content: center;
  align-items: center;
}


</style>