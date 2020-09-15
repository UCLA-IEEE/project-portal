<template>
  <div>
    <div id='navbar'>
      <router-link :to="`/login`"><img class='logo' src='../../public/desktop-logo.svg'></router-link>

      <div v-if="onPublic">
        <ul class='link-list'>
          <li class='link'>
            <router-link class="font-fix" :to="`/register`">Sign Up</router-link>
          </li>
        </ul>
        <router-link class='main-button' :to="`/login`" tag="button">
          <p class="font-fix">Sign In</p>
        </router-link>
      </div>

      <div v-else>
        <ul class='link-list'>
          <li class='link' v-for="routes in links" :key="routes.id">
            <router-link class="font-fix" :key="routes.id" :to="`${routes.page}`">{{routes.text}}</router-link>
          </li>
        </ul>
        <router-link class='main-button' :to="`/me`" tag="button">
          <p class="font-fix">Me</p>
        </router-link>
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
    display: flex;
    align-items: center;
    justify-content: space-between;

    margin: 10px 0;
    padding: 0 50px;
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

  /* Mobile Navbar */

  
</style>
