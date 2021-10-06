import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    arrival: localStorage.getItem('arrival'),
    departure: localStorage.getItem('departure'),
    name: localStorage.getItem('name'),
    profileUrl: localStorage.getItem('profileUrl'),
    token: localStorage.getItem('token'),
    userId: localStorage.getItem('userId'),
  },
  getters: {
    isLogin: function (state) {
      return state.token ? true : false
    },
  },
  mutations: {
    SET_ARRIVAL: (state, idx) => {
      state.arrival = idx
    },
    SET_DEPARTURE: (state, idx) => {
      state.departure = idx
    },
    SET_NAME: (state, name) => {
      state.name = name
    },
  },
  actions: {
    setArrival({commit}, idx) {
      localStorage.setItem('arrival', idx)
      commit('SET_ARRIVAL', idx)
    },
    setDeparture({commit}, idx) {
      localStorage.setItem('departure', idx)
      commit('SET_DEPARTURE', idx)
    },
    setName({commit}, name) {
      commit('SET_NAME', name)
    },
  },
})