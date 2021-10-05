import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main.vue'
import Login from '@/views/Login.vue'
import Airline from '@/views/Airline.vue'
import Profile from '@/views/Profile.vue'
import NotFound from '@/views/NotFound.vue'
import ProfileUpdate from '@/components/profile/ProfileUpdate.vue'
import MyReview from '@/components/profile/MyReview.vue'
import Form from '@/views/Form.vue'
import SearchLog from '@/components/profile/SearchLog.vue'


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
  {
    path: '/form/update',
    name: 'Update',
    component: Form
  },
  {
    path: '/:userId/logs',
    name: 'SearchLog',
    component: SearchLog
  },
  {
    path: '/404',
    name: 'NotFound',
    component: NotFound
  },
  { path: '*',
    name: 'NotFound',
    component: NotFound
  },
]

const router = new VueRouter({
  mode: 'history',
  routes,
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
})

export default router
