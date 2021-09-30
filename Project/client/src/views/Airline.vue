<template>
  <div>
    {{arrival_id}}
    {{airline_id}}
    <AirlineInfo />
    <DetailTab />

  </div>
</template>

<script>
import AirlineInfo from "@/components/airline/statistics/AirlineInfo"
import DetailTab from '../components/airline/statistics/DetailTab'

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
      arrival_id: '',
      airline_id: '',
    }
  },
  methods: {
    getAirlineInfo: function() {
      axios({
        url: API.URL + API.ROUTES.get_airline_info,
        method: "get",
      })
        .then((res) => {
          return res
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getAirlineStatistics: function() {
      axios({
        url: API.URL + API.ROUTES.get_airline_statistics,
        method: "get",
      })
        .then((res) => {
          return res
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.arrival_id = this.$route.params.arrival_id
    this.airline_id = this.$route.params.airline_id
  }
}
</script>

<style>

</style>