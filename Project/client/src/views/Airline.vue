<template>
  <div>
    {{ arrival_id }}
    {{ airline_id }}
    <AirlineInfo 
    :airline_info="airline_info"
    />
    <DetailTab 
    :report="report"
    />
  </div>
</template>

<script>
import AirlineInfo from "@/components/airline/statistics/AirlineInfo"
import DetailTab from '@/components/airline/statistics/DetailTab'

import axios from "axios"
import API from "@/common/drf.js"

export default {
  name: 'AirlineDetail',
  components: {
    AirlineInfo,
    DetailTab,
  },
  data () {
    return {
      arrival_id: String,
      airline_id: String,
      report: Array,
      airline_info: Object,
    }
  },
  methods: {
    getAirlineStatistics: function () {
      axios({
        url: API.URL + API.ROUTES.get_airlines + this.arrival_id + '/' + this.airline_id + '/',
        method: "get",
      })
        .then((res) => {
          const report = res.data.data
          console.log(report)
          this.report_detail = report
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getAirlineInfo: function () {
      axios({
        url: API.URL + API.ROUTES.get_airline_info + this.airline_id + '/',
        method: "get",
      })
        .then((res) => {
          const airlineInfo = res.data
          console.log(airlineInfo)
          this.airline_info = airlineInfo
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.arrival_id = this.$route.params.arrival_id
    this.airline_id = this.$route.params.airline_id
    this.getAirlineInfo()
    this.getAirlineStatistics()
  }
}
</script>

<style>

</style>