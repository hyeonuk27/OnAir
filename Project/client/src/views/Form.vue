<template>
  <div class="review-container">
    <div class="review-form">
      <div id="review-box">
        <h2 class="mb-3">리뷰 작성</h2>
        <p>목적지로 가는 여정, 이용하신 항공사에 대한 리뷰와 세부 평점을 입력해주세요.<br>
          남겨주신 리뷰는 On: Air의 리포트와 항공사의 더 나은 서비스 제공을 위해 활용될 수 있습니다.
        </p>
        <div id="circles" class="d-flex justify-content-center">
          <div style="width: 15px; height: 15px; border-radius: 50%; background-color: #656F8C;"></div>
          <div class="mx-4" style="width: 15px; height: 15px; border-radius: 50%; background-color: #656F8C;"></div>
          <div style="width: 15px; height: 15px; border-radius: 50%; background-color: #656F8C;"></div>
        </div>
        
        <!-- 제목 -->
        <div id="title" class="mb-3">
          제목 &nbsp;
          <input
            type="text"
            v-model="title"
            placeholder="제목을 입력하세요."
            size=80
          />
        </div>

        <div id="info" class="mb-3 d-flex justify-content-between">
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

          <div id="select" class="d-flex">
            <!-- 도착지 -->
            <vs-select
              color="#B9A6C9"
              class="select-box"
              placeholder="도착지"
              width="200px"
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
          </div>
        </div>
        
        <!-- 내용 -->
        <div id="content" class="mt-4">
          <textarea 
            type="text"
            v-model="content"
            placeholder="내용을 입력하세요."
            style="height: 400px; width: 750px;"
          ></textarea>
        </div>
      </div>
      
      <div id="score-box">
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
          @click="createReview"
          class="submit"
          :class="{ disable : !arrivalId || !title || !content || !flightAt || !seat || !score }" 
          :disabled="
            !arrivalId ||
            !title ||
            !content ||
            !flightAt ||
            !seat ||
            !score
          "
        >
          작성 완료
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
    };
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("token")
      const config = {
        Authorization: token,
      };
      return config;
    },
    // views.py 수정 후 확인해야 함.
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
      };
      
      console.log('이상하다')
      console.log('data')
      axios({
        url: API.URL + API.ROUTES.reviewList + this.airlineId +'/',
        method: "post",
        data,
        headers,
      })
      .then((res) => {
        console.log('여기여기')
        console.log(res.data)
        console.log('저저기')
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
      const headers = this.setToken()

      axios({
        url: API.URL + API.ROUTES.reviewDetail + this.reviewId,
        method: "get",
        headers,
      })
      .then((res) => {
        const review = res.data
        console.log('불러온다불러와')
        console.log(review)
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
  border: 5px solid #DAD6DD;
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

#score-box {
  background-color: #DAD6DD;
  width: 300px;
  height: 800px;
  padding-top: 350px;
}

#circles {
  margin-top: 30px;
  margin-bottom: 40px;
}

.submit {
  background-color: #3D2F6B;
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