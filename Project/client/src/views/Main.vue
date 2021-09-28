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
        <Search/>
      </div>
    </div>
  </div>
</template>

<script>
import Search from "@/components/main/Search"

export default {
  name: 'Main',
  components: {
    Search
  },
  data() {
    return {
      airline_list: [],
      arrival_list: [],
      departure_list: ['인천(ICN)'],
      bg_img: require('@/assets/main.jpg'),
      departure: 'ICN✈',
      arrival: '✈TAO',
    }
  }
}
</script>

<style>
  .arrival-info {
    color: white;
    font-size: 130px;
    font-weight: 700;
    margin-top: 50px;
    display: flex;
    justify-content: center;
  }

  .main {
    background-size: cover;
    background-attachment: fixed;
  }

  .main-container {
    height: 1190px;
  }

  .search-box {
    border: 1px solid black;
  }
</style>