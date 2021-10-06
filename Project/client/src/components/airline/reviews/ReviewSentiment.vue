<template>
  <div 
    v-if="isSentimentRendered"
    class="review-sentiment-chart"
  >
    <charts :options="reviewChartOptions" />
  </div>
  <div
    v-else
    style="height: 700px;"
  >
  </div>
</template>

<script>
import axios from 'axios'
import API from '@/common/drf.js'

export default {
  name: 'ReviewSentiment',
  props: {
    airlineId: String,
  },
  data() {
    return {
      isSentimentRendered: false,
      negative: 0,
      positive: 0,
    }
  },
  methods: {
    getSentiment: function () {
      axios({
        url: `${API.URL}${API.ROUTES.reviewDetail}sentiment/${this.airlineId}/`,
        method: 'get',
      })
      .then((res) => {
        this.positive = res.data['positive']
        this.negative = res.data['negative']
        this.isSentimentRendered = true
      })
    },
  },
  created() {
    this.getSentiment()
  },
  computed: {
    reviewChartOptions: function () {
      return {
        chart: {
          type: 'bar',
          height: 100,
          width: 450,
        },
        colors: [
          'rgba(13, 110, 253, 0.75)', 
          'rgba(220, 53, 69, 0.75)'
        ],
        credits: {
          enabled: false
        },
        exporting: {
          enabled: false
        },
        title: {
          text: '리뷰 긍/부정 비율',
          style: {'color': '#3D2F6B', 'font-weight': 'bold'}
        },
        legend: {
          enabled: false,
        },
        xAxis: {
          visible: false,
          categories: ['리뷰 감성분석']
        },
        yAxis: {
          visible: false,
          reversedStacks: false,
        },
        tooltip: {
          pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}%</b><br/>',
          shared: false
        },
        plotOptions: {
          bar: {
            stacking: 'percent',
            borderRadius: 10,
          },
        },
        series: [{
          name: '긍정',
          data: [this.positive]
        }, {
          name: '부정',
          data: [this.negative]
        }],
      }
    },
  }
}
</script>

<style>
  .review-sentiment-chart {
    margin-top: 30px;
  }
</style>