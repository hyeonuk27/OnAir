<template>
  <div class="analysis-container">
    <div class="anaylsis-preview">
      <h5 class="text-start">
        <ReviewKeyword />
      </h5>
      <div class="analysis-head">
        <p class="analysis-head-total"> 
          총 운항횟수 
          <span style="background-color: #3D2F6B;" class="analysis-numbers">
            {{ report.total }}</span> 회
        </p>
        <p class="analysis-head-delay-rate">
          {{ report.arrival_name }}행 평균 지연률 
          <span style="background-color: #B9A6C9;" class="analysis-numbers">
            {{ report.delay_rate }}</span> %
        </p>
        <p class="analysis-head-delay-time">
          {{ report.arrival_name }}행 평균 지연시간 
          <span style="background-color: #B9A6C9;" class="analysis-numbers">
            {{ report.delay_time }}</span> 분
        </p>
        <p class="analysis-head-predict-time">
          오늘 예상 지연률 
          <span style="background-color: #656F8C;" class="analysis-numbers">
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
              height: 120,
              width: 1000,
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
            categories: ['지연건수']
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
                  stacking: 'percent'
              }
          },
          series: [{
              name: '30분 내 출발',
              dataSorting: {
                enabled: true,
              },
              data: [this.report.under_30]
          }, {
              name: '30분 초과 60분 내 출발',
              dataSorting: {
                enabled: true,
              },
              data: [this.report.under_60]
          }, {
              name: '60분 이상 지연',
              dataSorting: {
                enabled: true,
              },
              data: [this.report.over_60]
          }],
        },
        chart1Options: {
          chart: {
              plotBackgroundColor: null,
              plotBorderWidth: 0,
              plotShadow: false
          },
          colors: [
            '#3D2F6B', '#B9A6C9', '#D4C6E2',
            '#fff6ef', '#eb488a', '#B81F5A'
          ], 
          credits: {
              enabled: false
          },
          exporting: {
              enabled: false
          },
          title: {
              text: this.report.airline_name + '의 전체 지연 사유 분포',
              align: 'center',
              verticalAlign: 'top',
              y: 10
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
                  dataLabels: {
                      enabled: true,
                      distance: 50,
                      style: {
                          fontWeight: 'bold',
                          color: 'white'
                      }
                  },
                  startAngle: -90,
                  endAngle: 90,
                  center: ['50%', '75%'],
                  size: '110%'
              }
          },
          series: [{
              type: 'pie',
              name: '지연 사유',
              innerSize: '50%',
              data: [
                  [this.report.total_delay_list[0], this.report.total_delay_cnt[0]],
                  [this.report.total_delay_list[1], this.report.total_delay_cnt[1]],
                  [this.report.total_delay_list[2], this.report.total_delay_cnt[2]],
                  [this.report.total_delay_list[3], this.report.total_delay_cnt[3]],
                  [this.report.total_delay_list[4], this.report.total_delay_cnt[4]],
                  [this.report.total_delay_list[5], this.report.total_delay_cnt[5]],
                  {
                      name: 'Other',
                      y: 7.61,
                      dataLabels: {
                          enabled: false
                      }
                  }
              ]
          }]
        },
        chart2Options: {
          chart: {
            type: 'spline',
            width: 900,
            scrollablePlotArea: {
              minWidth: 340,
              scrollPositionX: 1
            }
          },
          colors: ['#B9A6C9'], 
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
                  to: 60,
                  color: 'rgba(218, 214, 221)',
                  label: {
                      text: '60분 이하 지연',
                      style: {
                          color: '#606060'
                      }
                  }
              }, { // Light breeze
                  from: 60,
                  to: 160,
                  color: 'rgba(0, 0, 0, 0)',
                  label: {
                      text: '60분 이상 지연(항공 이상)',
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
                  pointInterval: 24 * 3600 * 1000 * 31, // one hour
                  pointStart: Date.UTC(2017, 1, 1, 0, 0, 0)
              }
          },
          series: [{
              name: '평균 지연 시간',
              data: this.report.delay_month_avg_time
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
            width: 450,
          },
          colors: [
            '#3D2F6B', '#B9A6C9', '#D4C6E2',
            '#fff6ef', '#eb488a', '#B81F5A'
          ], 
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
            name: '비율',
            colorByPoint: true,
            data: [{
              name: this.report.arrival_delay_list[0],
              y: this.report.arrival_delay_cnt[0],
              sliced: true,
              selected: true
            }, {
              name: this.report.arrival_delay_list[1],
              y: this.report.arrival_delay_cnt[1]
            }, {
              name: this.report.arrival_delay_list[2],
              y: this.report.arrival_delay_cnt[2]
            }, {
              name: this.report.arrival_delay_list[3],
              y: this.report.arrival_delay_cnt[3]
            }, {
              name: this.report.arrival_delay_list[4],
              y: this.report.arrival_delay_cnt[4]
            }, {
              name: this.report.arrival_delay_list[5],
              y: this.report.arrival_delay_cnt[5]
            }]
          }]
        },
        chart4Options: {
          chart: {
            type: 'column',
            width: 450,
          },
          colors: [
            '#B9A6C9'
          ],
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
            text: '지연사유별 평균지연시간'
          },
          xAxis: {
            categories: this.report.arrival_reason_list,
            crosshair: true
          },
          yAxis: {
            min: 0,
            title: {
              text: '평균 지연시간 (분)'
            }
          },
          tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
              '<td style="padding:0"><b>{point.y:.1f}분</b></td></tr>',
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
            name: '평균 지연시간',
            data: this.report.arrival_avg_time
          }]
        },
        chart5Options: {
          chart: {
            zoomType: 'x',
            width: 450
          },
          colors: [
            '#B9A6C9'
          ], 
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
                          [0, '#B9A6C9'],
                          [1, 'rgba(255, 255, 255, 0.5)'],
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
            width: 450
          },
          colors: [
            '#B9A6C9'
          ],
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
          }]
        },
        chart7Options: {
          chart: {
            type: 'column',
            width: 900,
          },
          colors: ['#B9A6C9'], 
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
    padding-bottom: 50px;
  }

  .analysis-preview {
    max-width: 1000px;
  }

  .analysis-numbers {
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
    width: 1000px;
    font-size: 14px;
    text-align: center;
  }

  .analysis-head-total {
    grid-column: 1;
    grid-row: 1;
    width: 175px;

  }

  .analysis-head-delay-rate {
    grid-column: 2;
    grid-row: 1;
    width: 310px;

  }
  
  .analysis-head-delay-time {
    grid-column: 3;
    grid-row: 1;
    width: 310px;

  }

  .analysis-head-predict-time {
    grid-column: 4;
    grid-row: 1;
    width: 175px;
  }

  .analysis-charts {
    display: inline-grid;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 30px;
    grid-auto-rows: min-content;
  }

  .analysis-chart-1 {
    grid-column: 1 / 3;
    grid-row: 1;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .analysis-chart-2 {
    grid-column: 1 / 3;
    grid-row: 3;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .analysis-chart-3 {
    grid-column: 1;
    grid-row: 2;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .analysis-chart-4 {
    grid-column: 2;
    grid-row: 2;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .analysis-chart-5 {
    grid-column: 1;
    grid-row: 4;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .analysis-chart-6 {
    grid-column: 2;
    grid-row: 4;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .analysis-chart-7 {
    grid-column: 1 / 3;
    grid-row: 5;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>