import Vue from 'vue'
import Router from 'vue-router'
import { store } from '@/store'
import Login from '@/components/Login'
import OPS from '@/components/OPS'
import Micromouse from '@/components/Micromouse'
import Aircopter from '@/components/Aircopter'
import Checkoffs from '@/components/Checkoffs'
import Secure from '@/components/Secure'
import Spec from '@/components/Spec'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      beforeEnter: (to, from, next) => {
        // If already logged in, redirect to secure
        if (store.getters.authenticated) {
          next('/secure')
        }
        else {
          next()
        }
      }
    },
    {
      path: '/ops',
      name: 'OPS',
      component: OPS
    },
    {
      path: '/mm',
      name: 'Micromouse',
      component: Micromouse
    },
    {
      path: '/ap',
      name: 'Aircopter',
      component: Aircopter
    },
    {
      path: '/dav',
      name: 'DAV',
      component: Aircopter
    },
    {
      path: '/checkoffs',
      name: 'Checkoffs',
      component: Checkoffs
    },
    {
      path: '/secure',
      name: 'Secure',
      component: Secure
    },
    {
      path: '/spec',
      name: 'Spec',
      component: Spec
    }
  ]
})

// Redirect to login if user isn't authenticated
router.beforeEach((to, from, next) => {
  const publicPages = ['/login', '/register', '/reset', '/verify'];
  const authRequired = !publicPages.includes(to.path)

  if (!store.getters.authenticated && authRequired) {
    next('/login')
  }
  else {
    next()
  }
})

export {router as default}
