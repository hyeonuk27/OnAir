<template>
  <div class="my-review-el">
    <div class="dropdown">
      <button
        v-if="userId == review.user"
        class="btn btn-sm dropdown-toggle"
        type="button"
        id="dropdownMenuButton1"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        ...
      </button>
      <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
        <li class="dropdown-item" @click="goAirline">이 동</li>
        <li class="dropdown-item" @click="moveToReviewForm(review.id)">수 정</li>
        <li class="dropdown-item" @click="deleteReview(review.id)">삭 제</li>
      </ul>
    </div>
    <div class="my-review-el-name">
      <div>NAME OF PASSENGER</div>
      {{name}}
    </div>
    <div class="my-review-el-date">
      <div>DATE</div>
      {{review.flight_at}}
    </div>
    <div class="my-review-el-seat">
      <div>SEAT</div>
      {{review.seat}}
    </div>
    <div class="my-review-el-airline">
      <div>AIRLINE</div>
      {{review.airline_name}}
    </div>
    <div class="my-review-el-img">
      <span style="font-size: 30px;">ICN <span style="transform: rotate(90deg);" class="material-icons">flight</span> {{review.arrival_name.substring(0, 3)}}</span>
    </div>
    <div class="my-review-el-score">
      <div v-for="index in review.score" :key="index" class="my-review-score"></div>
      <div v-for="index2 in 5-review.score" :key="index2+'a'" class="my-review-not-score"></div>
    </div>
    <div class="my-review-el-content">
      <div>{{review.content}}</div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import API from "@/common/drf.js";
import { mapState } from 'vuex';

export default {
  name: 'MyReviewElement',
  props: ['review', 'name'],
  data() {
    return {
      flag: 0,
    }
  },
  methods: {
    goAirline: function () {
      this.$router.push({
        name: "Airline",
        params: {
          airlineId: this.review.airline,
          arrivalId: this.review.arrival,
        },
      })
    },
    setToken: function () {
      const token = localStorage.getItem("token");
      const config = {
        Authorization: token,
      };
      return config;
    },
    deleteReview: function (reviewId) {
      const headers = this.setToken();
      axios({
        url: API.URL + API.ROUTES.reviewDetail + reviewId,
        method: "delete",
        headers,
      })
      .then(() => {
        this.$emit("myReviewsUpdate");
      })
      .catch((err) => {
        console.log(err);
      });
    },
    moveToReviewForm: function (reviewId) {
      this.$router.push({ name: "Form", params: { reviewId: reviewId, flag: this.flag, userId: this.userId  } });
    },
  },
  computed: {
    ...mapState(["userId"]),
  },
}
</script>

<style>
  .dropdown {
    grid-column: 4;
    grid-row: 1;
    justify-self: end;
    background-color: rgba(0, 0, 0, 0);
  }

  .dropdown-item:hover {
    background-color: rgba(223, 223, 223, 0.904);
    transition: 0.3s
  }

  .dropdown-menu {
    text-align: center;
  }

  .my-review-el {
    border: 1px solid rgba(180, 180, 180, 0.658);
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.151);
    cursor: pointer;
    display: grid;
    grid-template-columns: 250px 200px 200px 350px;
    grid-auto-rows: 90px 40px 70px;
    width: 1000px;
    height: 200px;
    margin-bottom: 20px;
    transition: 0.2s;
  }

  .my-review-el:hover {
    background-color: rgba(223, 223, 223, 0.904);
  }

  .my-review-el-name {
    grid-column: 1;
    grid-row: 1;
    padding: 20px;
    text-align: start;
  }

  .my-review-el-date {
    grid-column: 2;
    grid-row: 1;
    padding: 20px;
    text-align: start;
  }

  .my-review-el-seat {
    grid-column: 3;
    grid-row: 1;
    padding: 20px;
    text-align: start;
  }

  .my-review-el-airline {
    grid-column: 4;
    grid-row: 1;
    padding: 20px;
    text-align: start;
  }

  .my-review-el-img {
    grid-column: 1;
    grid-row: 2 / 3;
    padding: 20px;
    text-align: start;
  }

  .my-review-el-score {
    display: flex;
    grid-column: 2;
    grid-row: 2;
    padding: 20px;
  }

  .my-review-el-content {
    grid-column: 2 / 5;
    grid-row: 3;
    padding: 20px;
    text-align: start;
  }

  .my-review-el-content div {
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    width: 600px;
  }

  .my-review-score {
    background-color: #B9A6C9;
    border-radius: 70%;
    width: 20px;
    height: 20px;
    margin: 0 2px;
  }

  .my-review-not-score {
    border: 2px solid #B9A6C9;
    border-radius: 70%;
    width: 20px;
    height: 20px;
    margin: 0 2px;
  }
</style>