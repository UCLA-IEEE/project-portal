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

            temp.date = self.parseDate(raw[j].gsx$datemmddyyyy.$t)
            if (temp.date.absolute < new Date().getTime()) { continue; }  // If the event has already passed, skip it

            temp.id = globalId++
            temp.title = raw[j].gsx$name.$t
            temp.location = raw[j].gsx$location.$t
            refined.push(temp)
          }
          nPagesLoaded++

          if (nPagesLoaded == self.N_PAGES) {  // After loading last page, store and sort event data
            self.calEvents = refined

            self.calEvents.sort(function(a, b) { return a.date.absolute - b.date.absolute})
          }
        }

        xhr.open('GET', 'https://spreadsheets.google.com/feeds/list/19eixWfc2iZl5JbjN2JqfQxr1KIkt-bDJm7NZrAg6NBM/' + i + '/public/values?alt=json')
        xhr.send()
      }
    },
    parseDate: function (raw) {
      var temp = { 'absolute': null, 'formatted': null} // absolute: date in milliseconds, formatted: display formatting
      var date = new Date(raw)
      temp.absolute = date.getTime()

      var day = date.getDate().toString()

      var month
      switch (date.getMonth()) {
        case 0:   month = 'jan';    break;
        case 1:   month = 'feb';    break;
        case 2:   month = 'mar';    break;
        case 3:   month = 'apr';    break;
        case 4:   month = 'may';    break;
        case 5:   month = 'jun';    break;
        case 6:   month = 'jul';    break;
        case 7:   month = 'aug';    break;
        case 8:   month = 'sep';    break;
        case 9:   month = 'oct';    break;
        case 10:  month = 'nov';    break;
        case 11:  month = 'dec';    break;
      }

      temp.formatted = month + ' ' + day
      return temp
    }
  },
  data() {
    return {
      calEvents: [],
      N_PAGES: 2
    }
  }
}
</script>

<style>
</style>
