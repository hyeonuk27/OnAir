<template>
  <div class="review-rate-chart">
    <charts :options="rateChartOptions" />
  </div>
</template>

<script>
export default {
  name: 'ReviewScoreChart',
  props: {
    chartData: Object,
  },
  data () {
    return {
      rateChartOptions: {
        chart: {
          type: 'pie',
          width: 450,
        },
        colors: [
          '#3D2F6B',
          '#A999CF',
          '#B9A6C9',
          '#C8AEE2', 
          '#FFEDF9',
        ], 
        credits: {
          enabled: false
        },
        exporting: {
          enabled: false
        },
        title: {
          text: '평점 분포',
          style: {'color': '#3D2F6B', "font-weight": 'bold'}
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
            name: '1점',
            y: this.chartData['1'],
          },{
            name: '2점',
            y: this.chartData['2'],
          },{
            name: '3점',
            y: this.chartData['3'],
          },{
            name: '4점',
            y: this.chartData['4'],
          },{
            name: '5점',
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