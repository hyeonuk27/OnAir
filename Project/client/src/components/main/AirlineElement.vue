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
      <p class="airline-element-table" style="left: 50px;"> 
        총 운항횟수 
        <span class="airline-element-table-circle" style="background-color: #3D2F6B;">
          {{airline.total}}</span> 회
      </p>
      <p class="airline-element-table" style="left: 280px;">
        지연률 
        <span class="airline-element-table-circle" style="background-color: #B9A6C9;">
          {{airline.delay_rate}}</span> %
      </p>
      <p class="airline-element-table" style="left: 417px;">
        평균 지연시간 
        <span class="airline-element-table-circle" style="background-color: #B9A6C9;">
          {{airline.delay_time}}</span> 분
      </p>
      <p class="airline-element-table" style="left: 600px;">
        오늘 예상 지연률 
        <span class="airline-element-table-circle" style="background-color: #656F8C;">
          {{airline.predicted_delay_rate}}</span> %
      </p>
    </div>
  </div>
</template>

<script>
import API from '@/common/drf.js'
import axios from 'axios'
import {mapState} from 'vuex'

export default {
  name: 'AirlineElement',
  props: {
    airline: Object,
    arrivalId: String,
  },
  methods: {
    goAirline: function () {
      if (this.token != null) {
        this.logCreate()
      }
      this.$router.push({
        name: 'Airline',
        params: {
          airlineId: this.airline.id,
          arrivalId: this.arrivalId,
        },
      })
    },
    logCreate: function () {
      axios({
        url: API.URL + API.ROUTES.createLog,
        method: 'post',
        headers: {
          Authorization: this.token,
        },
        data: {
          airline_id: this.airline.id,
          arrival_id: this.arrivalId,
        },
      }) 
    }
  },
  computed: {
    ...mapState([
      'token'
    ])
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
  height: 150px;
  margin-bottom: 20px;
  padding: 0px 40px;
  transition: 0.2s;
  width: 1000px;
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
  margin-bottom: 10px;
  width: 150px;
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
.airline-element-table {
  font-size: 15px; 
  position: absolute; 
  top: -17px;
  width: 200px; 
}
.airline-element-table-circle {
  color: white; 
  border-radius: 70%; 
  display: inline-block; 
  font-weight: 400; 
  height: 40px; 
  padding: 8px 0px 7px 0px; 
  text-align: center; 
  top: -10px;
  width: 40px !important;
}
</style>