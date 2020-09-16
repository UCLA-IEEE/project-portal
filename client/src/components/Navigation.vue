<template>
  <div>
    <div id='navbar'>
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
          <div class="drop card text-center">
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
export default {
  name: 'Nav',
  data() {
    return {
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
  methods: {
    logout() {
      this.$store.commit('logout');
      if (!this.$store.getters.authenticated)
        this.$router.push({name: "Login"});
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

    margin: 10px 0;
    padding: 0 20px;
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

    width: 100px;
    height: 40.8px;

    padding: 0 5px;
    margin: 0 -5px;

    overflow: hidden;

    transition: all .2s;
  }

  #navbar .button-wrapper:hover {
    height: 82.8px;
    margin-bottom: -42px;

    transition: all 0s;
  }

  #navbar .button-wrapper:hover .main-button {
    background-color: var(--blue);
    color: var(--white);
  }

  #navbar .button-wrapper:hover .drop {
    opacity: 1;
    top: 0;

    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14),
    0 3px 1px -2px rgba(0, 0, 0, 0.2),
    0 1px 5px 0 rgba(0, 0, 0, 0.12);
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
      padding: 0 50px;
    }
  }
</style>
