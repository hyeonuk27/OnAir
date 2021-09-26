<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <!-- <div class="g-signin2" id="google-signin-btn" data-onsuccess="onSignIn"></div> -->
    <!-- <div class="g-signin2" id="google-signin-btn"></div> -->
    <div id="my-signin2"></div>
    <a href="#" @click="signOut">로그아웃</a>
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener">babel</a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener">eslint</a></li>
    </ul>
    <h3>Essential Links</h3>
    <ul>
      <li><a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank" rel="noopener">Forum</a></li>
      <li><a href="https://chat.vuejs.org" target="_blank" rel="noopener">Community Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank" rel="noopener">Twitter</a></li>
      <li><a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a></li>
    </ul>
    <h3>Ecosystem</h3>
    <ul>
      <li><a href="https://router.vuejs.org" target="_blank" rel="noopener">vue-router</a></li>
      <li><a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a></li>
      <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank" rel="noopener">vue-devtools</a></li>
      <li><a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">awesome-vue</a></li>
    </ul>
  </div>
</template>

<script src="https://apis.google.com/js/platform.js" async defer></script>
<script>
import axios from 'axios'


export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  methods: {
    onSuccess(googleUser) {
      const accessToken = googleUser.getAuthResponse().id_token
      axios.get("http://localhost:8000/api/v1/auth/login", {
        headers: {
            Authorization: accessToken
        }
      })
      .then((res) => {
        console.log(res.data)
      })
    },
    onFailure(error) {
      console.log(error);
    },
    signOut() {
      const auth2 = gapi.auth2.getAuthInstance()
      auth2.signOut().then(function () {
        console.log('로그아웃')
      })
      auth2.disconnect()
    }
  },
  mounted() {
    window.gapi.signin2.render('my-signin2', {
      scope: 'profile email',
      width: 240,
      height: 50,
      longtitle: true,
      theme: 'dark',
      onsuccess: this.onSuccess,
      onfailure: this.onFailure,
    });
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
