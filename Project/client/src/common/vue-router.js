import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main.vue'
import Login from '@/views/Login.vue'
import Airline from '@/views/Airline.vue'
import Profile from '@/views/Profile.vue'
import ReviewCreate from '@/components/airline/reviews/ReviewCreate.vue'


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
    path: '/airline',
    name: 'Airline',
    component: Airline
  },
  {
    path: '/mypage',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/airline/create',
    name: 'ReviewCreate',
    component: ReviewCreate
  },
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
