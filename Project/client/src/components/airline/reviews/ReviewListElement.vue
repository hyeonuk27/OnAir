<template>
  <div class="review-list-el">
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
        <li @click="moveToReviewForm(review.id)">수정</li>
        <li @click="deleteReview(review.id)">삭제</li>
      </ul>
    </div>
    <div class="review-list-el-name">
      <div>NAME OF PASSENGER</div>
      {{ review.username }}
    </div>
    <div class="review-list-el-date">
      <div>DATE</div>
      {{ review.flight_at }}
    </div>
    <div class="review-list-el-class">
      <div>CLASS</div>
      {{ review.seat }}
    </div>
    <div class="review-list-el-arrival">
      <div>ARRIVAL</div>
      ✈ {{ review.arrivalname }}
    </div>
    <img
      class="review-list-el-profile"
      :src="review.userpic"
      alt="user-image"
    />
    <div class="review-list-el-title">"{{ review.title }}"</div>
    <div class="review-list-el-content">{{ review.content }}</div>
    <div class="review-list-el-score">
      <div>TOTAL <div>{{ review.score }}</div></div>
      <div>SEAT <div>{{ review.seat_score }}</div></div>
      <div>SERVICE <div>{{ review.service_score }}</div></div>
      <div>CHECKIN <div>{{ review.checkin_score }}</div></div>
      <div>FOOD <div>{{ review.food_score }}</div></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import API from "@/common/drf.js";
import { mapState } from "vuex";

export default {
  name: "ReviewListElement",
  props: {
    review: Object,
  },
  methods: {
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
          this.$emit("reviewListUpdate");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    moveToReviewForm: function (reviewId) {
      this.$router.push({ name: "Form", params: { reviewId: reviewId } });
    },
  },
  computed: {
    ...mapState(["userId"]),
  },
};
</script>

<style>
.review-list-el {
  border: 1px solid rgba(180, 180, 180, 0.658);
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.151);
  display: grid;
  grid-template-columns: 250px 200px 200px 350px;
  grid-auto-rows: 90px 40px 70px;
  width: 1000px;
  height: 300px;
  margin-bottom: 20px;
}

.review-list-el-name {
  grid-column: 1;
  grid-row: 1;
  padding: 20px;
  text-align: start;
  margin-left: 50px;
  width: 220px;
}

.review-list-el-profile {
  grid-column: 1;
  grid-row: 1;
  margin: 17px;
  margin-top: 25px;
  border-radius: 70%;
  height: 40px;
  width: 40px;
}

.review-list-el-date {
  grid-column: 2;
  grid-row: 1;
  padding: 20px;
  text-align: start;
}

.review-list-el-class {
  grid-column: 3;
  grid-row: 1;
  padding: 20px;
  text-align: start;
}

.review-list-el-arrival {
  grid-column: 4;
  grid-row: 1;
  padding: 20px;
  text-align: start;
}

.dropdown {
  grid-column: 4;
  grid-row: 1;
  justify-self: end;
  background-color: rgba(0, 0, 0, 0);
}

.review-list-el-title {
  padding-left: 20px;
  display: flex;
  grid-column: 2;
  grid-row: 2;
  font-weight: 550;
  text-align: start;
  white-space: 100%;
  font-size: 15px;
  overflow: hidden;
  width: 680px;
  height: 20px;
}

.review-list-el-content {
  padding-left: 20px;
  grid-column: 2;
  grid-row: 3;
  text-align: start;
  font-size: 15px;
  overflow: hidden;
  width: 680px;
  height: 139px;
}

.review-list-el-score {
  grid-column: 1;
  grid-row: 2;
  padding: 20px;
  text-align: start;
  font-size: 12px;
}
</style>