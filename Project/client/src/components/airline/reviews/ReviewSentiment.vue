<template>
  <div>
    <div id="bar-container" class="progress">
      <div
        class="progress-bar progress-bar-animated"
        id="bar-negative"
        role="progressbar"
        aria-valuenow="75"
        aria-valuemin="0"
        aria-valuemax="100"
        :style="negativeStyle"
      >
        {{ negative }}
      </div>
      <div
        class="progress-bar progress-bar-animated"
        id="bar-positive"
        role="progressbar"
        aria-valuenow="75"
        aria-valuemin="0"
        aria-valuemax="100"
        :style="positiveStyle"
      >
        {{ positive }}
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import API from "@/common/drf.js";

export default {
  name: "ReviewSentiment",
  props: {
    airlineId: String,
  },
  data() {
    return {
      positiveStyle: null,
      negativeStyle: null,
      positive: 0,
      negative: 0,
    };
  },
  methods: {
    getSentiment: function () {
      axios({
        url: `${API.URL}${API.ROUTES.reviewDetail}sentiment/${this.airlineId}/`,
        method: "get",
      })
        .then((res) => {
          this.positiveStyle = { width: res.data["positive"] + "%" };
          this.negativeStyle = { width: res.data["negative"] + "%" };
          this.positive = res.data["positive"] + "%"
          this.negative = res.data["negative"] + "%"
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getSentiment();
  },
};
</script>

<style>
#bar-container {
  height: 25px;
}
#bar-negative {
  background-color: #f7cac9;
}
#bar-positive {
  background-color: #92a8d1;
}
</style>