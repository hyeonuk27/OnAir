<template>
  <div style="display: flex; justify-content: center;">
    <div style="width: 1190px;">
      <nav v-if="this.$route.name === 'Main'" class="nav justify-content-end">
        <div v-if="isLogin" class="nav-menu d-flex mt-5">
          <div style="color: white; cursor: pointer; text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.26);" class="nav-element" @click="moveToMypage">마이페이지</div>
          <div style="color: white; cursor: pointer; text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.26);" class="nav-element" @click="logOut">로그아웃</div>
        </div>
        <div v-else style="color: white; cursor: pointer; text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.26);" class="login mt-5" @click="moveToLogin">로그인</div>   
      </nav>
      <nav v-else class="nav justify-content-between nav-not-main">
        <!-- 로고 -->
        <img src="@/assets/onair_logo.png"
          alt="logo-image"
          id="logo-image"
          class="mt-5"
          @click="moveToMain"
          />
        <!-- 로그인 -->
        <div v-if="isLogin" class="nav-menu d-flex mt-5">
          <div class="nav-element" @click="moveToMypage">마이페이지</div>
          <div class="nav-element" @click="logOut">로그아웃</div>
        </div>
        <div v-else class="login mt-5" @click="moveToLogin">로그인</div>        
      </nav>
    </div>
  </div>
</template>

<script src="https://apis.google.com/js/platform.js" async defer></script>
<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'NavBar',
  data() {
    return {
      token: localStorage.getItem('token'),
    }
  },  
  methods: {
    ...mapActions([
      'setDeparture',
      'setArrival'
    ]),
    moveToMain: function() {
      this.setDeparture([])
      this.setArrival([])
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

  .nav-not-main{
    border-bottom: 10px solid #EFEDF2;
    padding-bottom: 10px;
  }

  .navbar {
    height: 250px;
  }

  .login .logout {
    cursor: pointer;
  }
</style>