<template>
  <div class='navbar'>
    <img class='logo' src='../../public/ieee-logo.png'>
    <ul class='project-list'>
      <li class='project' v-for="routes in links">
        <router-link v-bind:key="routes.id"
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
    height: 55px;
    margin: 10px 100px;
    padding: 0 50px 0px 50px;
  }
  .logo {
    float: left;
    width: 45px;
  }
  .project-list {
    float: right;
    margin: 10px 5px;
  }
  .project {
    display: inline;
    margin-left: 50px;
  }
  a {
    color: black;
    text-decoration: none;
    font-size: 13px;
    text-transform: uppercase;
  }
</style>
