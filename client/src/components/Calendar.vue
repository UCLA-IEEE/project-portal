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

      // Loading data from first 2 pages of spreadsheet

      var i
      for (i = 1; i <= 2; i++) {
        var xhr = new XMLHttpRequest()

        xhr.onload = function () {
          var raw = JSON.parse(this.responseText)
          raw = raw.feed.entry
          if (raw.length > 1) {  // Only process the page if there are events on it
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

      // Loading data from last 4 pages of spreadsheet

      for (i = 3; i <= self.N_PAGES; i++) {
        var xhr = new XMLHttpRequest()

        xhr.onload = function () {
          var raw = JSON.parse(this.responseText)
          raw = raw.feed.entry
          if (raw.length > 2) {  // Only process the page if there are events on it
            delete raw[0]    // Remove formatting rows
            delete raw[1]
            var j
            for (j in raw) { // Extract necessary fields
              var temp = { 'id': null, 'date': null, 'title': null, 'location': null }

              temp.date = self.parseDate(raw[j].gsx$datemdyy.$t)
              if (temp.date.absolute < new Date().getTime() || 
                  raw[j].gsx$leaveoffcalendaryesno.$t == 'Yes' || 
                  raw[j].gsx$leaveoffcalendaryesno.$t == 'yes') 
                  { continue; }  // If the event has already passed or doesn't belong on the calendar, skip it

              temp.id = globalId++
              temp.title = raw[j].gsx$name.$t
              temp.location = raw[j].gsx$location.$t
              refined.push(temp)
            }
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

      if (isNaN(raw[0])) {  // If the first char isn't a number, the string requires trimming
        var i
        for (i in raw) {
          if (!isNaN(raw[i])) {   // On finding the first number, exit the loop
            break;
          }
        }
        raw = raw.substring(i)
      }

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
      N_PAGES: 6
    }
  }
}
</script>

<style>
</style>
