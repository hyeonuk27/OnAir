<template>
  <div class="container p-3">
    <div class="row p-2 align-items-center">
      <div class="col-2">
        <img
        :src="airline_info.profile_url" 
        alt="airline-logo"
        class="img-fluid"
        >
      </div>
      <div class="col-2">
        <img
        v-if="airline_info.is_skyteam"
        src="@/assets/team_logo/skyteam.png"
        class="img-fluid"
        >
        <img
        v-if="airline_info.is_star"
        src="@/assets/team_logo/star.png"
        class="img-fluid"
        >
        <img
        v-if="airline_info.is_oneworld"
        src="@/assets/team_logo/oneworld.png"
        class="img-fluid"
        >
      </div>
      <div class="col-8">
        <span>{{ airline_info.detail }}</span>
      </div>
    </div>
    <div class="p-2">
      <span><i class="fas fa-building"></i>{{ airline_info.address }}</span> |
      <span><i class="fas fa-phone"></i>{{ airline_info.phone_number }}</span> |
      <a :href="airline_info.site_url"><i class="fas fa-globe"></i>홈페이지</a> |
      <a :href="airline_info.corona_url"><i class="fas fa-info-circle"></i>코로나 19 업데이트 </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AirlineInfo',
  props: ['airline_info'],
  data() {
    return {
      
    }
  },
  methods: {
  }
}
</script>

<style>

</style>