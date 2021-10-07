<template>
  <div id="review-list-container">
    <div
      v-if="isRendered"
    >
      <ReviewListElement
        v-for="(review, idx) in reviewList"
        :key="idx"
        :review="review"
        @reviewListUpdate="getReviewList"
      />
      <vs-pagination
        class="review-list-pagination"
        :total="pageTotal"
        v-model="pageNum"
        color="#B9A6C9"
        @change="getReviewList"
      ></vs-pagination>
    </div>
    <div v-else style="display: flex; justify-content: center; align-items: center; height: 200px; font-weight: bold; color: #3D2F6B;">
      리뷰 로딩중입니다 ...
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import API from '@/common/drf.js'
import ReviewListElement from '@/components/airline/reviews/ReviewListElement'

export default {
  name: 'ReviewList',
  components: {
    ReviewListElement,
  },
  props: {
    airlineId: String,
  },
  data() {
    return {
      pageNum: 1,
      pageTotal: 0,
      reviewList: [],
      isRendered: false,
    }
  },
  methods: {
    getReviewList: function () {
      axios({
        url: `${API.URL}${API.ROUTES.reviewList}${this.airlineId}/`,
        method: 'get',
        params: {
          page: this.pageNum,
        },
      })
      .then((res) => {
        this.pageTotal = res.data[res.data.length - 1]['page_total']
        this.reviewList = res.data.slice(0, 5)
        this.isRendered = true
      })
    },
  },
  created() {
    this.getReviewList()
  },
}
</script>

<style>
#review-list-container {
  height: 100%;
}
.review-list-pagination {
  display: flex;
  justify-content: center;
  margin: 40px 100px 50px 0px;
}
.vs-pagination--mb {
  display: flex;
  justify-content: center !important;
}
</style>

