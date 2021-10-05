<template>
  <div id="review-button-container">
    <button class="review-button" @click="moveToReviewForm">리뷰 작성</button>
  </div>
</template>

<script>
export default {
  name: "ReviewCreateButton",
  props: {
    airlineId: String,
    arrivalId: String,
    arrivalName: String,
  },
  data() {
    return {
      flag: 1,
    };
  },
  methods: {
    moveToReviewForm() {
      this.$router.push({
        name: "Form",
        params: {
          airlineId: this.airlineId,
          arrivalId: this.arrivalId,
          arrivalName: this.arrivalName,
          flag: this.flag,
        },
      });
    },
  },
};
</script>

<style>
#review-button-container {
  display: flex;
  justify-content: flex-start;
  margin-bottom: 10px;
}
.review-button {
  background-color: rgb(182, 168, 198);
  border: 0;
  color: white;
  width: 80px;
  height: 40px;
  border-radius: 5px;
}
.review-button:hover {
  background-color: rgba(0, 0, 0, 0.3);
  transition: 0.3s
}
</style>