<template>
  <div>
    {{arrival_id}}
    {{airline_id}}
  </div>
</template>

<script>
export default {
  name: 'Airline',
  data () {
    return {
      arrival_id: '',
      airline_id: '',
    }
  },
  methods: {

  },
  created() {
    this.arrival_id = this.$route.params.arrival_id
    this.airline_id = this.$route.params.airline_id
  }
}
</script>

<style>

</style>