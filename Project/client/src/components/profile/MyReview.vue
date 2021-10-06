<template>
  <div class="my-review">
    <div class="my-review-container">
      <div>
        <img class="my-review-img" :src="profileUrl" alt="">
      </div>
      <div>
        <div v-if="reviews.length != 1" class="my-review-list">
          <MyReviewElement
            v-for="(review, idx) in reviews"
            :key="idx"
            :review="review"
            :name="name"
            @myReviewsUpdate="getMyReviews"
          />
        </div>
        <vs-pagination 
          v-if="reviews.length != 1" 
          v-model="pageNum" 
          class="my-review-pagination" 
          color="#B9A6C9" 
          :total="pageTotal" 
          @change="getMyReviews"
        ></vs-pagination>
        <div class="my-review-default" v-else>
          아직 작성하신 리뷰가 없습니다. 여행을 떠나볼까요? ✈
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import API from '@/common/drf.js'
import axios from 'axios'
import MyReviewElement from '@/components/profile/MyReviewElement'

export default {
  name: 'MyReview',
  components: {
    MyReviewElement
  },
  data() {
    return {
      name: '',
      profileUrl: '',
      pageNum: 1,
      pageTotal: 2,
      reviews: [],
      userId: '',
    }
  },
  methods: {
    getMyReviews: function () {
      axios({
        url: `${API.URL}${API.ROUTES.getMyReviews}${this.userId}/reviews/`,
        method: 'get',
        params: {
          page: this.pageNum,
        },
      })
      .then((res) => {
        this.pageTotal = res.data[res.data.length-1]['page_total']
        this.name = res.data[res.data.length-1]['user_name']
        this.profileUrl = res.data[res.data.length-1]['user_profile_url']
        this.reviews = res.data.slice(0, 5)
      })
    },
  },
  created() {
    this.userId = this.$route.params.userId
    this.getMyReviews()
  },
}
</script>

<style>
.my-review {
  display: flex;
  justify-content: center;
  margin-top: 150px;
}
.my-review-container {
  display: flex;
  justify-content: center;
  width: 1190px;
}
.my-review-default {
  border: 1px solid rgba(180, 180, 180, 0.658);
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.151);
  height: 200px;
  padding: 50px;
  width: 1000px;
}
.my-review-img {
  border-radius: 70%;
  margin-right: 50px;
  object-fit: cover;
  width: 100px;
}
.my-review-pagination {
  margin: 40px 100px 50px 0px;
}
.vs-pagination--mb {
  justify-content: center;
}
</style>