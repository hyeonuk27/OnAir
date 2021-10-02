<template>
  <div>
    <button @click="moveToReviewForm">리뷰 작성</button>
  </div>
</template>

<script>
export default {
  name: "ReviewCreateButton",
  props: {
    airlineId: String,
  },
  methods: {
    moveToReviewForm() {
      this.$router.push({ name: "Form" , params: {airlineId: this.airlineId}})
    }
  } 
}
</script>

<style>

</style>