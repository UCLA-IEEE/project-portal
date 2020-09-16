<template>
  <div>
    <div id='navbar' :class="{'shadow--6dp': isScrolled}">
      <router-link :to="`/login`"><img class='logo' src='../../public/desktop-logo.svg'></router-link>

      <div style="display: flex;" v-if="onPublic">
        <ul class='link-list'>
          <li class='link'>
            <router-link class="font-fix" :to="`/register`">Sign Up</router-link>
          </li>
        </ul>
        <router-link class='main-button' :to="`/login`" tag="button">
          <p class="font-fix">Sign In</p>
        </router-link>
      </div>

      <div style="display: flex;" v-else>
        <ul class='link-list'>
          <li class='link' v-for="routes in links" :key="routes.id">
            <router-link class="font-fix" :key="routes.id" :to="`${routes.page}`">{{routes.text}}</router-link>
          </li>
        </ul>

        <div class="button-wrapper">
          <router-link class='main-button' :to="`/me`" tag="button">
            <p class="font-fix">Me</p>
          </router-link>
          <div class="drop card text-center" :class="[isScrolled ? 'shadow--4dp' : 'shadow--2dp']">
            <a @click="logout">
              Sign Out
            </a>
          </div>
        </div>
      </div>

    </div>

    <div id='mobile-navbar'>

    </div>
  </div>
</template>

<script>
import { debounce } from "debounce";
export default {
  name: 'Nav',
  data() {
    return {
      isScrolled: false,
      links: [
        {
          id: 1,
          text: 'ops',
          page:'/ops'
        },
        {
          id: 2,
          text: 'mm',
          page:'/mm'
        },
        {
          id: 3,
          text: 'ap',
          page:'/ap'
        },
        {
          id: 4,
          text: 'dav',
          page: '/dav'
        }
      ]
    }
  },
  created() {
    this.debouncedHandleScroll = debounce(this.handleScroll, 0);
    window.addEventListener("scroll", this.debouncedHandleScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.debouncedHandleScroll);
  },
  methods: {
    logout() {
      this.$store.commit('logout');
      if (!this.$store.getters.authenticated)
        this.$router.push({name: "Login"});
    },
    handleScroll() {
      if (window.scrollY > 10)
        this.isScrolled = true;
      else
        this.isScrolled = false;
    }
  },
  computed: {
    onPublic: function() {
      const publicPages = ["Login", "Register", "Reset", "Verify"]
      return publicPages.includes(this.$route.name)
    }
  }
}
</script>

<style>
  /* Desktop Navbar */
  #navbar {
    display: none;
    align-items: center;
    justify-content: space-between;

    position: fixed;
    background-color: var(--off-white);

    width: 100%;
    padding: 10px 20px;

    transition: box-shadow .2s;
  }

  #navbar .logo {
    height: 48px;
  }

  #navbar .link-list {
    margin: 10px 10px 10px 5px;

    display: inline-flex;
    align-items: center;
  }

  #navbar li {
    display: inline;
    margin: 0 30px;
  }

  #navbar .main-button {
    display: inline-block;
    font-size: 14px;
    padding: 7px 15px;
    width: 90px;

    position: relative;
    z-index: 10;
  }

  #navbar a {
    color: var(--off-black);
    text-decoration: none;
    text-transform: uppercase;
  }

  #navbar .link-list a:hover, 
  #navbar .link-list a:focus,
  #navbar .link-list a.router-link-active {
    color: var(--off-black);
    border-bottom: 1px solid var(--off-black);
  }

  #navbar .button-wrapper {
    display: inline-block;
    position: relative;

    width: 106px;
    height: 40.8px;

    padding: 0 8px;
    margin: 0 -8px;

    overflow: hidden;

    transition: all .2s;
  }

  #navbar .button-wrapper:hover {
    height: 85.8px;
    margin-bottom: -45px;

    transition: all 0s;
  }

  #navbar .button-wrapper:hover .main-button {
    background-color: var(--blue);
    color: var(--white);
  }

  #navbar .button-wrapper:hover .drop {
    opacity: 1;
    top: 0;
  }

  #navbar .drop {
    display: inline-block;
    position: relative;
    z-index: 9;
    width: 90px;
    top: -10px;
    opacity: 0;

    padding: 9.8px 0 7px;

    transition: all 0.2s;
  }

  #navbar .drop a:hover {
    cursor: pointer;
  }

  /* Mobile Navbar */

  /* Media Queries */
  @media only screen and (min-width: 768px) {
    #navbar {
      display: flex;
    }

    #mobile-navbar {
      display: none;
    }
  }

  @media only screen and (min-width: 992px) {
    #navbar {
      padding: 10px 50px;
    }
  }
</style>
