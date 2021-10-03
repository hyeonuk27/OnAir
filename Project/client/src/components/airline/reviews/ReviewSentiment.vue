<template>
  <div>
    <div class="progress">
      <div class="progress-bar progress-bar-animated bg-danger" 
        role="progressbar" aria-valuenow="75" 
        aria-valuemin="0" aria-valuemax="100" 
        style="width: {{ negative }}%">
      </div>
      <div class="progress-bar progress-bar-animated" 
        role="progressbar" aria-valuenow="75" 
        aria-valuemin="0" aria-valuemax="100" 
        style="width: {{ positive }}%">
      </div>
  </div>

  </div>
</template>

<script>
export default {
  name: "ReviewSentiment",
  props: {
    airlineId: String,
  },
  data() {
    return {
      positive: 0,
      negative: 0,
    }
  },
  methods: {
    getSentiment: function () {
      axios({
        url: `${API.URL}${API.ROUTES.reviewDetail}sentiment/${this.airlineId}/`,
        method: "get",
      })
      .then((res) => {
        this.positive = res.data['positive']
        this.negative = res.data['negative']
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