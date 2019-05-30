<template>
  <div id="app">
    <Navigation @authenticated="updateAuthenticated"></Navigation>
    <router-view @authenticated="updateAuthenticated"/>
  </div>
</template>

<script>
import Navigation from './components/Navigation'
export default {
  name: 'app',
  data() {
    return {
      authenticated: false
    }
  },
  methods: {
    updateAuthenticated() {
      this.authenticated = !this.authenticated;
      if(!this.authenticated) {
        this.$router.replace({ name: "Login" });
      }
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
