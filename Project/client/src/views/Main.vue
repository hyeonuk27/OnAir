<template>
  <div class='main' :style="{backgroundImage: 'linear-gradient( rgba(0, 0, 0, 0.08), rgba(0, 0, 0, 0.08) ), url('+ bgImg +')'}">
    <!-- <img class="main-img" src="@/assets/main.jpg" alt=""> -->
    <div class="main-container">
      <div class="arrival-info">
        <span>
          {{departure}}
        </span>
        <span style="margin-top: 250px; margin-left: 350px;">
          {{arrival}}
        </span>
      </div>
      <div class="search-box">
        <Search
        v-if="isRendered"
        :arrivalList="arrivalList"
        :departureList="departureList"
        @search="getAirlines"
        />
      </div>
      <div class="airline-list">
        <div v-if="isSearched">
          <AirlineElement
          v-for="(airline, idx) in airlineList"
          :key="idx"
          :airline="airline"
          :arrivalId="arrivalId"
          />
        </div>
        <div v-else>
          오늘의 항공 분석 예측 서비스<br><br>
          On:Air는 당신의 편안한 비행을 위해 항공사의 지연률 통계 및 예측 서비스를 제공합니다.
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AirlineElement from "@/components/main/AirlineElement"
import Search from "@/components/main/Search"
import axios from "axios"
import API from "@/common/drf.js"

export default {
  name: 'Main',
  components: {
    Search,
    AirlineElement,
  },
  data() {
    return {
      airlineList: [],
      arrivalList: [],
      departureList: [{text: 'ICN(인천)', value: 1}],
      bgImg: require('@/assets/main.jpg'),
      departure: 'On✈',
      arrival: '✈Air',
      arrivalId: '',
      isSearched: false,
      isRendered: false,
    }
  },
  methods: {
    getArrivals: function() {
      axios({
        url: API.URL + API.ROUTES.getArrivals,
        method: "get",
      })
        .then((res) => {
          const arrivals = res.data
          arrivals.sort(function (a, b) {
            if (a.name[4] > b.name[4]) {
              return 1
            } 
            else if (a.name[4] < b.name[4]) {
              return -1
            }
            return 0
          })
          for (let i = 0; i < arrivals.length; i++) {
            this.arrivalList.push(
              {id: arrivals[i].id, text: arrivals[i].name, value: i+1}
            )
          }
          this.isRendered = true
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getAirlines: function (arrivalId, departureCode, arrivalCode) {
      this.$vs.loading({
        type: 'material'
      })
      this.airlineList = []
      this.arrivalId = arrivalId
      this.setDeparture(departureCode)
      this.setArrival(arrivalCode)
      this.bgImg = `https://j5a203.p.ssafy.io/static/airlines/images/city_bg/${arrivalCode.toLowerCase()}.jpeg`
      axios({
        url: API.URL + API.ROUTES.getAirlines + arrivalId + '/',
        method: "get",
      })
        .then((res) => {
          if (this.airlineList.length == 0) {
            const airlines = res.data.Airlines
            airlines.sort(function (a, b) {
              if (a.total > b.total) {
                return -1
              } 
              else if (a.total < b.total) {
                return 1
              }
              return 0
            })
            for (const airline of airlines) {
              if (airline.total != 0) {
                this.airlineList.push(airline)
              }
            }
            this.isSearched = true
            this.$vs.loading.close()
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    setDeparture: function (name) {
      this.departure = name + '✈'
    },
    setArrival: function (name) {
      this.arrival = '✈' + name
    }
  },
  mounted() {
    this.getArrivals()
  },
  created() {
  }
}
</script>

<style>
  .airline-list {
    display: flex;
    justify-content: center;
    padding-bottom: 150px;
  }

  .arrival-info {
    color: white;
    font-size: 130px;
    font-weight: 700;
    text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.26);
    margin-top: 50px;
    display: flex;
    justify-content: center;
  }

  .main {
    background-size: cover;
    background-attachment: fixed;
  }

  .main-container {
    height: auto;
    min-height: 1000px;
  }

  .search-box {
    display: flex;
    justify-content: center;
    margin-top: 20px;
    margin-bottom: 80px;
  }
</style>