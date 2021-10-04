<template>
  <div id="review-button-container">
    <vs-button 
      color="rgba(182,168,198)" 
      border 
      @click="moveToReviewForm"
    >
    리뷰 작성
    </vs-button>
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
      this.$router.push({
        name: "Form",
        params: {
          airlineId: this.airlineId,
          arrivalId: this.arrivalId,
          arrivalName: this.arrivalName,
        },
      });
    },
  },
};
</script>

<style>
#review-button-container {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 10px;
}
</style>