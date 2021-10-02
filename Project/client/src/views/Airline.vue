<template>
  <div class="airline">
    <div class="airline-container">
      {{airlineId}}
      <AirlineInfo 
      :airlineInfo="airlineInfo"
      />
      <!-- <DetailTab  -->
      <ReviewTab
      :airlineId="airlineId"
      />
    </div>
  </div>
</template>


<script>
import AirlineInfo from "@/components/airline/statistics/AirlineInfo"
// import DetailTab from '../components/airline/statistics/DetailTab'
import ReviewTab from "@/components/airline/reviews/ReviewTab"

import axios from "axios"
import API from "@/common/drf.js"

export default {
  name: 'AirlineDetail',
  components: {
    AirlineInfo,
    // DetailTab,
    ReviewTab,
  },
  data () {
    return {
      arrivalId: '',
      airlineId: '',
      airlineInfo: {},
    }
  },
  methods: {
    getAirlineStatistics: function () {
      axios({
        url: API.URL + API.ROUTES.getAirlines + this.arrivalId + '/' + this.airlineId + '/',
        method: "get",
      })
        .then((res) => {
          const report = res.data.data
          console.log(report)
          // this.report_detail = report
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getAirlineInfo: function () {
      console.log(this.airlineId)
      axios({
        url: API.URL + API.ROUTES.getAirlineInfo + this.airlineId + '/',
        method: "get",
      })
        .then((res) => {
          const airlineInfo = res.data
          this.airlineInfo = airlineInfo
          console.log(airlineInfo)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.arrivalId = this.$route.params.arrivalId
    this.airlineId = this.$route.params.airlineId
    this.getAirlineInfo()
    // this.getAirlineStatistics()
  }
}
</script>

<style>
  .airline {
    display: flex;
    justify-content: center;
    margin-top: 150px;
  }

  .airline-container {
    width: 1190px;
    min-width: 1190px;
  }
</style>