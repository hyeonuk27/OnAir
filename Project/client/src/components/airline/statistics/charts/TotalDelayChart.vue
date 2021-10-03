<template>
  <charts :options="analysisChartOptions" />
</template>

<script>
export default {
  name: 'AnalysisTab',
  props: ['report'],
  data () {
    return {
        analysisChartOptions: {
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
              data: [this.report.under_30]
          }, {
              name: '30분 초과 60분 내 출발',
              data: [this.report.under_60]
          }, {
              name: '60분 이상 지연',
              data: [this.report.over_60]
          }],
        },
      }
  },
}
</script>

<style>

</style>