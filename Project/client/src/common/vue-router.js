import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main.vue'
import Login from '@/views/Login.vue'
import Airline from '@/views/Airline.vue'
import Profile from '@/views/Profile.vue'
import Form from '@/views/Form.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/airline/:arrival_id/:airline_id',
    name: 'Airline',
    component: Airline
  },
  {
    path: '/profile/:user_id',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/form',
    name: 'Form',
    component: Form
  },
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
