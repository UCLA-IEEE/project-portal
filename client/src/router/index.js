import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import OPS from '@/components/OPS'
import Micromouse from '@/components/Micromouse'
import Aircopter from '@/components/Aircopter'
import Secure from '@/components/Secure'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/Login'
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
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
      path: '/secure',
      name: 'Secure',
      component: Secure
    }
  ]
})
