<template>
  <div>
    <img 
    :src="airline_info.profile_url" 
    alt="airline-logo">
    <img
    src="skyteam"
    >
    <div>
      <span>{{ airline_info.details }}</span>
      <span>{{ airline_info.address }}</span> |
      <span>{{ airline_info.phone_number }}</span> |
      <a :href="airline_info.site_url">홈페이지</a> |
      <a :href="airline_info.corona_url">코로나 19 업데이트 </a>
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