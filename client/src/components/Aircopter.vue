<template>
  <div>
    <h1 class="page-title">Aircopter</h1>
    <SpecListing project="Aircopter"/>
  </div>
</template>

<script>
import SpecListing from "./SpecListing"
export default {
  name: 'Aircopter', //this is the name of the component
  components: {
    SpecListing
  }
}
</script>
<style>
.page-title {
  position: absolute;
  left: 150px;
  top: 90px;

  text-transform: uppercase;
  font-weight: 500;
  font-size: 24px;
  color: #1F6891;
}

@media all and (max-width: 950px) {
  .page-title {
    left: 35px;
  }
}
</style>
