import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import OPS from '@/components/OPS'
import Micromouse from '@/components/Micromouse'
import Aircopter from '@/components/Aircopter'
import Spec from '@/components/Spec'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/ops',
      name: 'OPS',
      component: OPS
    },
    {
      path: '/micromouse',
      name: 'Micromouse',
      component: Micromouse
    },
    {
      path: '/aircopter',
      name: 'Aircopter',
      component: Aircopter
    },
    {
      path: '/spec',
      name: 'Spec',
      component: Spec
    }
  ]
})
