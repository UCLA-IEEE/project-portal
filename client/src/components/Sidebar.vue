<template>
  <div class="sidebar">
    <p class="section-title">Upcoming Dates</p>
    <Calendar/>
    <p class="section-title">All Projects</p>
    <p class="section-title">Keep Updated</p>
  </div>
</template>

<script>
import Calendar from "./Calendar"
export default {
  name: "Sidebar",
  components: {
    Calendar
  },
}
</script>

<style>
.sidebar {
  height: 600px;
  margin: 25px 0px;
  padding: 10px 35px;
}
.sidebar:after {
  content: "";
  height: 90%;
  width: 1px;

  position: absolute;
  right: 350px;
  top: 110px;
  background-color: rgba(31, 104, 145, 0.5);
}
.section-title {
  width: 220px;
  border-bottom: 1px solid rgba(31, 104, 145, 0.5);

  text-transform: uppercase;
  text-align: left;
  font-weight: 500;
  font-size: 14px;
  line-height: 40px;
  color: #1F6891;
}
</style>
