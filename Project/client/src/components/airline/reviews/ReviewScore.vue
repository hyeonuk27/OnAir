<template>
  <div>
    <p class="review-score-title">평점 상세</p>
    <div class="review-score-detail">
      <div class="score-title">총평점</div>
      <div v-for="i in total" :key="i" class="score"></div>
      <div v-for="j in 5 - total" :key="'no' + j" class="not-score"></div>
    </div>
    <div class="review-score-detail">
      <div class="score-title">레그룸</div>
      <div v-for="i in seat" :key="i" class="score"></div>
      <div v-for="j in 5 - seat" :key="'no' + j" class="not-score"></div>
    </div>
    <div class="review-score-detail">
      <div class="score-title">서비스</div>
      <div v-for="i in service" :key="i" class="score"></div>
      <div v-for="j in 5 - service" :key="'no' + j" class="not-score"></div>
    </div>
    <div class="review-score-detail">
      <div class="score-title">체크인</div>
      <div v-for="i in checkin" :key="i" class="score"></div>
      <div v-for="j in 5 - checkin" :key="'no' + j" class="not-score"></div>
    </div>
    <div class="review-score-detail">
      <div class="score-title">기내식</div>
      <div v-for="i in food" :key="i" class="score"></div>
      <div v-for="j in 5 - food" :key="'no' + j" class="not-score"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import API from '@/common/drf.js'

export default {
  name: 'ReviewScore',
  props: {
    airlineId: String,
  },
  data() {
    return {
      total: 0,
      checkin: 0,
      food: 0,
      seat: 0,
      service: 0,
    }
  },
  methods: {
    getScore: function () {
      axios({
        url: `${API.URL}${API.ROUTES.reviewDetail}score/${this.airlineId}/`,
        method: 'get',
      })
      .then((res) => {
        this.total = parseInt(res.data['score'])
        this.seat = parseInt(res.data['seat_score'])
        this.service = parseInt(res.data['service_score'])
        this.checkin = parseInt(res.data['checkin_score'])
        this.food = parseInt(res.data['food_score'])
      })
    },
  },
  created() {
    this.getScore()
  },
}
</script>

<style>
.not-score {
  border: 2px solid #b9a6c9;
  border-radius: 70%;
  height: 20px;
  margin: 0 2px;
  width: 20px;
}
.review-score-detail {
  align-items: center;
  display: flex;
  grid-column: 2;
  grid-row: 2;
  padding: 10px;
}
.review-score-title {
  font-weight: bold;
  margin-bottom: 18px;
  color: #3D2F6B;
  font-size: 17px;
}
.score {
  background-color: #b9a6c9;
  border-radius: 70%;
  height: 20px;
  margin: 0 2px;
  width: 20px;
}
.score-title {
  margin-right: 20px;
  font-weight: bold;
}
</style>