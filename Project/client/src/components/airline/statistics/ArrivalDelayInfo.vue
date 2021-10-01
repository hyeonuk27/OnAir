<template>
  <div>
    <h4>여기 키워드 넣어주세요</h4>
    <div>
      <p> 
        총 운항횟수 
        <span style="background-color: #3D2F6B; border-radius: 70%; color: white; display: inline-block; font-weight: 400; padding: 8px 0px 7px 0px; width: 40px; height: 40px; text-align: center; top: -10px;">
          {{airline.total}}</span> 회
      </p>
      <p>
        {{ arrival.name }}으로 출발 시 지연률 
        <span style="background-color: #B9A6C9; border-radius: 70%; color: white; display: inline-block; font-weight: 400; padding: 8px 0px 7px 0px; width: 40px; height: 40px; text-align: center; top: -10px;">
          {{airline.delay_rate}}</span> %
      </p>
      <p>
        {{ arrival.name }}으로 출발 시 평균 지연시간 
        <span style="background-color: #B9A6C9; border-radius: 70%; color: white; display: inline-block; font-weight: 400; padding: 8px 0px 7px 0px; width: 40px; height: 40px; text-align: center; top: -10px;">
          {{airline.delay_time}}</span> 분
      </p>
      <p>
        오늘 예상 지연률 
        <span style="background-color: #656F8C; border-radius: 70%; color: white; display: inline-block; font-weight: 400; padding: 8px 0px 7px 0px; width: 40px; height: 40px; text-align: center; top: -10px;">
          {{airline.predicted_delay_rate}}</span> %
      </p>
    </div>
    <charts :options="delayedTimeBar" />
  </div>
</template>

<script>
export default {
  name: 'ArrivalDelayInfo',
  props: ['arrival_name', 'airline_name'],
  data () {
    return {
        delayedTimeBar: {
          chart: {
              type: 'bar',
              height: 100,
              width: 1000,
              className: 'pBar',
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
              data: [5]
          }, {
              name: '30분 초과 60분 내 출발',
              data: [2]
          }, {
              name: '60분 이상 지연',
              data: [3]
          }],
        },
      }
  },
}
</script>

<style>

</style>