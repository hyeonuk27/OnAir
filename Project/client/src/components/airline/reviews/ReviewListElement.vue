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
        <li class="dropdown-item" @click="moveToReviewForm(review.id)">수 정</li>
        <li class="dropdown-item" @click="deleteReview(review.id)">삭 제</li>
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
      <div class="arrival-container">
        <span class="material-icons review-material-icons">
          flight
        </span> 
        {{ review.arrivalname }}
      </div>
    </div>
    <img
      class="review-list-el-profile"
      :src="review.userpic"
      alt="user-image"
      @click="moveToMyReview(review.user)"
    />
    <div class="review-list-el-title">"{{ review.title }}"</div>
    <div class="review-list-el-content">{{ review.content }}</div>
    <div class="review-list-el-score">
      <div class="review-el-score">
        <div class="me-3">총평점</div>
        <div
          v-for="index in review.score"
          :key="index"
          class="review-score"
        ></div>
        <div
          v-for="index2 in 5 - review.score"
          :key="index2 + 'a'"
          class="review-not-score"
        ></div>
      </div>
      <div v-show="review.seat_score" class="review-el-score">
        <div class="me-3">레그룸</div>
        <div
          v-for="index in review.seat_score"
          :key="index"
          class="review-score"
        ></div>
        <div
          v-for="index2 in 5 - review.seat_score"
          :key="index2 + 'a'"
          class="review-not-score"
        ></div>
      </div>
      <div v-show="review.service_score" class="review-el-score">
        <div class="me-3">서비스</div>
        <div
          v-for="index in review.service_score"
          :key="index"
          class="review-score"
        ></div>
        <div
          v-for="index2 in 5 - review.service_score"
          :key="index2 + 'a'"
          class="review-not-score"
        ></div>
      </div>
      <div v-show="review.checkin_score" class="review-el-score">
        <div class="me-3">체크인</div>
        <div
          v-for="index in review.checkin_score"
          :key="index"
          class="review-score"
        ></div>
        <div
          v-for="index2 in 5 - review.checkin_score"
          :key="index2 + 'a'"
          class="review-not-score"
        ></div>
      </div>
      <div v-show="review.food_score" class="review-el-score">
        <div class="me-3">기내식</div>
        <div
          v-for="index in review.food_score"
          :key="index"
          class="review-score"
        ></div>
        <div
          v-for="index2 in 5 - review.food_score"
          :key="index2 + 'a'"
          class="review-not-score"
        ></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'
import API from '@/common/drf.js'
import { mapState } from 'vuex'

export default {
  name: 'ReviewListElement',
  props: {
    review: Object,
  },
  data() {
    return {
      flag: 1,
    }
  },
  methods: {
    deleteReview: function (reviewId) {
      swal({
        title: '게시글을 삭제하시겠습니까?',
        icon: 'warning',
        buttons: {
          cancel: '취소',
          confirm: {
            className: 'confirm-btn',
            text: '확인',
          },
        },
      })
      .then((isDelete) => {
        if (isDelete) {
          const headers = this.setToken()
          axios({
            url: API.URL + API.ROUTES.reviewDetail + reviewId,
            method: 'delete',
            headers,
          })
          .then(() => {
            this.$emit('reviewListUpdate')
            swal({
              title: '게시글이 삭제되었습니다.',
              icon: 'success',
              buttons: {
                confirm: {
                  text: '확인',
                  className: 'confirm-btn'
                },
              },
            })
          })
        }
      })
    },
    moveToMyReview: function (userId) {
      this.$router.push({ name: 'MyReview', params: { userId: userId } })
    },
    moveToReviewForm: function (reviewId) {
      this.$router.push({ name: 'Update', params: { reviewId: reviewId, flag: this.flag } })
    },
    setToken: function () {
      const token = localStorage.getItem('token')
      const config = {
        Authorization: token,
      }
      return config
    },
  },
  computed: {
    ...mapState(['userId']),
  },
}
</script>

<style>
.arrival-container {
  align-items: center;
  display: inline-flex; 
}

.dropdown {
  background-color: rgba(0, 0, 0, 0);
  grid-column: 4;
  grid-row: 1;
  justify-self: end;
}

.dropdown-menu {
  text-align: center;
}

.dropdown-item:hover {
  background-color: rgba(223, 223, 223, 0.904);
  transition: 0.3s;
}
.review-el-score {
  display: flex;
  grid-column: 2;
  grid-row: 2;
  padding: 5px;
}

.review-list-el {
  border: 1px solid rgba(180, 180, 180, 0.658);
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.151);
  display: grid;
  grid-auto-rows: 90px 40px 70px;
  grid-template-columns: 250px 200px 200px 350px;
  height: 290px;
  margin-bottom: 20px;
  width: 1000px;
}
.review-list-el-arrival {
  grid-column: 4;
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
.review-list-el-content {
  font-size: 15px;
  grid-column: 2;
  grid-row: 3;
  height: 139px;
  overflow: scroll;
  padding-left: 20px;
  text-align: start;
  width: 700px;
}
.review-list-el-date {
  grid-column: 2;
  grid-row: 1;
  padding: 20px;
  text-align: start;
}
.review-list-el-name {
  grid-column: 1;
  grid-row: 1;
  margin-left: 50px;
  padding: 20px;
  text-align: start;
  width: 220px;
}
.review-list-el-profile {
  border-radius: 70%;
  grid-column: 1;
  grid-row: 1;
  height: 40px;
  margin: 17px;
  width: 40px;
  cursor: pointer;
}
.review-list-el-score {
  font-size: 12px;
  grid-column: 1;
  grid-row: 2;
  padding: 15px;
  padding-top: 34px;
  text-align: start;
  margin-left: 50px;
}
.review-list-el-title {
  display: flex;
  font-size: 15px;
  font-weight: 550;
  grid-column: 2;
  grid-row: 2;
  height: 20px;
  overflow: hidden;
  padding-left: 20px;
  text-align: start;
  white-space: 100%;
  width: 700px;
}

.review-material-icons {
  font-size: 24px; 
  margin-right: 3px;
  transform: rotate(90deg);
}

.review-score {
  background-color: #b9a6c9;
  border-radius: 70%;
  height: 15px;
  margin: 1.8px;
  width: 15px;
}
.review-not-score {
  border: 2px solid #b9a6c9;
  border-radius: 70%;
  height: 15px;
  margin: 1.8px;
  width: 15px;
}
</style>