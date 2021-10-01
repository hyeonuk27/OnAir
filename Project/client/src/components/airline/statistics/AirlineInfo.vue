<template>
  <div>
    <img 
    :src="airline_info.profile_url" 
    alt="airline-logo">
    <img
    src="skyteam"
    >
    <div>
      <p>{{ airline_info.details }}</p>
      <p>{{ airline_info.address }}</p> |
      <p>{{ airline_info.phone_number }}</p> |
      <p>{{ airline_info.site_url }}</p> |
      <p>{{ airline_info.corona_url }}</p>
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