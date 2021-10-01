<template>
  <div>
    <ReviewKeyword/>
    <ArrivalDelayInfo/>
    <ReviewWordcloud/>
    <ReviewSentimentAnalysis/>
    <ReviewScore/>
    <ReviewScoreChart/>
    <ReviewList/>
    <ReviewCreateButton/>
  </div>
</template>

<script>

import ReviewKeyword from "@/components/airline/reviews/ReviewKeyword.vue"
import ArrivalDelayInfo from "@/components/airline/reviews/ArrivalDelayInfo.vue"
import ReviewWordcloud from "@/components/airline/reviews/ReviewWordcloud.vue"
import ReviewSentimentAnalysis from "@/components/airline/reviews/ReviewSentimentAnalysis"
import ReviewScore from "@/components/airline/reviews/ReviewScore"
import ReviewScoreChart from "@/components/airline/reviews/ReviewScoreChart"
import ReviewList from "@/components/airline/reviews/ReviewList.vue"
import ReviewCreateButton from "@/components/airline/reviews/ReviewCreateButton.vue"

export default {
  name: ReviewTab,
  components: {
    ReviewKeyword,
    ArrivalDelayInfo,
    ReviewWordcloud,
    ReviewSentimentAnalysis,
    ReviewScore,
    ReviewScoreChart,
    ReviewList,
    ReviewCreateButton,
  },
}
</script>

<style>

</style>