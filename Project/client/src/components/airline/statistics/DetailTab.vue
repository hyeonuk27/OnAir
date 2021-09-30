<template>
  <div>
    여기에 탭이 들어갑니다. 탭 안에 분석결과와 차트가 들어갑니다.
    <div>
      <TotalDelayInfo />
      <AnalysisChart />
    </div>
  </div>
</template>

<script>
import AnalysisChart from "@/components/airline/statistics/AnalysisCharts"
import TotalDelayInfo from "@/components/airline/statistics/TotalDelayInfo"

export default {
  name: 'DetailTab',
  components:     
    AnalysisChart,
    TotalDelayInfo,
}
</script>

<style>

</style>