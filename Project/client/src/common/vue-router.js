import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main.vue'
import Login from '@/views/Login.vue'
import Airline from '@/views/Airline.vue'
import ReviewCreate from '@/components/airline/reviews/ReviewCreate.vue'
import HelloWorld from '@/components/HelloWorld.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  //테스트중...
  {
    path: '/test',
    name: 'HelloWorld',
    component: HelloWorld
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
    path: '/airline/create',
    name: 'ReviewCreate',
    component: ReviewCreate
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
