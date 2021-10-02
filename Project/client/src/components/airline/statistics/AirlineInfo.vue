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
        <p>{{ airlineInfo.detail }}</p>
      </div>
      <div class="text-start line-info">
        <p class="address"><i class="fas fa-building address"></i>{{ airlineInfo.address }}</p> |
        <p class="num"><i class="fas fa-phone num"></i>{{ airlineInfo.phone_number }}</p> |
        <a :href="airlineInfo.site_url" target="_blank" class="website"><i class="fas fa-globe website"></i>홈페이지<i class="fas fa-external-link-alt website"></i></a> |
        <a :href="airlineInfo.corona_url" target="_blank" class="text-danger covid19"><i class="fas fa-info-circle website"></i>코로나 19 업데이트<i class="fas fa-external-link-alt covid19"></i></a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AirlineInfo',
  props: ['airlineInfo'],
}
</script>

<style>
  .airline-info {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .airline-info-wrapper {
    display: grid;
    grid-template-columns: 150px 20px 40px 1fr;
    grid-gap: 0px 20px;
    grid-auto-rows: min-content;
  }

  .profile-logo {
    grid-column: 1;
    grid-row: 1;
    width: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .team-logo {
    grid-column: 2 / 3;
    grid-row: 1;
    width: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .line-intro {
    grid-column: 4;
    grid-row: 1;
    width: 100%;
    line-height: 120%;
    font-size: 12px;
    display: flex;
    align-items: center;
    color: #656F8C;
  }

  .line-info {
    grid-column: 1 / 5;
    grid-row: 2;
    display: inline;
    line-height: 110%;
    font-size: 12px;
    color: #656F8C;
  }
  .address {
    display: inline;
    padding-right: 5px;
  }

  .num {
    display: inline;
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

</style>