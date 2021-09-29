<template>
  <div class="d-flex justify-content-between">
    <nav class="navbar">
      <!-- 로고 -->
      <button @click="moveToMain">
        <img
          src="@/assets/log.png"
          style="height: 2.1rem"
          alt="logo-image"
        />
      </button>

      <!-- 로그인 -->
      <button @click="moveToLogin">로그인</button>
  </div>
</template>

<script src="https://apis.google.com/js/platform.js" async defer></script>
<script>
export default {
  name: 'NavBar',
  methods: {
    moveToMain() {
      if (this.$route.path !== "/") {
        this.$router.push({ name: "Main" })
      }
    },
    moveToLogin() {
      if (this.$route.path !== "login") {
        this.$router.push({ name: "Login" })
      }
    },
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