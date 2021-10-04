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
          <div
            style="
              width: 13px;
              height: 13px;
              border-radius: 50%;
              background-color: #656f8c;
            "
          ></div>
          <div
            class="mx-4"
            style="
              width: 13px;
              height: 13px;
              border-radius: 50%;
              background-color: #656f8c;
            "
          ></div>
          <div
            style="
              width: 13px;
              height: 13px;
              border-radius: 50%;
              background-color: #656f8c;
            "
          ></div>
        </div>

        <!-- 제목 -->
        <div id="info" class="mb-3 d-flex justify-content-between">
          <div id="title" class="mb-3">
            제목 &nbsp;
            <input
              type="text"
              v-model="title"
              placeholder="제목을 입력하세요."
              size="50"
            />
          </div>
          
          <!-- 여행 출발일 -->
          <div id="date">
            출발일 &nbsp;
            <input
              type="date"
              id="start"
              name="trip-start"
              value="0000.00.00."
              v-model="flightAt"
            />
          </div>
        </div>

        <!-- 내용 -->
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
        <!-- CLASS -->
        <vs-select
          color="#B9A6C9"
          class="select-box"
          placeholder="Class"
          width="200px"
          v-model="seat"
        >
          <vs-select-item
            :key="index"
            :value="item"
            :text="item"
            v-for="(item, index) in seatList"
          />
        </vs-select>

        <!-- 전체 평점 -->
        <vs-select
          color="#B9A6C9"
          class="select-box mb-5"
          placeholder="총 평점"
          width="200px"
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
          width="200px"
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
          width="200px"
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
          width="200px"
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
          width="200px"
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
import axios from "axios";
import API from "@/common/drf.js";

export default {
  name: "Form",
  data() {
    return {
      flag: 0,
      userId: "",
      reviewId: "",
      arrivalId: "",
      arrivalName: "",
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
    };
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("token");
      const config = {
        Authorization: token,
      };
      return config;
    },
    // views.py 수정 후 확인해야 함.
    createReview: function () {
      const headers = this.setToken();

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
      };
      axios({
        url: API.URL + API.ROUTES.reviewList + this.airlineId + "/",
        method: "post",
        data,
        headers,
      })
      .then(() => {
        if (this.flag == 1) {
          this.$router.push({
            name: "Airline",
            params: { airlineId: this.airlineId, arrivalId: this.arrivalId },
          });
        }
        else {
          this.$router.push({
            name: "MyReview",
            params: { userId: this.userId },
          });
        }
      })
      .catch((err) => {
        console.log(err);
      });
    },
    updateReview: function () {
      const headers = this.setToken();

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
      };
      axios({
        url: API.URL + API.ROUTES.reviewDetail + this.reviewId + "/",
        method: "put",
        data,
        headers,
      })
      .then(() => {
        if (this.flag == 1) {
          this.$router.push({
            name: "Airline",
            params: { airlineId: this.airlineId, arrivalId: this.arrivalId },
          });
        }
        else {
          this.$router.push({
            name: "MyReview",
            params: { userId: this.userId },
          });
        }
      })
      .catch((err) => {
        console.log(err);
      });
    },
    setReview: function () {
      const headers = this.setToken();

      axios({
        url: API.URL + API.ROUTES.reviewDetail + this.reviewId,
        method: "get",
        headers,
      })
      .then((res) => {
        const review = res.data;

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
      .catch((err) => {
        console.log(err);
      });
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
      this.setReview();
    }
  },
};
</script>

<style>
.select-box {
  justify-content: center;
}

.review-form {
  display: flex;
  margin: 160px auto;
  width: 1190px;
}

#review-box {
  border: 5px solid #dad6dd;
  padding: 30px;
  width: 900px;
  height: 800px;
}

#info {
  margin-left: 40px;
  margin-right: 40px;
}

.select-box {
  width: 200px;
  margin-left: 47px;
  margin-bottom: 1rem;
}

#select-box {
  background-color: #dad6dd;
  width: 300px;
  height: 800px;
  padding-top: 330px;
}

#circles {
  margin-top: 30px;
  margin-bottom: 40px;
}

.submit {
  background-color: #3d2f6b;
  color: white;
  margin-top: 35px;
  width: 200px;
  height: 40px;
}

.disable {
  background-color: #585858;
  color: rgb(128, 128, 128);
  margin-top: 35px;
  width: 200px;
  height: 40px;
}
</style>