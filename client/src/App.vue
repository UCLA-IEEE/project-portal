<template>
  <div id="app">
    <MobileNavigation v-if="mobile" :width="windowSize.width"/>
    <Navigation v-else></Navigation>
    <router-view/>
  </div>
</template>

<script>
import Navigation from './components/Navigation'
import MobileNavigation from './components/MobileNavigation'
export default {
  name: 'app',
  data() {
    return {
      authenticated: false,
      windowSize: {
        width: 0,
        height: 0
      }
    }
  },
  updated() {
    this.$nextTick(function () {
      if(!this.$store.state.authenticated) {
        this.$router.replace({ name: "Login" });
      }
    })
  },
  components: {
    'Navigation': Navigation,
    'MobileNavigation': MobileNavigation
  },
  mounted: function() {
    window.addEventListener("resize", this.handleResize)
    this.handleResize()
  },
  beforeDestroy: function() {
    window.removeEventListener("resize", this.handleResize)
  },
  methods: {
    handleResize: function() {
      var w = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth
      var h = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight
      this.windowSize.width = w
      this.windowSize.height = h
    }
  },
  computed: {
    mobile: function() {
      if (this.windowSize.width < 950)
        return true
      else
        return false
    }
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
