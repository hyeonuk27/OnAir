<template>
  <div class='main' :style="{backgroundImage: 'linear-gradient( rgba(0, 0, 0, 0.08), rgba(0, 0, 0, 0.08) ), url('+ bg_img +')'}">
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
        :arrival_list="arrival_list"
        :departure_list="departure_list"
        @search="getAirlines"
        />
      </div>
      <div class="airline-list">
        <div>
          <AirlineElement
          v-for="(airline, idx) in airline_list"
          :key="idx"
          :airline="airline"
          :arrival_id="arrival_id"
          />
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
      airline_list: [],
      arrival_list: [],
      departure_list: [{text: 'ICN(인천)', value: 1}],
      bg_img: require('@/assets/main.jpg'),
      departure: 'On✈',
      arrival: '✈Air',
      arrival_id: '',
      is_searched: false,
    }
  },
  methods: {
    getArrivals: function() {
      axios({
        url: API.URL + API.ROUTES.get_arrivals,
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
            this.arrival_list.push(
              {id: arrivals[i].id, text: arrivals[i].name, value: i+1}
            )
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getAirlines: function (arrival_id, departure_code, arrival_code) {
      this.airline_list = []
      this.arrival_id = arrival_id
      this.setDeparture(departure_code)
      this.setArrival(arrival_code)
      this.bg_img = `https://j5a203.p.ssafy.io/static/airlines/images/city_bg/${arrival_code.toLowerCase()}.jpeg`
      axios({
        url: API.URL + API.ROUTES.get_airlines + arrival_id + '/',
        method: "get",
      })
        .then((res) => {
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
              this.airline_list.push(airline)
            }
          }
          this.is_searched = true
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
  created() {
    this.getArrivals()
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