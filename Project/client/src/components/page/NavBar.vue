<template>
  <div>
    <nav class="nav justify-content-between">
      <!-- 로고 -->
        <img
          src="@/assets/onair_logo.png"
          style="height: 3.2rem"
          alt="logo-image"
          @click="moveToMain"
          class="mt-5 mx-5"
        />
      <!-- 로그인 -->
        <div
          v-if="token"
          class="mt-5 mx-5"
          @click="signOut">
          로그아웃
        </div>
        <div
          v-else
          class="mt-5 mx-5"
          @click="moveToLogin">
          로그인
        </div>        

    </nav>
  </div>
</template>

<script src="https://apis.google.com/js/platform.js" async defer></script>
  <script src="https://apis.google.com/js/platform.js?onload=onLoad" async defer></script>
<script>
export default {
  name: 'NavBar',
  data() {
    return {
      token: localStorage.getItem('token')
    }
  },  
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
      console.log(auth2)
      auth2.signOut().then(function () {
        localStorage.removeItem('token')
        console.log('로그아웃')
      })
      auth2.disconnect()
    },
    onLoad() {
      gapi.load('auth2', function() {
        gapi.auth2.init()
      })
    },
  },
  mounted() {
    gapi.load('auth2', function() {
      gapi.auth2.init()
    })
  } 
}
</script>

<style>

</style>