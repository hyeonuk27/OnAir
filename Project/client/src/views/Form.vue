<template>
  <div class="review-container">
    <div class="review-form">
      <div id="review-box">
        <h2 class="mb-3">리뷰</h2>
        <p>
          목적지로 가는 여정, 이용하신 항공사에 대한 리뷰와 세부 평점을
          입력해주세요.<br />
          남겨주신 리뷰는 On: Air의 리포트와 항공사의 더 나은 서비스 제공을 위해
          활용될 수 있습니다.
        </p>
        <div style="color: #656F8C;">도착지 ✈ {{arrivalName}}</div>
        <div id="circles" class="d-flex justify-content-center">
          <div class="review-circle"></div>
          <div class="mx-4 review-circle"></div>
          <div class="review-circle"></div>
        </div>
        <div id="info" class="mb-3 d-flex justify-content-between text-start">
          <div id="title" class="mb-3">
            <vs-input
              type="text"
              label="제목"
              v-model="title"
              placeholder="제목을 입력하세요."
              style="width:500px;"
            />
          </div>
          <div id="date">
            <vs-input
              type="date"
              label="출발일"
              id="start"
              name="trip-start"
              value="0000.00.00."
              v-model="flightAt"
            />
          </div>
        </div>
        <div id="content" class="mt-4">
          <textarea
            type="text"
            v-model="content"
            placeholder="내용을 입력하세요."
            style="height: 400px; width: 750px"
          ></textarea>
        </div>
      </div>

      <div id="select-box">
        <vs-select
          color="#B9A6C9"
          class="select-box review-form-select"
          placeholder="선택해주세요."
          width="200px"
          v-model="seat"
          label="클래스"
        >
          <vs-select-item
            :key="index"
            :value="item"
            :text="item"
            v-for="(item, index) in seatList"
          />
        </vs-select>

        <vs-select
          color="#B9A6C9"
          class="select-box review-form-select mb-5"
          placeholder="선택해주세요."
          width="200px"
          v-model="score"
          label="총 평점"
        >
          <vs-select-item
            :key="index"
            :value="item"
            :text="item"
            v-for="(item, index) in scoreList"
          />
        </vs-select>

        <vs-select
          color="#B9A6C9"
          class="select-box review-form-select"
          placeholder="선택해주세요."
          width="200px"
          v-model="seatScore"
          label="레그룸 평점"
        >
          <vs-select-item
            :key="index"
            :value="item"
            :text="item"
            v-for="(item, index) in scoreList"
          />
        </vs-select>

        <vs-select
          color="#B9A6C9"
          class="select-box review-form-select"
          placeholder="선택해주세요."
          width="200px"
          v-model="serviceScore"
          label="서비스 평점"
        >
          <vs-select-item
            :key="index"
            :value="item"
            :text="item"
            v-for="(item, index) in scoreList"
          />
        </vs-select>

        <vs-select
          color="#B9A6C9"
          class="select-box review-form-select"
          placeholder="선택해주세요."
          width="200px"
          v-model="checkinScore"
          label="체크인 평점"
        >
          <vs-select-item
            :key="index"
            :value="item"
            :text="item"
            v-for="(item, index) in scoreList"
          />
        </vs-select>

        <vs-select
          color="#B9A6C9"
          class="select-box review-form-select"
          placeholder="선택해주세요."
          width="200px"
          v-model="foodScore"
          label="기내식 평점"
        >
          <vs-select-item
            :key="index"
            :value="item"
            :text="item"
            v-for="(item, index) in scoreList"
          />
        </vs-select>

        <button
          v-if="this.$route.name === 'Form'"
          @click="createReview"
          class="submit"
          :class="{
            disable:
              !arrivalId || !title || !content || !flightAt || !seat || !score,
          }"
          :disabled="
            !arrivalId || !title || !content || !flightAt || !seat || !score
          "
        >
          작성 완료
        </button>
        <button
          v-else
          @click="updateReview"
          class="submit"
          :class="{
            disable:
              !arrivalId || !title || !content || !flightAt || !seat || !score,
          }"
          :disabled="
            !arrivalId || !title || !content || !flightAt || !seat || !score
          "
        >
          수정 완료
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import API from '@/common/drf.js'

