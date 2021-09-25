import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import store from './common/store.js'
import router from './common/vue-router.js'

Vue.use(VueRouter)
Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
