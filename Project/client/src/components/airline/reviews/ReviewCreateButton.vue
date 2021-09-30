<template>
  <div>
    <button @click="moveToReviewCreate">리뷰 작성</button>
  </div>
</template>

<script>
export default {
  name: ReviewCreateButton,
  method: {
    moveToReviewCreate() {
      this.$router.push({ name: "ReviewCreate" })
    }
  } 
  
}
</script>

<style>

</style>