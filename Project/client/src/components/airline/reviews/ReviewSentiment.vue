<template>
  <div>
    <div id="bar-container" class="progress">
      <div class="progress-bar progress-bar-animated bg-danger" 
        id ="bar-negative"
        role="progressbar" aria-valuenow="75" 
        aria-valuemin="0" aria-valuemax="100" 
        :style="negative">
      </div>
      <div class="progress-bar progress-bar-animated" 
        id ="bar-positive"
        role="progressbar" aria-valuenow="75" 
        aria-valuemin="0" aria-valuemax="100" 
        :style="positive">
      </div>
  </div>

  </div>
</template>

<script>
import axios from "axios"
import API from "@/common/drf.js"

export default {
  name: "ReviewSentiment",
  props: {
    airlineId: String,
  },
  data() {
    return {
      positive: null,
      negative: null,
    }
  },
  methods: {
    getSentiment: function () {
      axios({
        url: `${API.URL}${API.ROUTES.reviewDetail}sentiment/${this.airlineId}/`,
        method: "get",
      })
      .then((res) => {
        this.positive = { width: res.data['positive']+'%'}
        this.negative = { width: res.data['negative']+'%'}
      })
      .catch((err) => {
        console.log(err)
      })
    },

  },
  created() {
    this.getSentiment()
  },
}
</script>

<style>

</style>