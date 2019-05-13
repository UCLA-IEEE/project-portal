<template>
  <div>
    <h1>Micromouse</h1>
    <p>Here is some information. This is the Micromouse page</p>
    <SpecListing project="Micromouse"/>
  </div>
</template>

<script>
import SpecListing from "./SpecListing"
export default {
  name: 'Micromouse', //this is the name of the component
  components: {
    SpecListing
  }
}
</script>
<style>
</style>
