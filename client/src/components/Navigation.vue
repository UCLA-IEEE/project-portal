<template>
  <div class='navbar'>
    <img class='logo' src='../../public/ieee-logo.png'>
    <ul class='project-list'>
      <li class='project' v-for="routes in links">
        <button v-if="routes.id == 0">
          <router-link v-bind:key="routes.id"
          :to="`${routes.page}`">{{routes.text}}</router-link>
        </button>
        <router-link v-else v-bind:key="routes.id"
        :to="`${routes.page}`">{{routes.text}}</router-link>
      </li>
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
          id: 0,
          text: 'Sign In',
          page:'/Login'
        }
      ]
    }
  }
}
</script>

<style>
  .navbar {
    border-bottom: 0.3px solid black;
    height: 60px;
    margin: 10px 100px;
    padding: 0 50px 0px 50px;
  }
  .logo {
    float: left;
    width: 160px;
    margin-top: 5px;
  }
  .project-list {
    float: right;
    margin: 10px 5px;
  }
  .project {
    display: inline;
    margin-left: 50px;
  }
  button {
    background-color: #1F6891;
    color: white;
    padding: 8px 20px;
    border: none;
    border-radius: 5px;
    transition: background-color 0.2s ease;
  }
  button:hover {
    background-color: #68A0BF;
  }
  button a {
    color: white;
    transition: color 0.3s ease;
  }
  button a:hover {
    border-bottom: none;
    color: white;
  }
  a {
    color: black;
    text-decoration: none;
    font-size: 13px;
    text-transform: uppercase;
  }
  a:hover {
    border-bottom: 1px solid black;
  }
</style>
