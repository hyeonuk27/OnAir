<template>
  <div class="airline-element" @click="goAirline">
    <div class="airline-element-info">
      <img 
      class="airline-element-logo"
      :src="airline.profile_url" 
      alt="">
      <span class="airline-element-name">{{airline.name}}</span>
    </div>
    <div class="airline-element-statistics">
      <span style="position: absolute; left: 50px; top: -10px">총 운항횟수 {{airline.total}}회</span>
      <span style="position: absolute; left: 300px; top: -10px">지연률 {{airline.delay_rate}}%</span>
      <span style="position: absolute; left: 427px; top: -10px">평균 지연시간 {{airline.delay_time}}분</span>
      <span style="position: absolute; left: 600px; top: -10px">오늘 예상 지연률 {{airline.predicted_delay_rate}}%</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AirlineElement',
  props: ['airline', 'arrival_id'],
  data() {
    return {

    }
  },
  methods: {
    goAirline: function () {
      this.$router.push({
        name: "Airline",
        params: {
          airline_id: this.airline.id,
          arrival_id: this.arrival_id
        },
      })
    }
  }
}
</script>

<style>
  .airline-element {
    align-items: center;
    background-color: white;
    border-radius: 10px;
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.705);
    cursor: pointer;
    display: flex;
    width: 1000px;
    height: 150px;
    margin-bottom: 20px;
    padding: 0px 40px;
    transition: 0.2s;
  }

  .airline-element:hover {
    background-color: rgba(223, 223, 223, 0.904);
  }

  .airline-element-info {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .airline-element-logo {
    width: 150px;
    margin-bottom: 10px;
  }

  .airline-element-name {
    color: rgba(0, 0, 0, 0.603);
    font-weight: 700;
  }

  .airline-element-statistics {
    color: rgba(0, 0, 0, 0.74);
    font-weight: 700;
    position: relative;
    text-align: start;
  }

  .airline-element-statistics span {
    width: 200px;
  }
</style>