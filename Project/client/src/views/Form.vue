<template>
  <div class="mt-5">
    <h1>리뷰 작성</h1>

    <!-- 리뷰 -->
    <input 
      type="text"
      v-model="title"
      placeholder="제목을 입력하세요."
      required
    >

    <!-- 내용 -->
    <input 
      type="text"
      v-model="content"
      placeholder="내용을 입력하세요."
      required
    >

    <!-- 여행 출발 일자 -->
    <input 
      type="date"
      id="start"
      name="trip-start" 
      value="0000.00.00."
      v-model="flightAt"
      required
    >

    <!-- 평점 -->
    <input 
      type="number"
      min="0"
      max="5"
      v-model="score"
      required
    >
    <input 
      type="number"
      min="1"
      max="5"
      v-model="seatScore"
    >
    <input 
      type="number"
      min="1"
      max="5"
      v-model="serviceScore"
    >    
    <input 
      type="number"
      min="1"
      max="5"
      v-model="checkinScore"
    >
    <input 
      type="number"
      min="1"
      max="5"
      v-model="foodScore"
    >    
    <!-- 좌석 종류 선택 -->

    <select id="seat" name="seat" v-model="selectedSeat">
      <option
        v-for="(seat, idx) in seatList"
        :key="idx"
        >
      {{seat}}
      </option>
    </select>

    <button
      @click="createReview"
    >
      작성
    </button>
  </div>

</template>

<script>
import axios from "axios"
import API from "@/common/drf.js"

export default {
  name: "Form",
  data() {
    return {
      airlineId: "",
      title: "",
      content: "",
      flightAt: "",
      selectedSeat: "",
      seatList: ['퍼스트', '비즈니스', '이코노미'],
      score: 0,
      seatScore: 0,
      serviceScore: 0,
      checkinScore: 0,
      foodScore: 0,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('token')
      const config = {
        Authorization: token
      }
      return config
    },
    createReview: function () {
      const headers = this.setToken()
      console.log('111')
      console.log(headers)

      const data = {
        airlineId: this. airlineId,
        title: this.title,
        content: this.content,
        flight_at: this.flightAt,
        seat: this.seat,
        score: this.score,
        seat_score: this.seatScore,
        service_score: this.serviceScore,
        checkin_score: this.checkinScore,
        food_score: this.foodScore
      }
      console.log(data)
      axios({
        url: API.URL + API.ROUTES.review_list + this.airlineId,
        method: 'post',
        data,
        headers,
      })
      .then(() => {
        // 추후 수정 필요
        console.log('통과')
        this.$router.push({ name: 'ReviewList' })
      })
      .catch((err) => {
        console.log(err)
        console.log('통과x')
      })
    },
  },
  created() {
    this.arrivalId = this.$route.params.arrival_id
  }
}
</script>

<style>
</style>