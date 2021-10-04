<template>
  <div class="my-review-el" @click="goAirline">
    <div class="my-review-el-name">
      <div>NAME OF PASSENGER</div>
      {{name}}
    </div>
    <div class="my-review-el-date">
      <div>DATE</div>
      {{review.flight_at}}
    </div>
    <div class="my-review-el-seat">
      <div>SEAT</div>
      {{review.seat}}
    </div>
    <div class="my-review-el-airline">
      <div>AIRLINE</div>
      {{review.airline_name}}
    </div>
    <div class="my-review-el-img">
      <span style="font-size: 30px;">ICN <span style="transform: rotate(90deg);" class="material-icons">flight</span> {{review.arrival_name.substring(0, 3)}}</span>
    </div>
    <div class="my-review-el-score">
      <div v-for="index in review.score" :key="index" class="my-review-score"></div>
      <div v-for="index2 in 5-review.score" :key="index2+'a'" class="my-review-not-score"></div>
    </div>
    <div class="my-review-el-content">
      <div>{{review.content}}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyReviewElement',
  props: ['review', 'name'],
  methods: {
    goAirline: function () {
      this.$router.push({
        name: "Airline",
        params: {
          airlineId: this.review.airline,
          arrivalId: this.review.arrival,
        },
      })
    },
  }
}
</script>

<style>
  .my-review-el {
    border: 1px solid rgba(180, 180, 180, 0.658);
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.151);
    cursor: pointer;
    display: grid;
    grid-template-columns: 250px 200px 200px 350px;
    grid-auto-rows: 90px 40px 70px;
    width: 1000px;
    height: 200px;
    margin-bottom: 20px;
    transition: 0.2s;
  }

  .my-review-el:hover {
    background-color: rgba(223, 223, 223, 0.904);
  }

  .my-review-el-name {
    grid-column: 1;
    grid-row: 1;
    padding: 20px;
    text-align: start;
  }

  .my-review-el-date {
    grid-column: 2;
    grid-row: 1;
    padding: 20px;
    text-align: start;
  }

  .my-review-el-seat {
    grid-column: 3;
    grid-row: 1;
    padding: 20px;
    text-align: start;
  }

  .my-review-el-airline {
    grid-column: 4;
    grid-row: 1;
    padding: 20px;
    text-align: start;
  }

  .my-review-el-img {
    grid-column: 1;
    grid-row: 2 / 3;
    padding: 20px;
    text-align: start;
  }

  .my-review-el-score {
    display: flex;
    grid-column: 2;
    grid-row: 2;
    padding: 20px;
  }

  .my-review-el-content {
    grid-column: 2 / 5;
    grid-row: 3;
    padding: 20px;
    text-align: start;
  }

  .my-review-el-content div {
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    width: 600px;
  }

  .my-review-score {
    background-color: #B9A6C9;
    border-radius: 70%;
    width: 20px;
    height: 20px;
    margin: 0 2px;
  }

  .my-review-not-score {
    border: 2px solid #B9A6C9;
    border-radius: 70%;
    width: 20px;
    height: 20px;
    margin: 0 2px;
  }
</style>