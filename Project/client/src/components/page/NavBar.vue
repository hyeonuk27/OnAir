<template>
  <div>
    NavBar
  </div>
</template>

<script src="https://apis.google.com/js/platform.js" async defer></script>
<script>
export default {
  name: 'NavBar',
  methods: {
    signOut() {
      const auth2 = gapi.auth2.getAuthInstance()
      auth2.signOut().then(function () {
        console.log('로그아웃')
      })
      auth2.disconnect()
    }
  }
}
</script>

<style>

</style>