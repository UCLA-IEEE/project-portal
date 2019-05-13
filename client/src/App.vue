<template>
  <div id="app">
    <Navigation></Navigation>
    <router-view @authenticated="setAuthenticated" />
  </div>
</template>

<script>
import Navigation from './components/Navigation'
export default {
  name: 'app',
  data() {
    return {
      authenticated: false,
      mockAccount: {
        username: "ieee-test",
        password: "password"
      }
    }
  },
  mounted() {
    if(!this.authenticated) {
      this.$router.replace({ name: "Login" });
    }
  },
  methods: {
    setAuthenticated(status) {
      this.authenticated = status;
    },
    logout() {
      this.authenticated = false;
    }
  },
  components: {
    'Navigation': Navigation
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
