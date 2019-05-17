<template>
  <div>
    <h1 class="ops-title">Open Project Space</h1>
    <SpecListing project="OPS"/>
  </div>
</template>

<script>
import SpecListing from "./SpecListing"
export default {
  name: 'OPS',
  components: {
    SpecListing
  }
}
</script>

<style>
.ops-title {
  position: absolute;
  left: 150px;
  top: 90px;

  text-transform: uppercase;
  font-weight: 500;
  font-size: 24px;
  color: #1F6891;
}

@media all and (max-width: 950px) {
  .ops-title {
    left: 35px;
  }
}
</style>
