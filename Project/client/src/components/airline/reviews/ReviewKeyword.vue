<template>
  <div class="mt-2 mb-5">
    <div v-if="isRendered" class="keyword">
      <span
        v-for="(keyword, idx) in keywordList"
        :key="idx"
        class="badge rounded-pill keyword-tag"
      >
        {{ '# ' + keyword[0] + ' ' }}
      </span>
    </div>
    <div v-else style="display: flex; justify-content: center; align-items: center; height: 24px; font-weight: bold; color: #3D2F6B; font-size: 16px;">
      상위 키워드 분석중입니다 ...
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import API from '@/common/drf.js'

export default {
  name: 'ReviewKeyword',
  props: {
    airlineId: String,
  },
  data() {
    return {
      keywordList: [],
      isRendered: false,
    }
  },
  methods: {
    getKeyword: function () {
      if (this.airlineId != undefined) {
        axios({
          url: `${API.URL}${API.ROUTES.reviewDetail}keyword/${this.airlineId}/`,
          method: 'get',
        })
        .then((res) => {
          this.keywordList = res.data.slice(0, 5)
          this.isRendered = true
        })
      }
    },
  },
  created() {
    this.getKeyword()
  },
}
</script>

<style>
.keyword {
  text-align: center;
}
.keyword-tag {
  background-color: #DAD6DD;
  color: #3D2F6B;
  font-size: 18px;
  margin-right: 1rem;
  padding: 3px 10px 3px;
}
</style>