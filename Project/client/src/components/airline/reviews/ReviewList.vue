<template>
  <div class="container">
    <ul>
      <li v-for="(review, idx) in reviewList" :key="idx">
        <span>{{ review.title }}</span>
        <span>{{ review.content }}</span>
        <span>{{ review.flight_at }}</span>
        <span>{{ review.seat }}</span>
        <span>{{ review.score }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios"
import API from "@/common/drf.js"

export default {
  name: "ReviewList",
  data() {
    return {
      airlineId: "",
      reviewList: [],
    }
  },
  method: {
    getReviewList: function () {
      axios({
        url: API.URL + API.ROUTES.review_list + this.airlineId + '/',
        method: 'get',
      })
      .then((res) => {
        console.log(res)
        this.reviewList.push(...res)
        console.log(this.review_list)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created: function () {
    this.airlineId = this.$route.params.airline_id
    this.arrivalId = this.$route.params.arrival_id
    this.getReviewList
  }
}

</script>

<style>
  .container {
    margin-top: 20vh;
  }
</style>

