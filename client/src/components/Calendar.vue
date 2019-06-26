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
  created: function () {
    this.importEvents()
  },
  methods: {
    importEvents: function () {

      var self = this
      var globalId = 0  // Id element for v-bind:key
      var refined = []
      var nPagesLoaded = 0

      var i
      for (i = 1; i <= self.N_PAGES; i++) {   // Loads data for every page in the spreadsheet
        var xhr = new XMLHttpRequest()

        xhr.onload = function () {
          var raw = JSON.parse(this.responseText)
          raw = raw.feed.entry
          delete raw[0]    // Remove formatting row
          var j
          for (j in raw) { // Extract necessary fields
            var temp = { 'id': null, 'date': null, 'title': null, 'location': null }
            temp.id = globalId++
            temp.date = self.parseDate(raw[j].gsx$datemmddyyyy.$t)
            temp.title = raw[j].gsx$name.$t
            temp.location = raw[j].gsx$location.$t
            refined.push(temp)
          }
          nPagesLoaded++

          if (nPagesLoaded == self.N_PAGES) {  // After loading last page, store event data
            self.calEvents = refined
          }
        }

        xhr.open('GET', 'https://spreadsheets.google.com/feeds/list/19eixWfc2iZl5JbjN2JqfQxr1KIkt-bDJm7NZrAg6NBM/' + i + '/public/values?alt=json')
        xhr.send()
      }
    },
    parseDate: function (raw) {
      return raw
    }
  },
  data() {
    return {
      calEvents: [],
      N_PAGES: 6
    }
  }
}
</script>

<style>
</style>
