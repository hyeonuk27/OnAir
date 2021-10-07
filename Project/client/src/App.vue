<template>
  <div id="app">
    <NavBar id="navbar" />
    <RouterView id="router" :key="$route.fullPath" />
    <Footer id="footer" />
  </div>
</template>

<script>
import Footer from '@/components/page/Footer'
import NavBar from '@/components/page/NavBar'

export default {
  name: 'App',
  components: {
    NavBar,
    Footer
  }
}
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  box-sizing: border-box;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
  font-family: 'Noto Sans KR', sans-serif;
  height: 100%;
  position: relative;
  text-align: center;
}
#footer {
  min-width: 1190px;
}
html,body {
  height: 100%;
  margin: 0;
  padding: 0;
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
</style>

<style lang="scss">
::-webkit-scrollbar {
  background: #ffffff;
  height: 8px;
  width: 8px;
}
::-webkit-scrollbar-thumb {
  background-color: #B9A6C9;
  border-radius: 3.5px;

  &:hover {
    background-color: #D4C6E2;
  }
}
::-webkit-scrollbar-track {
  background: #ffffff;
}
</style>
