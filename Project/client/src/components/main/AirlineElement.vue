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
      <p style="position: absolute; font-size: 15px; left: 50px; top: -17px; width: 200px;"> 
        총 운항횟수 
        <span style="background-color: #3D2F6B; border-radius: 70%; color: white; display: inline-block; font-weight: 400; padding: 8px 0px 7px 0px; width: 40px; height: 40px; text-align: center; top: -10px;">
          {{airline.total}}</span> 회
      </p>
      <p style="position: absolute; font-size: 15px; left: 280px; top: -17px; width: 200px;">
        지연률 
        <span style="background-color: #B9A6C9; border-radius: 70%; color: white; display: inline-block; font-weight: 400; padding: 8px 0px 7px 0px; width: 40px; height: 40px; text-align: center; top: -10px;">
          {{airline.delay_rate}}</span> %
      </p>
      <p style="position: absolute; font-size: 15px; left: 417px; top: -17px; width: 200px;">
        평균 지연시간 
        <span style="background-color: #B9A6C9; border-radius: 70%; color: white; display: inline-block; font-weight: 400; padding: 8px 0px 7px 0px; width: 40px; height: 40px; text-align: center; top: -10px;">
          {{airline.delay_time}}</span> 분
      </p>
      <p style="position: absolute; font-size: 15px; left: 600px; top: -17px; width: 200px;">
        오늘 예상 지연률 
        <span style="background-color: #656F8C; border-radius: 70%; color: white; display: inline-block; font-weight: 400; padding: 8px 0px 7px 0px; width: 40px; height: 40px; text-align: center; top: -10px;">
          {{airline.predicted_delay_rate}}</span> %
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AirlineElement',
  props: ['airline', 'arrivalId'],
  methods: {
    goAirline: function () {
      this.$router.push({
        name: "Airline",
        params: {
          airlineId: this.airline.id,
          arrivalId: this.arrivalId,
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