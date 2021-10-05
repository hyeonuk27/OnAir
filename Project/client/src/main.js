import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import store from './common/store.js'
import router from './common/vue-router.js'
import Vuesax from 'vuesax'
import 'vuesax/dist/vuesax.css'
import 'material-icons/iconfont/material-icons.css'
import Highcharts from "highcharts"
import HighchartsVue from 'highcharts-vue'
import ExportingHighcharts from "highcharts/modules/exporting";
import VueMoment from 'vue-moment'
import loadWordcloud from 'highcharts/modules/wordcloud'

loadWordcloud(Highcharts)

Vue.use(VueRouter)
Vue.use(Vuesax)
ExportingHighcharts(Highcharts)
Vue.use(HighchartsVue, {tagName: 'charts'})
Vue.use(VueMoment)
Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
