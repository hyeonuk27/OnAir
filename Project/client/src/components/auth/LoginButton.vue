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
    onSuccess: function(googleUser) {
      const accessToken = googleUser.getAuthResponse().id_token
      axios({
        url: API.URL + API.ROUTES.login,
        method: 'get',
        headers: {
          Authorization: accessToken
        }
      })
      .then((res) => {
        localStorage.setItem('token', res.data.access_token)
        this.$router.push({ name: "Main" })
        window.location.reload()
      })
    },
    onFailure: function(error) {
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
    })
  },
}
</script>

<style>

</style>