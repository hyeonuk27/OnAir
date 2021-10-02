<template>
  <div class="container">
    <!-- 리뷰 리스트 -->
    <ul>
      <li v-for="(review, idx) in reviewList" :key="idx">
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
            ...
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
            <li @click="moveToReviewForm(review.id)">수정</li>
            <li @click="deleteReview(review.id)">삭제</li>
          </ul>
        </div>
        <div>유저: {{ review.user }}</div>
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
      reviewer: "",
      reviewId: "",
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
    getReviewList: function () {
      axios({
        url: API.URL + API.ROUTES.reviewList + this.airlineId + '/',
        method: 'get',
      })
      .then((res) => {
        this.reviewList = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 요청은 들어가나 요청한 사람 == 작성한 사람 일 때만 삭제가 되어서 문제..
    deleteReview: function (reviewId) {
      const headers = this.setToken()
      axios({
        url: API.URL + API.ROUTES.reviewDetail + reviewId,
        method: 'delete',
        headers
      })
      .then(() => {
        this.getReviewList()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    moveToReviewForm: function (reviewId) {
      this.$router.push({ name: "Form" , params: {reviewId: reviewId}})
    }
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

