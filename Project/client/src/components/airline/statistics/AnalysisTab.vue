<template>
  <div class="analysis-container">
    <div class="anaylsis-preview">
      <h5 class="text-start">#키워드 #키워드 #키워드 #키워드 #키워드 #키워드</h5>
      <div class="analysis-head">
        <p class="analysis-head-total"> 
          총 운항횟수 
          <span class="analysis-numbers">
            {{ report.total }}</span> 회
        </p>
        <p class="analysis-head-delay-rate">
          {{ report.arrival_name }}행 평균 지연률 
          <span class="analysis-numbers">
            {{ report.delay_rate }}</span> %
        </p>
        <p class="analysis-head-delay-time">
          {{ report.arrival_name }}행 평균 지연시간 
          <span class="analysis-numbers">
            {{ report.delay_time }}</span> 분
        </p>
        <p class="analysis-head-predict-time">
          오늘 예상 지연률 
          <span class="analysis-numbers">
            {{ predictedDelayRate }}</span> %
        </p>
      </div>
      <div class="analysis-body">
        <highcharts :options="analysisChartOptions"></highcharts>
        <TotalDelayChart 
        :report="report"/>
        <GChart />
      </div>
      <div class="analysis-charts">
        <div class="analysis-chart-1">
          Chart1
        </div>
        <div class="analysis-chart-2">
          Chart2
        </div>
        <div class="analysis-chart-3">
          Chart3
        </div>
        <div class="analysis-chart-4">
          Chart4
        </div>
        <div class="analysis-chart-5">
          Chart5
        </div>
        <div class="analysis-chart-6">
          Chart6
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TotalDelayChart from '@/components/airline/statistics/charts/TotalDelayChart'
import { GChart } from 'vue-google-charts'
import {Chart} from 'highcharts-vue'

export default {
  name: 'AnalysisTab',
  props: ['report', 'predictedDelayRate'],
  components: {
    highcharts: Chart,
    TotalDelayChart,
    GChart
  },
  data() {
    return {
        analysisChartOptions: {
          chart: {
              type: 'bar',
              height: 100,
              width: 1000,
          },
          title: {
            // text: null,
            text: '지연시간 분포표'
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
  .analysis-container {
    height: auto;
    min-height: 1000px;
  }

  .analysis-preview {
    max-width: 1000px;
  }

  .analysis-numbers {
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

  .analysis-head {
    display: grid;
    padding: 10px;
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 5px 10px;
    grid-auto-rows: min-content;
    font-size: 14px;
  }

  .analysis-head-total {
    grid-column: 1;
    grid-row: 1;
    width: 180px;
  }

  .analysis-head-delay-rate {
    grid-column: 2;
    grid-row: 1;
    width: 280px;
  }
  
  .analysis-head-delay-time {
    grid-column: 3;
    grid-row: 1;
    width: 280px;
  }

  .analysis-head-predict-time {
    grid-column: 4;
    grid-row: 1;
    width: 180px;
  }

  .analysis-charts {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 30px;
    grid-auto-rows: min-content;
  }

  .analysis-chart-1 {
    grid-column: 1;
    grid-row: 1;
  }

  .analysis-chart-2 {
    grid-column: 2;
    grid-row: 1;
  }

  .analysis-chart-3 {
    grid-column: 1;
    grid-row: 2;
  }

  .analysis-chart-4 {
    grid-column: 2;
    grid-row: 2;
  }

  .analysis-chart-5 {
    grid-column: 1;
    grid-row: 3;
  }

  .analysis-chart-6 {
    grid-column: 2;
    grid-row: 3;
  }
</style>