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

<script>
export default {
  name: "Navbar",
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
}
</script>

<style>

</style>