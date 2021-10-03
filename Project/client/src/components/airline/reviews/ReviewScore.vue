<template>
  <div>

  </div>
</template>

<script>
import axios from "axios"
import API from "@/common/drf.js"

export default {
  name: "ReviewScore",
  props: {
    airlineId: String,
  },
  data() {
    return {
      seat: 0,
      service: 0,
      checkin: 0,
      food: 0,
    }
  },
  methods: {
    getScore: function () {
      axios({
        url: `${API.URL}${API.ROUTES.reviewDetail}score/${this.airlineId}/`,
        method: "get",
      })
      .then((res) => {
        this.seat = res.data['seat_score']
        this.service = res.data['service_score']
        this.checkin = res.data['checkin_score']
        this.food = res.data['food_score']
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created() {
    this.getScore()
  },
}
</script>

<style>

</style>