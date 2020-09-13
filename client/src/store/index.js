import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import axios from 'axios'

Vue.use(Vuex)

export const store = new Vuex.Store({
  plugins: [createPersistedState({
    storage: window.localStorage
  })],
  state: {
    status: "",
    user: null
  },
  getters: {
    authStatus: state => state.status,
    authenticated: state => state.user !== null,
    user: state => state.user
  },
  mutations: {
    auth_success(state, user) {
      state.status = "success";
      state.user = user;
    },
    auth_error(state) {
      state.status = "error";
      state.user = null;
    },
    logout(state) {
      state.status = "";
      state.user = null;
    }
  },
  actions: {
    login({ commit }, user) {
      return axios({
        method: "POST",
        "url": "http://localhost:5000/auth/login",
        "data": {
          username: user.username,
          password: user.password
        },
        "headers": { "Content-Type": "application/json",
                     "Access-Control-Allow-Origin": '*' }
      })
      .then(res => {
        commit('auth_success', res.data)
      })
      .catch(() => {
        commit('auth_error')
      })
    }
  }
});
