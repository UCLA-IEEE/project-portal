<template>
  <div class="mobile-navbar">
    <div class="mobile-navbar-main">
      <img class="mobile-logo" src="../../public/mobile-ieee-logo.png"/>
      <svg class="mobile-icon" @click="clickMenu" :style="{ fill: menuColor }">
        <rect class="rectangle" y="0"/>
        <rect class="rectangle" y="8"/>
        <rect class="rectangle" y="16"/>
      </svg>
    </div>
    <div :class="[dropdownBase, displayMenu ? dropdownDisplay : '']" :style="{ width: dropWidth }">
      <router-link class="mobile-links" v-for="routes in links"
        :key="routes.id" :to="`${routes.page}`">{{routes.text}}</router-link>
      <router-link class="mobile-links" :to="`/Login`" v-if="!this.$store.getters.authenticated"
        @click="redirectLogin()">Sign In</router-link>
      <router-link class="mobile-links" :to="`/Login`" v-else
        @click.native="handleLogout()">Sign Out</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "MobileNavigation",
  props: {
    width: Number
  },
  data() {
    return {
      links: [
        {
          id: 0,
          text: 'OPS',
          page:'/OPS'
        },
        {
          id: 1,
          text: 'MM',
          page:'/Micromouse'
        },
        {
          id: 2,
          text: 'AP',
          page:'/Aircopter'
        },
        {
          id: 3,
          text: 'Secure',
          page: '/secure'
        }
      ],
      displayMenu: false,
      dropdownBase: "mobile-dropdown",
      dropdownDisplay: "mobile-dropdown-display"
    }
  },
  methods: {
    clickMenu: function() {
      if (!this.displayMenu)
        this.displayMenu = true
      else
        this.displayMenu = false
    },
    redirectLogin() {
      this.$router.replace({ name: "Login" });
    },
    handleLogout() {
      this.$store.commit('logout');
      if(!this.$store.getters.authenticated) {
        this.$router.replace({ name: "Login" });
      }
    }
  },
  computed: {
    menuColor: function() {
      if (this.displayMenu)
        return "rgba(31, 104, 145, 0.4)"
      return "#1F6891"
    },
    dropWidth: function() {
      var offset = 16 + .1*this.width
      return ((this.width - offset).toString() + "px")
    }
  }
}
</script>

<style>
  .mobile-dropdown, 
  .mobile-dropdown-display, 
  .mobile-icon, 
  .mobile-logo, 
  .mobile-navbar-main {
    box-sizing: content-box;
  }

  .mobile-navbar-main {
    position: relative;
    display: flex;
    height: 45px;
    padding: 10px 20px;
    margin: 8px;
    align-items: center;
    justify-content: space-between;
    z-index: 1;

    background-color: white;
    border-bottom: .3px solid black;
  }

  .mobile-icon {
    height: 18px;
    width: 24px;
    transition: fill .3s;
  }

  .rectangle {
    height: 2px;
    width: 24px;
  }

  .mobile-logo {
    width: 45px;
  }

  .mobile-dropdown {
    position: absolute;
    top: 5px;
    display: flex;
    height: 40px;
    padding: 10px 5%;
    margin: 8px;
    align-items: center;
    justify-content: space-around;
    z-index: 0;

    background: rgba(31, 104, 145, 0.85);
    transition: top .3s;
  }

  .mobile-dropdown-display {
    top: 65px;
  }

  .mobile-dropdown a, .mobile-sign-button a {
    color: white;
  }

  .mobile-dropdown a:hover {
    border-bottom: 1px solid white;
    text-decoration: none;
  }

  .mobile-dropdown a:focus {
    text-decoration: none;
  }
</style>
