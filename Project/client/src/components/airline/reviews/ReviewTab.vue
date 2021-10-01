<template>
  <div>
    <ReviewKeyword/>
    <ArrivalDelayInfo/>
    <ReviewWordcloud/>
    <ReviewSentiment/>
    <ReviewScore/>
    <ReviewScoreChart/>
    <ReviewCreateButton/>
    <ReviewList/>
  </div>
</template>

<script>

import ReviewKeyword from "@/components/airline/reviews/ReviewKeyword"
import ArrivalDelayInfo from "@/components/airline/reviews/ArrivalDelayInfo"
import ReviewWordcloud from "@/components/airline/reviews/ReviewWordcloud"
import ReviewSentiment from "@/components/airline/reviews/ReviewSentiment"
import ReviewScore from "@/components/airline/reviews/ReviewScore"
import ReviewScoreChart from "@/components/airline/reviews/ReviewScoreChart"
import ReviewCreateButton from "@/components/airline/reviews/ReviewCreateButton"
import ReviewList from "@/components/airline/reviews/ReviewList"

export default {
  name: "ReviewTab",
  components: {
    ReviewKeyword,
    ArrivalDelayInfo,
    ReviewWordcloud,
    ReviewSentiment,
    ReviewScore,
    ReviewScoreChart,
    ReviewCreateButton,
    ReviewList,
  },
}
</script>

<style>

</style>