<template>
  <div class="airline-element">
    <img 
    class="airline-logo"
    :src="airline.profile_url" 
    alt="">
    {{airline.name}}
    {{airline.total}}
    {{airline.delay_rate}}
    {{airline.delay_time}}
    {{airline.predicted_delay_rate}}
  </div>
</template>

<script>
export default {
  name: 'Airline',
  props: ['airline'],
  data() {
    return {

    }
  },
  methods: {

  }
}
</script>

<style>
  .airline-element {
    background-color: white;
    border-radius: 10px;
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.705);
    width: 1000px;
    height: 150px;
    margin-bottom: 20px;
  }

  .airline-logo {
    width: 150px;
  }
</style>