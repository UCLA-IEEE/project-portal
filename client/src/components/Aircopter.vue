<template>
  <div>
    <h1>Aircopter</h1>
    <p>Here is some information. This is the Aircopter page</p>
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
</style>
