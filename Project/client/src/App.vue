<template>
  <div id="app">
    <NavBar id="navbar"/>
    <RouterView id="router" :key="$route.fullPath"/>
    <Footer id="footer"/>
  </div>
</template>

<script>
import NavBar from "@/components/page/NavBar"
import Footer from "@/components/page/Footer"

export default {
  name: 'App',
  components: {
    NavBar,
    Footer
  }
}
</script>

<style>
html,body {
  margin: 0;
  padding: 0;
  height: 100%;
}

#app {
  font-family: 'Noto Sans KR', sans-serif;
  /* font-family: 'KoPubDotumMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/KoPubDotumMedium.woff') format('woff');; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  box-sizing: border-box;
  text-align: center;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
  /* max-width: 960px; */
  height: 100%;
  position: relative;
}

#navbar {
  float: left;
  min-width: 1190px;
  position: absolute;
  width: 100%;
}

#router {
  flex: 1;
  min-width: 1190px;
}

#footer {
  min-width: 1190px;
}
</style>

<style lang="scss">
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
  background: #ffffff;
}

::-webkit-scrollbar-thumb {
  border-radius: 3.5px;
  background-color: #B9A6C9;

  &:hover {
    background-color: #D4C6E2;
  }
}

::-webkit-scrollbar-track {
  background: #ffffff;
}
</style>
