<template>
  <div 
  v-if="isSentimentRendered"
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
import axios from "axios";
import API from "@/common/drf.js";

export default {
  name: "ReviewSentiment",
  props: {
    airlineId: String,
  },
  data() {
    return {
      positive: 0,
      negative: 0,
      isSentimentRendered: false,
      reviewChartOptions: {
        chart: {
            type: 'bar',
            height: 150,
            width: 1000,
        },
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
          categories: ['지연건수']
        },
        yAxis: {
          visible: false,
        },
        tooltip: {
            pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}%</b><br/>',
            shared: false
        },
        plotOptions: {
            bar: {
                stacking: 'percent'
            }
        },
        series: [{
            name: '긍정',
            data: [this.positive]
        }, {
            name: '부정',
            data: [this.negative]
        }],
      },
    }
  },
  methods: {
    getSentiment: function () {
      axios({
        url: `${API.URL}${API.ROUTES.reviewDetail}sentiment/${this.airlineId}/`,
        method: "get",
      })
        .then((res) => {
          this.positive = res.data['positive']
          this.negative = res.data['negative']
          this.isSentimentRendered = true
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getSentiment();
  },
  // computed: {
  //   getPositive: function () {
  //     return this.positive
  //   },
  //   getNegative: function () {
  //     return this.negative
  //   }
  // }
};
</script>

<style>
#bar-negative {
  background-color: #f7cac9;
}
#bar-positive {
  background-color: #92a8d1;
}
</style>