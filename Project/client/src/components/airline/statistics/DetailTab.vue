<template>
  <div class="main-container">
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
  props: {
    // report: Array,
  },
  components: {
    AnalysisChart,
    TotalDelayInfo,
  },

}
</script>

<style>
  .main-container {
    height: auto;
    min-height: 1000px;
  }
</style>