<template>
  <div class="search-log-el" @click="goAirline">
    <div class="search-log-date">
      {{$moment(regDt).format('YYYY.MM.DD &nbsp;HH시 mm분')}}
    </div>
    <div class="search-log-airline">
      항공사: {{log.airline_name}}
    </div>
    <div class="search-log-arrival">
      도착지: {{log.arrival_name}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchLogElement',
  props: {
    log: Object,
  },
  methods: {
    goAirline: function () {
      if (this.token != null) {
        this.logCreate()
      }
      this.$router.push({
        name: 'Airline',
        params: {
          airlineId: this.log.airline,
          arrivalId: this.log.arrival,
        },
      })
    },
  },
  computed: {
    regDt: function () {
      const timestamp = Date.parse(this.log.reg_dt)
      return new Date(timestamp)
    }
  }
}
</script>

<style>
.search-log-airline {
  grid-column: 2;
  grid-row: 2;
  padding: 20px;
  text-align: start;
}
.search-log-arrival {
  grid-column: 3;
  grid-row: 2;
  padding: 20px;
  text-align: start;
}
.search-log-date {
  grid-column: 1;
  grid-row: 2;
  padding: 20px;
  text-align: start;
}
.search-log-el {
  border: 1px solid rgba(180, 180, 180, 0.658);
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.151);
  cursor: pointer;
  display: grid;
  grid-auto-rows: 40px 50px 60px;
  grid-template-columns: 300px 300px 400px;
  height: 150px;
  margin-bottom: 20px;
  transition: 0.2s;
  width: 1000px;
}
.search-log-el:hover {
  background-color: rgba(223, 223, 223, 0.904);
}
</style>