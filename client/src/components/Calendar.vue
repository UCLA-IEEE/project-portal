<template>
  <div class="calendar">
    <CalendarEvent v-for="calEvent in calEvents" :key="calEvent.id" :calEvent="calEvent"/>
  </div>
</template>

<script>
import CalendarEvent from "./CalendarEvent"
export default {
  name: "Calendar",
  components: {
    CalendarEvent
  },
  data() {
    return {
      calEvents: [
        {
          id: 1,
          date: "nov 18",
          title: "Project 7 Deadline",
        },
        {
          id: 2,
          date: "nov 30",
          title: "Project 8 Lecture",
          location: "ENGR IV 6302",
          link: "http://ieeebruins.org/",
        },
        {
          id: 3,
          date: "dec 15",
          title: "IEEE Barbecue Social",
          location: "Sunset Rec Lawn",
          link: "https://www.facebook.com/groups/uclaieee/",
        },
        {
          id: 4,
          date: "dec 20",
          title: "Winter Break Starts",
        },
      ]
    }
  }
}
</script>

<style>
</style>
