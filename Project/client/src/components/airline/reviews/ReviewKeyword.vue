<template>
  <div class="mb-4">
    <div class="keyword">
      <span
        v-for="keyword in keywordList"
        :key="keyword"
        class="badge keyword-tag"
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
    },
  },
  created() {
    this.getKeyword();
  },
};
</script>

<style>
.keyword {
  color: #3D2F6B;
  text-align: center;
}

.keyword-tag {
  background-color: #DAD6DD;
  margin-right: 1rem;
  padding: 1px 8px 1px;
}
</style>