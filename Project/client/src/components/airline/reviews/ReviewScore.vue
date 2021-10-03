<template>
  <div class="review-score">
    <div class="review-score-detail">
      <div class="score-title">레그룸</div>
      <div v-for="i in seat" :key="i" class="score"></div>
      <div v-for="j in 5-seat" :key="'no'+j" class="not-score"></div>
    </div>
    <div class="review-score-detail">
      <div class="score-title">서비스</div>
      <div v-for="i in service" :key="i" class="score"></div>
      <div v-for="j in 5-service" :key="'no'+j" class="not-score"></div>
    </div>
    <div class="review-score-detail">
      <div class="score-title">체크인</div>
      <div v-for="i in checkin" :key="i" class="score"></div>
      <div v-for="j in 5-checkin" :key="'no'+j" class="not-score"></div>
    </div>
    <div class="review-score-detail">
      <div class="score-title">기내식</div>
      <div v-for="i in food" :key="i" class="score"></div>
      <div v-for="j in 5-food" :key="'no'+j" class="not-score"></div>
    </div>
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
        this.seat = parseInt(res.data['seat_score'])
        this.service = parseInt(res.data['service_score'])
        this.checkin = parseInt(res.data['checkin_score'])
        this.food = parseInt(res.data['food_score'])
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
  .review-score-detail {
    display: flex;
    grid-column: 2;
    grid-row: 2;
    padding: 20px;
    align-items: center;
  }
  .score {
    background-color: #B9A6C9;
    border-radius: 70%;
    width: 20px;
    height: 20px;
    margin: 0 2px;
  }

  .not-score {
    border: 2px solid #B9A6C9;
    border-radius: 70%;
    width: 20px;
    height: 20px;
    margin: 0 2px;
  }

  .score-title {
    margin-right: 20px;
  }
</style>