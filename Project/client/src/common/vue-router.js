import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main.vue'
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
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
