<template>
  <div id='navbar'>
    <router-link :to="`/login`"><img class='logo' src='../../public/ieee-logo.png'></router-link>
    <ul class='project-list'>
      <li class='project' v-for="routes in links" v-bind:key="routes.id">
        <router-link v-bind:key="routes.id"
        :to="`${routes.page}`">{{routes.text}}</router-link>
      </li>
      <button class='sign-button' v-if="!this.$store.state.authenticated" v-on:click="redirectLogin()">
        <router-link :to="`/Login`">Sign In</router-link>
      </button>
      <button class='sign-button' v-else v-on:click="handleLogout()">
        <router-link :to="`/Login`">Sign Out</router-link>
      </button>
    </ul>
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
          text: 'OPS',
          page:'/OPS'
        },
        {
          id: 2,
          text: 'Micromouse',
          page:'/Micromouse'
        },
        {
          id: 3,
          text: 'Aircopter',
          page:'/Aircopter'
        },
        {
          id: 4,
          text: 'Secure',
          page: '/secure'
        }
      ]
    }
  },
  methods: {
    redirectLogin() {
      this.$router.replace({ name: "Login" });
    },
    handleLogout() {
      this.$store.commit('logout');
      if(!this.$store.getters.authenticated) {
        this.$router.replace({ name: "Login" });
      }
    }
  }
}
</script>

<style>
  #navbar {
    border-bottom: 0.3px solid black;
    height: 60px;
    margin: 10px 100px;
    padding: 0 50px 0px 50px;
  }

  #navbar .logo {
    float: left;
    width: 160px;
    margin-top: 5px;
  }
  #navbar .project-list {
    float: right;
    margin: 10px 5px;
  }
  #navbar .project {
    display: inline;
    margin: 0 30px;
  }
  #navbar .sign-button {
    background-color: #1F6891;
    color: white;
    padding: 8px 20px;
    border: none;
    border-radius: 5px;
    margin-left: 30px;
    transition: background-color 0.2s ease;
  }
  #navbar .sign-button:hover {
    background-color: #68A0BF;
  }
  #navbar .sign-button a {
    color: white !important;
    transition: color 0.3s ease;
  }
  #navbar .sign-button a:hover {
    border-bottom: none;
  }
  #navbar a {
    color: black;
    text-decoration: none;
    font-size: 13px;
    text-transform: uppercase;
  }
  #navbar .project a:hover {
    color: black;
    border-bottom: 1px solid black;
  }

  #navbar .project-list a:hover, 
  #navbar .project-list a:focus {
    color: black; 
    text-decoration: none;
  }
</style>
