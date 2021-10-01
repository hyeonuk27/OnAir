<template>
  <div class="container">
    <!-- 리뷰 리스트 -->
    <ul>
      <li v-for="(review, idx) in reviewList" :key="idx">
        <div>제목: {{ review.title }}</div>
        <div>내용: {{ review.content }}</div>
        <div>출발 일자: {{ review.flight_at }}</div>
        <div>클래스: {{ review.seat }}</div>
        <div>전체 평점: {{ review.score }}</div>
        <div>좌석 평점: {{ review.seat_score }}</div>
        <div>서비스 평점: {{ review.service_score }}</div>
        <div>체크인 평점: {{ review.checkin_score }}</div>
        <div>기내식 평점: {{ review.food_score }}</div>
        <hr>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios"
import API from "@/common/drf.js"

export default {
  name: "ReviewList",
  props: {
    airlineId: String,
  },  
  data() {
    return {
      reviewList: [],
    }
  },
  methods: {
    getReviewList: function () {
      axios({
        url: API.URL + API.ROUTES.review_list + this.airlineId + '/',
        method: 'get',
      })
      .then((res) => {
        console.log('저기')
        console.log(res)
        this.reviewList = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created () {
    this.getReviewList()
  }
}

</script>

<style>
  .container {
    margin-top: 20vh;
  }
</style>

