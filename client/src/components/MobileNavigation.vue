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
    <div class="mobile-dropdown" v-show="displayMenu">
      <router-link class="mobile-links" v-for="routes in links"
      :key="routes.id" :to="`${routes.page}`">{{routes.text}}</router-link>
      <button class='mobile-sign-button' v-if="!this.$store.state.authenticated" v-on:click="redirectLogin()">
        <router-link :to="`/Login`">Sign In</router-link>
      </button>
      <button class='mobile-sign-button' v-else v-on:click="handleLogout()">
        <router-link :to="`/Login`">Sign Out</router-link>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "MobileNavigation",
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
          id: 4,
          text: 'Secure',
          page: '/secure'
        }
      ],
      displayMenu: false
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
      this.$store.commit('updateAuthenticated', false);
      if(!this.$store.state.authenticated) {
        this.$router.replace({ name: "Login" });
      }
    }
  },
  computed: {
    menuColor: function() {
      if (this.displayMenu)
        return "rgba(31, 104, 145, 0.4)"
      return "#1F6891"
    }
  }
}
</script>

<style>
  .mobile-navbar-main {
    display: flex;
    height: 45px;
    padding: 10px 20px;
    align-items: center;
    justify-content: space-between;

    background-color: white;
    box-shadow: 0px 5px 5px rgba(0, 0, 0, 0.2);
  }
  .mobile-icon {
    height: 18px;
    width: 24px;
    transition: fill .5s;
  }
  .rectangle {
    height: 2px;
    width: 24px;
  }
  .mobile-logo {
    width: 45px;
  }

  .mobile-dropdown {
    display: flex;
    height: 40px;
    width: inherit;
    padding: 10px 40px;
    align-items: center;
    justify-content: space-between;

    background: rgba(31, 104, 145, 0.85);
    box-shadow: 0px 5px 5px rgba(0, 0, 0, 0.2);
  }
  .mobile-dropdown a, .mobile-sign-button a {
    color: white;
  }
  .mobile-dropdown a:hover {
    border-bottom: 1px solid white;
  }
  .mobile-sign-button a:hover {
    border-bottom: none;
  }
  .mobile-sign-button {
    background-color: inherit;
    padding: 8px 20px;
    border: 1px solid white;
    border-radius: 5px;
    margin-left: 30px;
  }
</style>
