<template>
  <div>
    <nav v-if="this.$route.name === 'Main'" class="nav justify-content-end">
      <div v-if="isLogin" class="logout mt-5 mx-5" @click="logOut">로그아웃</div>
      <div v-else class="login mt-5 mx-5" @click="moveToLogin">로그인</div>   
    </nav>
    <nav v-else class="nav justify-content-between">
      <!-- 로고 -->
      <img src="@/assets/onair_logo.png"
        alt="logo-image"
        id="logo-image"
        class="mt-5 mx-5"
        @click="moveToMain"
        />
      <!-- 로그인 -->
      <div v-if="isLogin" class="logout mt-5 mx-5" @click="logOut">로그아웃</div>
      <div v-else class="login mt-5 mx-5" @click="moveToLogin">로그인</div>        
    </nav>
  </div>
</template>

<script src="https://apis.google.com/js/platform.js" async defer></script>
<script>
import { mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  data() {
    return {
      token: localStorage.getItem('token'),
    }
  },  
  methods: {
    moveToMain: function() {
      if (this.$route.path !== "/") {
        this.$router.push({ name: "Main" })
      }
    },
    moveToLogin: function() {
      if (this.$route.path !== "login") {
        this.$router.push({ name: "Login" })
      }
    },
    logOut: function() {
      const auth2 = gapi.auth2.getAuthInstance()
      if (confirm("로그아웃 하시겠습니까?")) {
        auth2.signOut().then(function () {
          localStorage.clear()
          window.location.reload()
        })
        auth2.disconnect()
      }
    },
  },
  mounted() {
    gapi.load('auth2', function() {
      gapi.auth2.init()
    })
  },
  computed: {
    ...mapGetters([
      'isLogin'
    ])
  },
}
</script>

<style>
#logo-image {
  height: 3.2rem;
}
.login .logout {
  cursor: pointer;
}
</style>