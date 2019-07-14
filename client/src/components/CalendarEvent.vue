<template>
  <a class="calendar-event" :href="calEvent.link">
    <div class="date-background">
      <p class="event-date">{{calEvent.date}}</p>
    </div>
    <div class="event-info">
      <p class="event-title">{{calEvent.title}}</p>
      <p class="event-location">{{calEvent.location}}</p>
    </div>
  </a>
</template>

<script>
export default {
  name: "CalendarEvent",
  props: {
    calEvent: Object
  }
}
</script>

<style>
.calendar-event {
  width: 250px;
  height: 55px;
  margin: 10px;

  display: grid;
  grid-template-columns: 55px auto;
  grid-template-rows: 55px;
  grid-column-gap: 20px;
  grid-template-areas: 'date info';
}
.date-background {
  grid-area: date;

  height: 55px;
  width: 55px;

  background: #1F6891;
  border-radius: 5px;
}
.event-date {
  position: relative;
  bottom: 6px;
  left: 7.5px;

  height: 40px;
  width: 40px;

  text-transform: uppercase;
  text-align: center;
  color: white;
}
.event-info {
  grid-area: info;
  margin: 10px 0px;

  font-size: 13px;
}
.event-title {
  margin: 0px;
}
.event-location {
  margin: 0px;
  font-size: 11px;
  color: #4684A7;
}
</style>
