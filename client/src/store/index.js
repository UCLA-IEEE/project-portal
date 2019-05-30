import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    authenticated: false
  },
  getters: {
    authenticated: state => state.authenticated
  },
  mutations: {
    updateAuthenticated (state) {
      state.authenticated = !state.authenticated;
    }
  }
});
