<template>
  <div class='main' :style="{backgroundImage: 'linear-gradient( rgba(0, 0, 0, 0.08), rgba(0, 0, 0, 0.08) ), url('+ bgImg +')'}">
    <div class="main-container">
      <div class="arrival-info user-select-none">
        <span>
          {{departure}}
          <span class="material-icons flight-icon">
            flight
          </span>
        </span>
        <span style="margin-top: 250px; margin-left: 350px;">
          <span class="material-icons flight-icon">
            flight
          </span>
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
        <div class="main-intro user-select-none" v-else>
          <span style="font-size: 17px; font-weight: bold;">On:Air는 당신의 편안한 비행을 위해 항공사의 지연률 통계 및 예측, 리뷰 감성분석 서비스를 제공합니다.</span><br><br><br>
          <span style="margin-left: 20px; margin-right: 150px;">항공사 출발 데이터 통계</span>
          <span style="margin-right: 140px;">빅데이터 기반 출발 지연 예측</span>
          <span>리뷰 키워드 도출 및 감성분석</span><br>
          <img style="border-radius: 5px; width: 300px; object-fit: cover; margin-right: 30px; margin-top: 10px;" src="@/assets/intro1.png" alt="onair-data">
          <img style="border-radius: 5px; width: 306px; object-fit: cover; margin-right: 30px; margin-top: 10px;" src="@/assets/intro2.png" alt="onair-predict">
          <img style="border-radius: 5px; width: 297px; object-fit: cover; margin-top: 10px;" src="@/assets/intro3.png" alt="onair-review">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import API from '@/common/drf.js'
import AirlineElement from '@/components/main/AirlineElement'
import Search from '@/components/main/Search'

export default {
  name: 'Main',
  components: {
    AirlineElement,
    Search,
  },
  data() {
    return {
      airlineList: [],
      arrivalList: [],
      departureList: [{ text: 'ICN(인천)', value: 1 }],
      bgImg: require('@/assets/main.jpg'),
      departure: 'On',
      arrival: 'Air',
      arrivalId: '',
      isSearched: false,
      isRendered: false,
    }
  },
  methods: {
    getArrivals: function () {
      axios({
        url: API.URL + API.ROUTES.getArrivals,
        method: 'get',
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
          this.arrivalList.push({ 
            id: arrivals[i].id, 
            text: arrivals[i].name, 
            value: i+1 
          })
        }
        this.isRendered = true
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
        url: `${API.URL}${API.ROUTES.getAirlines}${arrivalId}/`,
        method: 'get',
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
    },
    setDeparture: function (name) {
      this.departure = name
    },
    setArrival: function (name) {
      this.arrival = name
    }
  },
  mounted() {
    this.getArrivals()
  },
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
  display: flex;
  font-size: 130px;
  font-weight: 700;
  justify-content: center;
  margin-top: 50px;
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.26);
}
.flight-icon {
  font-size: 130px !important; 
  transform: rotate(90deg);
  vertical-align: -20px; 
}
.main {
  background-attachment: fixed;
  background-size: cover;
}
.main-container {
  height: auto;
  min-height: 1000px;
}
.main-intro {
  background-color: rgba(239, 237, 242, 0.5);
  border-radius: 5px;
  color: #555555;
  padding: 60px 40px 60px 40px;
  width: 1050px;
}
.search-box {
  display: flex;
  justify-content: center;
  margin-bottom: 80px;
  margin-top: 20px;
}
</style>