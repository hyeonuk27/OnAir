<template>
  <div>
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
  methods: {
    moveToReviewForm() {
      this.$router.push({ name: "Form" , params: {airlineId: this.airlineId, arrivalId: this.arrivalId, arrivalName: this.arrivalName }})
    }
  } 
}
</script>

<style>
.review-button {
  background-color: #3d2f6b;
  color: white;
  margin-top: 35px;
  width: 100px;
  height: 40px;
}
</style>