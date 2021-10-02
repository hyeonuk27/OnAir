import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main.vue'
import Login from '@/views/Login.vue'
import Airline from '@/views/Airline.vue'
import Profile from '@/views/Profile.vue'
import ProfileUpdate from '@/components/profile/ProfileUpdate.vue'
import MyReview from '@/components/profile/MyReview.vue'
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
    path: '/airline/:arrivalId/:airlineId',
    name: 'Airline',
    component: Airline
  },
  {
    path: '/profile/:userId',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/profile/:userId/update',
    name: 'ProfileUpdate',
    component: ProfileUpdate
  },
  {
    path: '/profile/:userId/reviews',
    name: 'MyReview',
    component: MyReview
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
