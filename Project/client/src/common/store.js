import Vue from 'vue'
import Vuex from 'vuex'

// import SERVER from '@/common/drf.js'
// import router from '@/common/vue-router.js'
// import axios from 'axios'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    
  },
  getters: {
    
  },
  mutations: {
    
  },
  actions: {
  },
  modules: {
  },
  plugins: [
    createPersistedState(),
  ],
})