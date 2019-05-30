<template>
  <div class="mobile-navbar">
    <img class="mobile-logo" src="../../public/ieee-logo.png"/>
    <svg class="mobile-menu" @click="clickMenu" :style="{ fill: menuColor }">
      <rect class="rectangle" y="0"/>
      <rect class="rectangle" y="8"/>
      <rect class="rectangle" y="16"/>
    </svg>
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
          text: 'Home',
          page:'/'
        },
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
  .mobile-navbar {
    display: flex;
    height: 45px;
    margin: 10px 15px;
    padding: 10px 20px;
    align-items: center;
    justify-content: space-between;
  }
  .mobile-menu {
    height: 18px;
    width: 24px;
  }
  .rectangle {
    height: 2px;
    width: 24px;
  }
  .mobile-logo {
    width: 45px;
  }
</style>
