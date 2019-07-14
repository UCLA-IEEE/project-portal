import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import Cookies from 'js-cookie'

Vue.use(Vuex)

export const store = new Vuex.Store({
  plugins: [createPersistedState({
    storage: window.localStorage
  })],
  state: {
    authenticated: false
  },
  getters: {
    authenticated: state => state.authenticated
  },
  mutations: {
    updateAuthenticated(state, param) {
      state.authenticated = param
    }
  }
});
