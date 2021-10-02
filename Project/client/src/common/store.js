import Vue from 'vue'
import Vuex from 'vuex'

// import SERVER from '@/common/drf.js'
// import router from '@/common/vue-router.js'
// import axios from 'axios'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('token'),
    userId: localStorage.getItem('userId'),
    name: localStorage.getItem('name'),
    profileUrl: localStorage.getItem('profileUrl'),
  },
  getters: {
    isLogin: function (state) {
      return state.token ? true : false
    }
  },
  mutations: {
    SET_NAME: (state, name) => {
      state.name = name
    }
  },
  actions: {
    setName({commit}, name) {
      commit('SET_NAME', name)
    }
  },
  modules: {
  },
  plugins: [
    createPersistedState(),
  ],
})