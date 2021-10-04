<template>
  <div class="analysis-container">
    <div class="anaylsis-preview">
      <h5 class="text-start">
        <ReviewKeyword />
      </h5>
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
            {{ report.predicted_delay_rate }}</span> %
        </p>
      </div>
      <div class="analysis-body">
        <charts :options="analysisChartOptions" />
      </div>
      <div class="analysis-charts">
        <div class="analysis-chart-1">
          <charts :options="chart1Options" />
        </div>
        <div class="analysis-chart-2">
          <charts :options="chart2Options" />
        </div>
        <div class="analysis-chart-3">
          <charts :options="chart3Options" />
        </div>
        <div class="analysis-chart-4">
          <charts :options="chart4Options" />
        </div>
        <div class="analysis-chart-5">
          <charts :options="chart5Options" />
        </div>
        <div class="analysis-chart-6">
          <charts :options="chart6Options" />
        </div>
        <div class="analysis-chart-7">
          <charts :options="chart7Options" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewKeyword from "@/components/airline/reviews/ReviewKeyword";

export default {
  name: 'AnalysisTab',
  props: ['report'],
  components: {
  ReviewKeyword
  },
  data() {
    return {
        analysisChartOptions: {
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
        chart1Options: {
          chart: {
            type: 'pie',
            width: 340,
          },
          credits: {
              enabled: false
          },
          exporting: {
              enabled: false
          },
          title: {
            text: this.report.airline_name + '의 전체 지연 사유 분포'
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
            name: '지연 사유',
            colorByPoint: true,
            data: [{
              name: 'Chrome',
              y: 61.41,
              sliced: true,
              selected: true
            }, {
              name: 'Internet Explorer',
              y: 11.84
            }, {
              name: 'Firefox',
              y: 10.85
            }, {
              name: 'Edge',
              y: 4.67
            }, {
              name: 'Safari',
              y: 4.18
            }, {
              name: 'Other',
              y: 7.05
            }]
          }]
        },
        chart2Options: {
          chart: {
            type: 'spline',
            width: 340,
            height: 340,
            scrollablePlotArea: {
              minWidth: 340,
              scrollPositionX: 1
            }
          },
          credits: {
              enabled: false
          },
          exporting: {
              enabled: false
          },
          legend: {
              enabled: false
          },
          title: {
            text: this.report.airline_name + '의 월별 평균 지연시간',
          },
          xAxis: {
            type: 'datetime',
            labels: {
              overflow: 'justify'
            }
          },
          yAxis: {
              title: {
                  text: '평균 지연시간'
              },
              minorGridLineWidth: 0,
              gridLineWidth: 0,
              alternateGridColor: null,
              plotBands: [{ // Light air
                  from: 0,
                  to: 30,
                  color: 'rgba(68, 170, 213, 0.1)',
                  label: {
                      text: '정시 출발',
                      style: {
                          color: '#606060'
                      }
                  }
              }, { // Light breeze
                  from: 30,
                  to: 60,
                  color: 'rgba(0, 0, 0, 0)',
                  label: {
                      text: '지각',
                      style: {
                          color: '#606060'
                      }
                  }
              }]
          },
          tooltip: {
              valueSuffix: ' 분'
          },
          plotOptions: {
              spline: {
                  lineWidth: 4,
                  states: {
                      hover: {
                          lineWidth: 5
                      }
                  },
                  marker: {
                      enabled: false
                  },
                  pointInterval: 3600000, // one hour
                  pointStart: Date.UTC(2018, 1, 13, 0, 0, 0)
              }
          },
          series: [{
              name: 'Hestavollane',
              data: [
                  37, 33, 39, 51, 35, 38, 40, 50, 61, 37, 33, 64,
                  69, 60, 68, 49, 40, 38, 50, 49, 92, 96, 95, 63,
                  95, 108, 140, 115, 100, 102, 103, 94, 89, 106, 105, 111,
                  104, 107, 113, 102, 96, 102, 111, 108, 130, 125, 125, 113,
                  101
              ]
          }],
          navigation: {
              menuItemStyle: {
                  fontSize: '10px'
              }
          }
        },
        chart3Options: {
          chart: {
            type: 'pie',
            width: 340,
          },
          credits: {
              enabled: false
          },
          exporting: {
              enabled: false
          },
          title: {
            text: this.report.arrival_name + '행 지연 사유 분포'
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
            name: 'Brands',
            colorByPoint: true,
            data: [{
              name: 'Chrome',
              y: 61.41,
              sliced: true,
              selected: true
            }, {
              name: 'Internet Explorer',
              y: 11.84
            }, {
              name: 'Firefox',
              y: 10.85
            }, {
              name: 'Edge',
              y: 4.67
            }, {
              name: 'Safari',
              y: 4.18
            }, {
              name: 'Other',
              y: 7.05
            }]
          }]
        },
        chart4Options: {
          chart: {
            type: 'pie',
            width: 340,
          },
          credits: {
              enabled: false
          },
          exporting: {
              enabled: false
          },
          title: {
            text: '지연사유별 평균지연시간'
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
              name: '연결-항공기에 의한 지연',
              y: 61.41,
              sliced: true,
              selected: true
            }, {
              name: '항로혼잡에 의한 지연',
              y: 11.84
            }, {
              name: '연결-승객에 의한 지연',
              y: 10.85
            }, {
              name: '제방빙작업에 의한 지연',
              y: 4.67
            }, {
              name: '기타',
              y: 4.18
            }, {
              name: '주기장혼잡(부족)에 의한 지연',
              y: 7.05
            }]
          }]
        },
        chart5Options: {
          chart: {
            zoomType: 'x',
            width: 485
          },
          title: {
              text: '월별 이용객 추이'
          },
          credits: {
              enabled: false
          },
          exporting: {
              enabled: false
          },
          xAxis: {
              type: 'datetime'
          },
          yAxis: {
              title: {
                  text: '이용객 수'
              }
          },
          legend: {
              enabled: false
          },
          plotOptions: {
              area: {
                  fillColor: {
                      linearGradient: {
                          x1: 0,
                          y1: 0,
                          x2: 0,
                          y2: 1
                      },
                      stops: [
                          [0, '#2f7ed8'],
                          [1, '#B2A6A8'],
                      ]
                  },
                  marker: {
                      radius: 2
                  },
                  lineWidth: 1,
                  states: {
                      hover: {
                          lineWidth: 1
                      }
                  },
                  threshold: null
              }
          },
          series: [{
              type: 'area',
              name: '월별 이용객 수',
              data: this.report.passengers_by_month
          }],
        },
        chart6Options: {
          chart: {
            type: 'column',
            width: 485
          },
          credits: {
              enabled: false
          },
          exporting: {
              enabled: false
          },
          legend: {
            enabled: false
          },
          title: {
            text: '월별 이용객 에 따른 지연률 예측'
          },
          xAxis: {
            categories: this.report.month_list,
            crosshair: true
          },
          yAxis: {
            min: 0,
            title: {
              text: '지연률 (%)'
            }
          },
          tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
              '<td style="padding:0"><b>{point.y:.2f} %</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
          },
          plotOptions: {
            column: {
              pointPadding: 0.2,
              borderWidth: 0
            }
          },
          series: [{
            name: '지연률',
            data: this.report.predicted_by_passengers
            // data: [0.5, 0.6, 0.75]
          }]
        },
        chart7Options: {
          chart: {
            type: 'column',
            width: 1000
          },
          credits: {
              enabled: false
          },
          exporting: {
              enabled: false
          },
          legend: {
            enabled: false
          },
          title: {
            text: '날씨에 따른 지연률 예측'
          },
          xAxis: {
            categories: this.report.weather_list,
            crosshair: true
          },
          yAxis: {
            min: 0,
            title: {
              text: '지연률 (%)'
            }
          },
          tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
              '<td style="padding:0"><b>{point.y:.2f} %</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
          },
          plotOptions: {
            column: {
              pointPadding: 0.2,
              borderWidth: 0
            }
          },
          series: [{
            name: '지연률',
            data: this.report.predicted_by_weather
          }]
        },
    }
  }}
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

  .analysis-chart-7 {
    grid-column: 1 / 3;
    grid-row: 4;
  }
</style>