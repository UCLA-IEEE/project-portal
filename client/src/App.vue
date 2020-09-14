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
      var w = document.documentElement.clientWidth || document.body.clientWidth
      var h = document.documentElement.clientHeight || document.body.clientHeight
      this.windowSize.width = w
      this.windowSize.height = h
    }
  },
  computed: {
    mobile: function() {
      if (this.windowSize.width < 1105)
        return true
      else
        return false
    }
  }
}
</script>

<style>
/****** GLOBAL STYLES ******/

#app {
  /* Theme Colors */
  --blue: #1F6891;
  --gold: #A48623;
  --red: #CE0000;
  --white: #FFFFFF;
  --off-white: #F8F8F8;
  --gray: #A6A6A6;
  --off-black: #2B2B2B;

  font-family: 'Josefin Sans', Helvetica, Arial, sans-serif;
  color: var(--off-black);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Text */

h1 {
  font-size: 28px;
}

h2 {
  font-size: 20px;
}

h3 {
  font-size: 16px;
}

p {
  font-size: 14px;
}

/* Links */

a {
  color: var(--blue);
  text-decoration: underline;
}

a:hover {
  color: var(--gold);
  text-decoration: none;
}

/* Forms */

input,
select,
textarea {
  height: 30px;

  border: 2px solid var(--gray);
  border-radius: 5px;
  transition: border-color .3s;
}

input:focus,
select:focus,
textarea:focus {
  outline: none;
  border-color: var(--blue);
}

input:focus::placeholder,
textarea:focus::placeholder {
  color: transparent;
}

/* Buttons */

button {
  background-color: transparent;
  border: 2px solid var(--blue);
  color: var(--blue);
  font-size: 12px;
  text-transform: uppercase;

  padding: 7px 15px 5px;

  transition: .3s;
}

button:hover,
button.selected {
  background-color: var(--blue);
  color: var(--white)
}

/* Default Card */

.card {
  background-color: var(--white);
  border-radius: 5px;
}

/* Shadows */

.shadow--2dp {
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14),
    0 3px 1px -2px rgba(0, 0, 0, 0.2),
    0 1px 5px 0 rgba(0, 0, 0, 0.12);
}

.shadow--3dp {
    box-shadow: 0 3px 4px 0 rgba(0, 0, 0, 0.14),
    0 3px 3px -2px rgba(0, 0, 0, 0.2),
    0 1px 8px 0 rgba(0, 0, 0, 0.12);
}

.shadow--4dp {
    box-shadow: 0 4px 5px 0 rgba(0, 0, 0, 0.14),
    0 1px 10px 0 rgba(0, 0, 0, 0.12),
    0 2px 4px -1px rgba(0, 0, 0, 0.2);
}

.shadow--6dp {
    box-shadow: 0 6px 10px 0 rgba(0, 0, 0, 0.14),
    0 1px 18px 0 rgba(0, 0, 0, 0.12),
    0 3px 5px -1px rgba(0, 0, 0, 0.2);
}

.shadow--8dp {
    box-shadow: 0 8px 10px 1px rgba(0, 0, 0, 0.14),
    0 3px 14px 2px rgba(0, 0, 0, 0.12),
    0 5px 5px -3px rgba(0, 0, 0, 0.2);
}

.shadow--16dp {
    box-shadow: 0 16px 24px 2px rgba(0, 0, 0, 0.14),
    0 6px 30px 5px rgba(0, 0, 0, 0.12),
    0 8px 10px -5px rgba(0, 0, 0, 0.2);
}

.shadow--24dp {
    box-shadow: 0 9px 46px 8px rgba(0, 0, 0, 0.14),
    0 11px 15px -7px rgba(0, 0, 0, 0.12),
    0 24px 38px 3px rgba(0, 0, 0, 0.2);
}
</style>
