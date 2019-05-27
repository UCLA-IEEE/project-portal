<template>
  <div class="mm-page">
    <h1 class="mm-title">Micromouse</h1>
    <SpecListing class="mm-list" project="Micromouse"/>
    <Sidebar class="mm-sidebar" v-if="sidebar" facebook="https://www.facebook.com/groups/456491081426382/"/> <!-- REPLACE LINK FOR NEW YEAR -->
  </div>
</template>

<script>
import SpecListing from "./SpecListing"
import Sidebar from "./Sidebar"
export default {
  name: 'Micromouse',
  components: {
    SpecListing,
    Sidebar
  },
  data() {
    return {
      sidebar: true
    }
  },
  mounted: function() {
    window.addEventListener('resize', this.handleResize);
    this.handleResize();
  },
  beforeDestroy: function() {
    window.removeEventListener('resize', this.handleResize);
  },
  methods: {
    handleResize: function() {
      var width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
      if (width < 950)
        this.sidebar = false;
      else
        this.sidebar = true;
    }
  }
}
</script>

<style>
.mm-page {
  display: grid;
  grid-template-columns: auto 350px;
  grid-template-rows: 70px auto;
  grid-template-areas: 'title sidebar'
                     'listing sidebar';
}

.mm-title {
  grid-area: title;
  margin-top: 30px;
  margin-left: 150px;

  text-align: left;
  text-transform: uppercase;
  font-weight: 500;
  font-size: 24px;
  color: #1F6891;
}

.mm-list {
  grid-area: listing;
}

.mm-sidebar {
  grid-area: sidebar;
}

@media all and (max-width: 950px) {
  .mm-page {
    grid-template-columns: auto;
    grid-template-areas: 'title'
                         'listing';
  }

  .mm-title {
    margin-left: 35px;
  }
}
</style>
