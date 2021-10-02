<template>
  <div>
    <button @click="moveToReviewForm">리뷰 작성</button>
  </div>
</template>

<script>
export default {
  name: "ReviewCreateButton",
  methods: {
    moveToReviewForm() {
      this.$router.push({ name: "Form" })
    }
  } 
}
</script>

<style>

</style>