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
      path: '/Login',
      name: 'Login',
      component: Login
    },
    {
      path: '/OPS',
      name: 'OPS',
      component: OPS
    },
    {
      path: '/Micromouse',
      name: 'Micromouse',
      component: Micromouse
    },
    {
      path: '/Aircopter',
      name: 'Aircopter',
      component: Aircopter
    },
    {
      path: '/Secure',
      name: 'Secure',
      component: Secure
    }
  ]
})
