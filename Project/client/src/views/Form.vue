<template>
  <div style="margin-top: 250px;">
    <h1>리뷰 작성</h1>

    <!-- 제목 -->
    <input
      type="text"
      v-model="title"
      placeholder="제목을 입력하세요."
    />

    <!-- 내용 -->
    <input
      type="text"
      v-model="content"
      placeholder="내용을 입력하세요."
    />

    <!-- 도착지 -->
    <vs-select
      color="#B9A6C9"
      class="select-box"
      placeholder="도착지"
      width="150px"
      v-model="arrivalId"
    >
      <vs-select-item
        :key="index"
        :value="item.id"
        :text="item.text"
        v-for="(item, index) in arrivalList"
      />
    </vs-select>

    <!-- CLASS -->
    <vs-select
      color="#B9A6C9"
      class="select-box"
      placeholder="Class"
      width="150px"
      v-model="seat"
    >
      <vs-select-item
        :key="index"
        :value="item"
        :text="item"
        v-for="(item, index) in seatList"
      />
    </vs-select>

    <!-- 여행 출발일 -->
    <input
      type="date"
      id="start"
      name="trip-start"
      value="0000.00.00."
      v-model="flightAt"
    />

    <!-- 전체 평점 -->
    <vs-select
      color="#B9A6C9"
      class="select-box"
      placeholder="총 평점"
      width="150px"
      v-model="score"
    >
      <vs-select-item
        :key="index"
        :value="item"
        :text="item"
        v-for="(item, index) in scoreList"
      />
    </vs-select>

    <!-- 좌석 평점 -->
    <vs-select
      color="#B9A6C9"
      class="select-box"
      placeholder="좌석 평점"
      width="150px"
      v-model="seatScore"
    >
      <vs-select-item
        :key="index"
        :value="item"
        :text="item"
        v-for="(item, index) in scoreList"
      />
    </vs-select>

    <!-- 서비스 평점 -->
    <vs-select
      color="#B9A6C9"
      class="select-box"
      placeholder="서비스 평점"
      width="150px"
      v-model="serviceScore"
    >
      <vs-select-item
        :key="index"
        :value="item"
        :text="item"
        v-for="(item, index) in scoreList"
      />
    </vs-select>

    <!-- 체크인 평점 -->
    <vs-select
      color="#B9A6C9"
      class="select-box"
      placeholder="체크인 평점"
      width="150px"
      v-model="checkinScore"
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
      class="select-box"
      placeholder="기내식 평점"
      width="150px"
      v-model="foodScore"
    >
      <vs-select-item
        :key="index"
        :value="item"
        :text="item"
        v-for="(item, index) in scoreList"
      />
    </vs-select>

    <!-- 필수 항목 모두 입력 시 버튼 활성화 -->
    <button
      @click="createReview"
      :disabled="
        !arrivalId ||
        !title ||
        !content ||
        !flightAt ||
        !seat ||
        !score
      "
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
      reviewId: "",
      arrivalId: "",
      airlineId: "",
      title: "",
      content: "",
      flightAt: "",
      seat: "",
      score: 0,
      seatScore: 0,
      serviceScore: 0,
      checkinScore: 0,
      foodScore: 0,
      scoreList: [1, 2, 3, 4, 5],
      arrivalList: [],
      seatList: ["퍼스트", "비즈니스", "이코노미"],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("token")
      const config = {
        Authorization: token,
      }
      return config
    },
    createReview: function () {
      const headers = this.setToken()

      const data = {
        arrival_id: this.arrivalId,
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
        url: API.URL + API.ROUTES.reviewList + this.airlineId,
        method: "post",
        data,
        headers,
      })
      .then(() => {
        this.$router.push({ name: "Airline", params: {airlineId: this.airlineId, arrivalId:this.arrivalId} })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getArrivals: function () {
      axios({
        url: API.URL + API.ROUTES.getArrivals,
        method: "get",
      })
      .then((res) => {
        const arrivals = res.data
        arrivals.sort(function (a, b) {
          if (a.name[4] > b.name[4]) {
            return 1
          } else if (a.name[4] < b.name[4]) {
            return -1
          }
          return 0
        })
        for (let i = 0; i < arrivals.length; i++) {
          this.arrivalList.push({
            id: arrivals[i].id,
            text: arrivals[i].name,
            value: i + 1,
          })
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    setReview: function () {
      axios({
        url: API.URL + API.ROUTES.reviewDetail + this.reviewId,
        method: "get",
      })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log('실패')
        console.log(err)
      })
    }
  },
  created() {
    this.airlineId = this.$route.params.airlineId
    this.reviewId = this.$route.params.reviewId
    this.getArrivals()
    if (this.reviewId) {
      this.setReview()
    }
  },
}
</script>

<style>
.select-box {
  justify-content: center
}
</style>