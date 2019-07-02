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
  props: {
    project: String
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
      for (i = 1; i <= this.N_PAGES; i++) {
        var xhr = new XMLHttpRequest()

        xhr.onload = function () {
          var raw = JSON.parse(this.responseText)

          var pageNum
          switch (raw.feed.title.$t) {    // Get page number in async xmlhttprequests
            case 'Fall':                        pageNum = 1;  break;
            case 'Fall Project Deadlines':      pageNum = 2;  break;
            case 'Winter':                      pageNum = 3;  break;
            case 'Winter Project Deadlines':    pageNum = 4;  break;
            case 'Spring':                      pageNum = 5;  break;
            case 'Spring Project Deadlines':    pageNum = 6;  break;
          }

          raw = raw.feed.entry
          if (pageNum > 2)      // Remove extra formatting row for pages 3 - 6
            delete raw[1]
          delete raw[0]         // Remove formatting row

          var j
          for (j in raw) {      // Extract necessary fields
            var temp = { 'id': null, 'date': null, 'title': null, 'location': null }

            if (pageNum > 2) {
              temp.date = self.parseDate(raw[j].gsx$datemdyy.$t)    // Handle different formatting for pages 3 - 6
            } else {
              temp.date = self.parseDate(raw[j].gsx$datemmddyyyy.$t)
            }
            
            /*
             * Skip an event if:
             *   * It has already passed
             *   * It doesn't belong on the calendar (pages 3 - 6)
             *   * It isn't relevant to the current project page
             */

            if ((temp.date.absolute < new Date().getTime()) || 
                (pageNum > 2 && raw[j].gsx$leaveoffcalendaryesno.$t.toLowerCase() == 'yes') || 
                (pageNum % 2 == 0 && raw[j].gsx$project.$t != '' && raw[j].gsx$project.$t != self.project)) { continue; } 

            temp.id = globalId++
            temp.title = raw[j].gsx$name.$t
            temp.location = raw[j].gsx$location.$t
            refined.push(temp)
          }
          nPagesLoaded++

          if (nPagesLoaded == self.N_PAGES) {  // After loading last page
            self.calEvents = refined     // Store data in global variable

            self.calEvents.sort(function(a, b) { return a.date.absolute - b.date.absolute })   // Sort events by date
            self.calEvents = self.calEvents.slice(0, 4) // Only display first 4 events
          }
        }

        xhr.open('GET', 'https://spreadsheets.google.com/feeds/list/19eixWfc2iZl5JbjN2JqfQxr1KIkt-bDJm7NZrAg6NBM/' + i + '/public/values?alt=json')
        xhr.send()
      }
    },

    parseDate: function (raw) {
      var temp = { 'absolute': null, 'formatted': null } // absolute: date in milliseconds, formatted: display formatting

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
