<template>
  <div class="airline-info">
    <div class="airline-info-wrapper">
      <div class="profile-logo">
        <img
        :src="airlineInfo.profile_url"
        alt="airline-logo"
        class="img-fluid"
        >
      </div>
      <div class="team-logo">
        <img
        v-if="airlineInfo.is_skyteam"
        src="@/assets/team_logo/skyteam.png"
        class="img-fluid"
        >
        <img
        v-if="airlineInfo.is_star"
        src="@/assets/team_logo/star.png"
        class="img-fluid"
        >
        <img
        v-if="airlineInfo.is_oneworld"
        src="@/assets/team_logo/oneworld.png"
        class="img-fluid"
        >
      </div>
      <div class="line-intro text-start">
        <span id="detailText" >{{ airlineInfo.detail }}</span>
      </div>
      <div class="line-info text-start">
        <span id="detailText" class="address"><i class="fas fa-building address"></i>{{ airlineInfo.address }}</span> |
        <span id="detailText" class="num"><i class="fas fa-phone num"></i>{{ airlineInfo.phone_number }}</span> |
        <a :href="airlineInfo.site_url" id="detailText" class="website"><i class="fas fa-globe website"></i>홈페이지<i class="fas fa-external-link-alt website"></i></a> |
        <a :href="airlineInfo.corona_url" id="detailText" class="covid19"><i class="fas fa-info-circle covid19"></i>코로나 19 업데이트<i class="fas fa-external-link-alt covid19"></i></a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AirlineInfo',
  props: ['airlineInfo'],
  data() {
    return {
      
    }
  },
  methods: {
  }
}
</script>

<style>
  .airline-info {
    width: 700px;
    margin: 0 auto;
  }

  .airline-info-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-gap: 30px 40px;
    grid-auto-rows: min-content;
  }

  .profile-logo {
    grid-column: 1;
    grid-row: 1;
    width: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .team-logo {
    grid-column: 2;
    grid-row: 1;
    width: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .line-intro {
    grid-column: 3;
    grid-row: 1;
    width: 400px;
  }

  .line-info {
    grid-column: 1 / 5;
    grid-row: 2;
    margin: 10px;
  }
  
  .address {
    padding: 5px;
  }

  .num {
    padding: 5px;
  }

  .website {
    padding: 5px;
    text-decoration: none;
  }

  .covid19 {
    padding: 5px;
    text-decoration: none;
  }

  #detailText {
    font-size: x-small;
    line-height: 100%;
  }
</style>