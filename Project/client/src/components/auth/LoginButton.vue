<template>
  <div class='LoginBtn'>
    <div id="my-signin2"></div>
  </div>
</template>

<script src="https://apis.google.com/js/platform.js" async defer></script>
<script>
import axios from 'axios'
import API from '@/common/drf.js'

export default {
  name: 'LoginButton',
  methods: {
    onSuccess(googleUser) {
      const accessToken = googleUser.getAuthResponse().id_token
      axios.get("https://j5a203.p.ssafy.io/api/v1/auth/login/", {
        headers: {
            Authorization: accessToken
        }
      })
      .then((res) => {
        localStorage.setItem('token', res.data.access_token)
        this.$router.push({ name: "Main" })
      })
    },
    onFailure(error) {
      console.log(error);
    },
  },
  mounted() {
    window.gapi.signin2.render('my-signin2', {
      scope: 'profile email',
      width: 500,
      height: 50,
      longtitle: true,
      theme: 'dark',
      onsuccess: this.onSuccess,
      onfailure: this.onFailure,
    });
  },
}
</script>

<style>

</style>