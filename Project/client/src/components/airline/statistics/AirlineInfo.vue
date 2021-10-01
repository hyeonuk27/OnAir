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
        <span>{{ airlineInfo.detail }}</span>
      </div>
      <div class="line-info text-start">
        <span class="address"><i class="fas fa-building"></i>{{ airlineInfo.address }}</span> |
        <span class="num"><i class="fas fa-phone"></i>{{ airlineInfo.phone_number }}</span> |
        <a :href="airlineInfo.site_url" class="website"><i class="fas fa-globe"></i>홈페이지</a> |
        <a :href="airlineInfo.corona_url" class="covid19"><i class="fas fa-info-circle"></i>코로나 19 업데이트 </a>
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
    display: flex;
    justify-content: center;
  }

  .airline-info-wrapper {
    display: grid;
    grid-template-columns: 200px 50px 1fr;
    grid-gap: 30px 40px;
    grid-auto-rows: min-content;
  }

  .profile-logo {
    grid-column: 1;
    grid-row: 1;
    width: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .team-logo {
    grid-column: 2;
    grid-row: 1;
    width: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .line-intro {
    grid-column: 3;
    grid-row: 1;
    width: 750px;
  }

  .line-info {
    grid-column: 1 / 5;
    grid-row: 2;
    margin: 10px;
  }

</style>