<template>
  <div>
    <nav v-if="this.$route.name === 'Main'" class="nav justify-content-end">
      <div v-if="isLogin" class="nav-menu d-flex mt-5 mx-5">
        <div class="nav-element" @click="moveToMypage">마이페이지</div>
        <div class="nav-element" @click="logOut">로그아웃</div>
      </div>
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
      <div v-if="isLogin" class="nav-menu d-flex mt-5 mx-5">
        <div class="nav-element" @click="moveToMypage">마이페이지</div>
        <div class="nav-element" @click="logOut">로그아웃</div>
      </div>
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
    moveToMypage: function() {
      if (this.$route.name !== "Profile") {
        this.$router.push({ name: "Profile" , params: {userId: localStorage.getItem('userId')},})
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
.nav-element:not(:last-child) {
  margin-right: 15px;
}
.navbar {
  height: 250px;
}
.login .logout {
  cursor: pointer;
}
</style>