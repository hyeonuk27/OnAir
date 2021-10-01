<template>
  <div class="search">
    <vs-select
      color="#B9A6C9"
      class="select-box"
      placeholder="출발지 선택"
      width="300px"
      v-model="departure"
      @change="search"
      >
      <vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in departureList" />
    </vs-select>

    <vs-select
      color="#B9A6C9"
      class="select-box"
      placeholder="도착지 선택"
      width="300px"
      v-model="arrival"
      @change="search"
      >
      <vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in arrivalList" />
    </vs-select>
  </div>
</template>

<script>
export default {
  name: 'Search',
  props: ['departureList', 'arrivalList'],
  data() {
    return {
      departure: [],
      arrival: [],
    }
  },
  methods: {
    search: function() {
      if (typeof this.departure != 'object' && typeof this.arrival != 'object') {
        this.$emit('search', this.arrivalList[this.arrival-1].id, this.departureList[this.departure-1].text.substring(0, 3), this.arrivalList[this.arrival-1].text.substring(0, 3))
      }
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