<template>
  <div class="main-container">
    <div>
      <TotalDelayInfo 
      :airline_name="airline_name"
      />
      <ArrivalDelayInfo 
      :arrival_name="arrival_name"
      :airline_name="airline_name"
      />
      <AnalysisChart 
      :report="report"
      />

    </div>
  </div>
</template>

<script>
import AnalysisChart from "@/components/airline/statistics/AnalysisCharts"
import TotalDelayInfo from "@/components/airline/statistics/TotalDelayInfo"
import ArrivalDelayInfo from '@/components/airline/statistics/ArrivalDelayInfo'

export default {
  name: 'DetailTab',
  props: {
    report: Array,
  },
  components: {
    AnalysisChart,
    TotalDelayInfo,
    ArrivalDelayInfo,
  },
  data () {
    return {
      arrival_name: '',
      airline_name: '',
    }
  }
}
</script>

<style>
  .main-container {
    height: auto;
    min-height: 1000px;
  }
</style>