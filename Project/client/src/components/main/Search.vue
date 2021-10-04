<template>
  <div class="search">
    <vs-select
      color="#B9A6C9"
      class="select-box"
      placeholder="출발지 선택"
      width="300px"
      v-model="departureIdx"
      >
      <vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in departureList" />
    </vs-select>

    <vs-select
      color="#B9A6C9"
      class="select-box"
      placeholder="도착지 선택"
      width="300px"
      v-model="arrivalIdx"
      >
      <vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in arrivalList" />
    </vs-select>
  </div>
</template>

<script>
import {mapState, mapActions} from 'vuex'

export default {
  name: 'Search',
  props: ['departureList', 'arrivalList'],
  data() {
    return {
      departureIdx: '',
      arrivalIdx: '',
    }
  },
  methods: {
    ...mapActions([
      'setDeparture',
      'setArrival'
    ]),
    search: function() {
      if (this.departure != '' && this.arrival != '' && this.departure != 'null' && this.arrival != 'null' && this.departure != null && this.arrival != null) {
        this.$emit('search', this.arrivalList[this.arrival-1].id, this.departureList[this.departure-1].text.substring(0, 3), this.arrivalList[this.arrival-1].text.substring(0, 3))
      }
    }
  },
  created() {
    localStorage.setItem('departure', [])
    localStorage.setItem('arrival', [])
    this.departureIdx = this.departure
    this.arrivalIdx = this.arrival
  },
  computed: {
    ...mapState(['arrival', 'departure'])
  },
  watch: {
    departureIdx: function (val) {
      this.setDeparture(val)
      this.search()
    },
    arrivalIdx: function (val) {
      this.setArrival(val)
      this.search()
    }
  }
}
</script>

<style>
  .search {
    align-items: center;
    background-color: white;
    border-radius: 10px;
    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.705);
    display: flex;
    justify-content: space-between;
    width: 700px;
    height: 100px;
    padding: 0 25px;
  }

  .search::-webkit-scrollbar{
    width: 6px;
  }

  .search::-webkit-scrollbar-thumb{
    height: 17%;
    background-color: rgba(255,255,255,1);
    /* 스크롤바 둥글게 설정    */
    border-radius: 10px;    
}
</style>