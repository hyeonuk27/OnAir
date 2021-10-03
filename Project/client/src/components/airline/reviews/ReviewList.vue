<template>
  <div class="container">
    <!-- 리뷰 리스트 -->
    <div>
      <ReviewListElement
        v-for="(review, idx) in reviewList"
        :key="idx"
        :review="review"
      />
      <vs-pagination class="my-review-pagination" :total="pageTotal" v-model="pageNum" color="#B9A6C9" @change="getReviewList"></vs-pagination>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import API from "@/common/drf.js"
import ReviewListElement from '@/components/airline/reviews/ReviewListElement'

export default {
  name: "ReviewList",
  props: {
    airlineId: String,
  },
  data() {
    return {
      pageNum: 1,
      pageTotal: 0,
      reviewList: [],
    }
  },
  components: {
    ReviewListElement
  },
  methods: {
    getReviewList: function () {
      axios({
        url: API.URL + API.ROUTES.reviewList + this.airlineId + "/",
        method: "get",
        params: {
          page: this.pageNum,
        },
      })
        .then((res) => {
          this.pageTotal = res.data[res.data.length - 1]["page_total"]
          this.reviewList = res.data.slice(0, 5)
        })
        .catch((err) => {
          console.log(err)
        })
    },

  },
  created() {
    this.getReviewList()
  },
}
</script>

<style>
.container {
  margin-top: 20vh;
}
</style>

