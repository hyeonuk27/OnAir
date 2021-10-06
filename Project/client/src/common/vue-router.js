import Vue from 'vue'
import VueRouter from 'vue-router'
import swal from 'sweetalert'

import Airline from '@/views/Airline.vue'
import Form from '@/views/Form.vue'
import Login from '@/views/Login.vue'
import Main from '@/views/Main.vue'
import MyReview from '@/components/profile/MyReview.vue'
import NotFound from '@/views/NotFound.vue'
import Profile from '@/views/Profile.vue'
import ProfileUpdate from '@/components/profile/ProfileUpdate.vue'
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
    path: '/profile/:userId/reviews',
    name: 'MyReview',
    component: MyReview
  },
  {
    path: '/profile/:userId/update',
    name: 'ProfileUpdate',
    component: ProfileUpdate
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

router.beforeEach((to, from, next) => {
  const authPages = [
    'Profile',
    'ProfileUpdate',
    'Form',
    'Update',
    'SearchLog',
  ]

  const authRequired = authPages.includes(to.name)
  const isLoggedIn = localStorage.getItem('token') ? true : false
  
  if (authRequired && !isLoggedIn) {
    swal({
      title: '로그인이 필요한 페이지입니다.',
      icon: 'warning',
      buttons: {
        confirm: {
          text: '확인',
          className: 'confirm-btn'
        },
      },
    })
    .then(() => {
      next({ name: 'Login' })
    })
  } else {
    next()
  }
})