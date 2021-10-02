<template>
  <div class="review-container">
    <div class="review-form">
      <div id="review-box">
        
        
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
            날짜 &nbsp;
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
        <button id="submit"
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
          작성 완료
        </button>
      </div>
    </div>
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
  },
  created() {
    this.airlineId = this.$route.params.airlineId
    this.getArrivals()
  },
}
</script>

<style>
.select-box {
  justify-content: center
}

.review-form {
  display: flex;
  margin: 200px auto;
  width: 1190px;
  height: 800px;
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

#submit {
  background-color: #3D2F6B;
  color: white;
  margin-top: 35px;
  width: 200px;
  height: 40px;
}
</style>