export default {
  name: 'Form',
  data() {
    return {
      flag: 0,
      userId: '',
      reviewId: '',
      arrivalId: '',
      arrivalName: '',
      airlineId: '',
      title: '',
      content: '',
      flightAt: '',
      seat: '',
      score: 0,
      seatScore: 0,
      serviceScore: 0,
      checkinScore: 0,
      foodScore: 0,
      scoreList: [1, 2, 3, 4, 5],
      arrivalList: [],
      seatList: ['퍼스트', '비즈니스', '이코노미'],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('token')
      const config = {
        Authorization: token,
      }
      return config
    },
    createReview: function () {
      const headers = this.setToken()
      const data = {
        arrival: this.arrivalId,
        airline_id: this.airlineId,
        title: this.title,
        content: this.content,
        flight_at: this.flightAt,
        seat: this.seat,
        score: this.score,
        seat_score: this.seatScore,
        service_score: this.serviceScore,
        checkin_score: this.checkinScore,
        food_score: this.foodScore,
      }
      axios({
        url: `${API.URL}${API.ROUTES.reviewList}${this.airlineId}/`,
        method: 'post',
        data,
        headers,
      })
      .then(() => {
        if (this.flag == 1) {
          this.$router.push({
            name: 'Airline',
            params: { airlineId: this.airlineId, arrivalId: this.arrivalId },
          })
        }
        else {
          this.$router.push({
            name: 'MyReview',
            params: { userId: this.userId },
          })
        }
      })
    },
    updateReview: function () {
      const headers = this.setToken()
      const data = {
        arrival: this.arrivalId,
        airline_id: this.airlineId,
        title: this.title,
        content: this.content,
        flight_at: this.flightAt,
        seat: this.seat,
        score: this.score,
        seat_score: this.seatScore,
        service_score: this.serviceScore,
        checkin_score: this.checkinScore,
        food_score: this.foodScore,
      }
      axios({
        url: `${API.URL}${API.ROUTES.reviewDetail}${this.reviewId}/`,
        method: 'put',
        data,
        headers,
      })
      .then(() => {
        if (this.flag == 1) {
          this.$router.push({
            name: 'Airline',
            params: { airlineId: this.airlineId, arrivalId: this.arrivalId },
          });
        }
        else {
          this.$router.push({
            name: 'MyReview',
            params: { userId: this.userId },
          })
        }
      })
    },
    setReview: function () {
      const headers = this.setToken()
      axios({
        url: API.URL + API.ROUTES.reviewDetail + this.reviewId,
        method: 'get',
        headers,
      })
      .then((res) => {
        const review = res.data
        this.reviewId = review.id,
        this.arrivalId = review.arrival,
        this.airlineId = review.airline,
        this.title = review.title,
        this.content = review.content,
        this.flightAt = review.flight_at,
        this.seat = review.seat,
        this.score = review.score,
        this.seatScore = review.seat_score,
        this.serviceScore = review.service_score,
        this.checkinScore = review.checkin_score,
        this.foodScore = review.food_score
      })
    },
  },
  created() {
    this.userId = this.$route.params.userId
    this.flag = this.$route.params.flag
    this.arrivalName = this.$route.params.arrivalName
    this.arrivalId = this.$route.params.arrivalId
    this.airlineId = this.$route.params.airlineId
    this.reviewId = this.$route.params.reviewId
    if (this.reviewId) {
      this.setReview()
    }
  },
}
</script>

<style>
#circles {
  margin-bottom: 40px;
  margin-top: 30px;
}
.disable {
  background-color: #585858;
  color: rgb(128, 128, 128);
  height: 40px;
  margin-left: 47px;
  margin-top: 20px;
  width: 200px;
}
#info {
  margin-left: 40px;
  margin-right: 40px;
}
#review-box {
  border: 5px solid #dad6dd;
  height: 800px;
  padding: 30px;
  width: 900px;
}
.review-circle {
  background-color: #656f8c;
  border-radius: 50%;
  height: 13px;
  width: 13px;
}
.review-form {
  display: flex;
  margin: 160px auto;
  width: 1190px;
}
.review-form-select {
  justify-content: center;
  margin-bottom: 10px;
  margin-left: 47px;
  width: 200px;
}
#select-box {
  background-color: #dad6dd;
  height: 800px;
  padding-top: 230px;
  text-align: left;
  width: 300px;
}
.submit {
  background-color: #3d2f6b;
  color: white;
  height: 40px;
  margin-left: 47px;
  margin-top: 20px;
  width: 200px;
}
</style>