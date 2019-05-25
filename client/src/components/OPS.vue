<template>
  <div class="ops-page">
    <h1 class="ops-title">Open Project Space</h1>
    <SpecListing class="ops-list" project="OPS"/>
    <Sidebar class="ops-sidebar"/>
  </div>
</template>

<script>
import SpecListing from "./SpecListing"
import Sidebar from "./Sidebar"
export default {
  name: 'OPS',
  components: {
    SpecListing,
    Sidebar
  }
}
</script>

<style>
.ops-page {
  display: grid;
  grid-template-columns: auto 350px;
  grid-template-rows: 70px auto;
  grid-template-areas: 'title sidebar'
                     'listing sidebar';
}
.ops-title {
  grid-area: title;
  margin-top: 30px;
  margin-left: 150px;

  text-align: left;
  text-transform: uppercase;
  font-weight: 500;
  font-size: 24px;
  color: #1F6891;
}
.ops-list {
  grid-area: listing;
}
.ops-sidebar {
  grid-area: sidebar;
}

@media all and (max-width: 950px) {
  .ops-title {
    left: 35px;
  }
}
</style>
