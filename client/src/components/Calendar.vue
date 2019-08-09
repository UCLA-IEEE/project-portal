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
  data() {
    return {
      calEvents: [],
      MAX_PAGES: 10,  // Max number of pages the algorithm will attempt to load
      N_PAGES: 6      // Number of pages the algorithm will import from
    }
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
      var finishedPages = false

      var i = 1
      while (!finishedPages && i <= this.MAX_PAGES) {
        var xhr = new XMLHttpRequest()

        xhr.onreadystatechange = function () {
          if (this.status == 400) {   // 400 bad request means past the end of the spreadsheet
            this.abort()
            self.finishedPages = true
          }
        }

        xhr.onload = function () {
          var raw = JSON.parse(this.responseText)

          var extraFormatting = false
          var isProject = false
          switch (raw.feed.title.$t) {    // Check page number in async xmlhttprequests
            case 'Fall Project Deadlines':      isProject = true;        
            case 'Fall':                        extraFormatting = false;  break;
            case 'Winter Project Deadlines':    isProject = true;
            case 'Winter':                      extraFormatting = true;  break;     // Winter and spring pages have extra formatting
            case 'Spring Project Deadlines':    isProject = true;
            case 'Spring':                      extraFormatting = true;  break;
            default:                            return;   // Do nothing if the page is not one of the expected pages
          }

          raw = raw.feed.entry
          if (extraFormatting)      // Remove extra formatting row
            delete raw[1]
          delete raw[0]         // Remove formatting row

          var j
          for (j in raw) {      // Extract necessary fields
            var temp = { 'id': null, 'date': null, 'title': null, 'location': null }

            try {
              temp.date = self.parseDate(raw[j].gsx$datemdyy.$t)
            }
            catch {
              temp.date = self.parseDate(raw[j].gsx$datemmddyyyy.$t)  // To handle inconsistent formatting
            }   
            
            /*
             * Skip an event if:
             *   * It has already passed
             *   * It doesn't belong on the calendar (extra formatting)
             *   * It isn't relevant to the current project page
             */

            if ((temp.date.absolute < new Date().getTime()) || 
                (extraFormatting && raw[j].gsx$leaveoffcalendaryesno.$t.toLowerCase() == 'yes') || 
                (isProject && raw[j].gsx$project.$t != '' && raw[j].gsx$project.$t != self.project)) { continue; } 

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

        i++
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
}
</script>

<style>
</style>
