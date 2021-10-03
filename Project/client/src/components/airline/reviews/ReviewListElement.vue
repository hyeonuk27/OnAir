<template>
  <div>
      <div class="dropdown">
        <button v-if="userId == review.user" class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
          ...
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
          <li @click="moveToReviewForm(review.id)">수정</li>
          <li @click="deleteReview(review.id)">삭제</li>
        </ul>
      </div>
      <img :src="review.userpic" alt="user-image" class="profile-image">
      <div>작성자: {{ review.username }}</div>
      <div>제목: {{ review.title }}</div>
      <div>내용: {{ review.content }}</div>
      <div>내용: {{ review.arrivalname }}</div>
      <div>출발 일자: {{ review.flight_at }}</div>
      <div>클래스: {{ review.seat }}</div>
      <div>총 평점: {{ review.score }}</div>
      <div>좌석 평점: {{ review.seat_score }}</div>
      <div>서비스 평점: {{ review.service_score }}</div>
      <div>체크인 평점: {{ review.checkin_score }}</div>
      <div>기내식 평점: {{ review.food_score }}</div>
      <hr>
  </div>
</template>

<script>
import axios from "axios"
import API from "@/common/drf.js"
import {mapState} from 'vuex'

export default {
  name: "ReviewListElement",
  props: {
    review: Object,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("token")
      const config = {
        Authorization: token,
      }
      return config
    },
    deleteReview: function (reviewId) {
      const headers = this.setToken()
      axios({
        url: API.URL + API.ROUTES.reviewDetail + reviewId,
        method: "delete",
        headers,
      })
        .then(() => {
          this.$emit("reviewListUpdate")
        })
        .catch((err) => {
          console.log(err)
        })
    },
    moveToReviewForm: function (reviewId) {
      this.$router.push({ name: "Form", params: { reviewId: reviewId } })
    },
  },
  computed: {
    ...mapState([
      'userId'
    ])
  }
}
</script>

<style>
.profile-image {
  border-radius: 70%;
  height: 50px;
  width: 50px;
}
</style>