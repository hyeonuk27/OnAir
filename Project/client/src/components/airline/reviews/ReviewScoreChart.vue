<template>
  <div class="review-rate-chart">
    <charts :options="rateChartOptions" />
  </div>
</template>

<script>
export default {
  name: "ReviewScoreChart",
  props: ['chartData'],
  data () {
    return {
      rateChartOptions: {
        chart: {
          type: 'pie',
          width: 450,
        },
        colors: [
          '#FFEDF9',
          '#C8AEE2', 
          '#B9A6C9',
          '#A999CF',
          '#3D2F6B',
        ], 
        credits: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        title: {
          text: '별점 분포',
          style: {"color": '#3D2F6B', "font-weight": 'bold'}
        },
        tooltip: {
          pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
          },
        accessibility: {
          point: {
            valueSuffix: '%'
          }
        },
        plotOptions: {
          pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
              enabled: false
            },
            showInLegend: true
          }
        },
        series: [{
          name: '비율',
          colorByPoint: true,
          data: [{
            name: '★',
            y: this.chartData['1'],
          },{
            name: '★★',
            y: this.chartData['2'],
          },{
            name: '★★★',
            y: this.chartData['3'],
          },{
            name: '★★★★',
            y: this.chartData['4'],
          },{
            name: '★★★★★',
            y: this.chartData['5'],
          }
          ]
        }]
      }, 
    }
  },
}
</script>

<style>
.review-rate-chart {
  padding: 10px;
}
</style>