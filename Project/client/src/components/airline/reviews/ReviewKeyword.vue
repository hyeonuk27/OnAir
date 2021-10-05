<template>
  <div class="mb-4">
    <div class="keyword">
      <span
        v-for="(keyword, idx) in keywordList"
        :key="idx"
        class="badge rounded-pill keyword-tag"
      >
        {{ '# ' + keyword[0] + ' ' }}
      </span>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import API from "@/common/drf.js"
export default {
  name: "ReviewKeyword",
  props: {
    airlineId: String,
  },
  data() {
    return {
      keywordList: [],
    };
  },
  methods: {
    getKeyword: function () {
        if (this.airlineId != undefined) {
        axios({
          url: `${API.URL}${API.ROUTES.reviewDetail}keyword/${this.airlineId}/`,
          method: "get",
        })
        .then((res) => {
          this.keywordList = res.data.slice(0, 5);
        })
        .catch((err) => {
          console.log(err);
        });
      }
    },
  },
  created() {
    this.getKeyword();
  },
};
</script>

<style>
.keyword {
  text-align: center;
}

.keyword-tag {
  color: #3D2F6B;
  background-color: #DAD6DD;
  font-size: 18px;
  margin-right: 1rem;
  padding: 3px 10px 3px;
}
</style>