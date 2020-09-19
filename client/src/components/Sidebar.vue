<template>
  <div class="sidebar">
    <p class="section-title">Upcoming Dates</p>
    <Calendar/>
    <p class="section-title">All Projects</p>
      <router-link v-for="project in projects" :key="project.id" :to="project.link">
        <p class="sidebar-project">{{project.title}}</p>
      </router-link>
    <p class="section-title">Keep Updated</p>
      <div class="sidebar-media">
        <a :href="facebook">
          <img class="facebook" src="../../public/facebook.png"/>
        </a>
        <a href="https://uclaieee.slack.com/">
          <img class="slack" src="../../public/slack.png"/>
        </a>
        <a href="https://www.instagram.com/uclaieee/">
          <img class="instagram" src="../../public/instagram.png"/>
        </a>
      </div>
  </div>
</template>

<script>
import Calendar from "./Calendar"
export default {
  name: "Sidebar",
  components: {
    Calendar
  },
  props: {
    facebook: String
  },
  data() {
    return {
      projects: [
        {
          id: 1,
          title: "Project 1 - Something Something",
          link: "/Micromouse"
        },
        {
          id: 2,
          title: "Project 2 - Breadboarding",
          link: "/Micromouse"
        },
        {
          id: 3,
          title: "Project 3 - Something Something 2: Electric Boogaloo",
          link: "/Micromouse"
        },
        {
          id: 4,
          title: "Project 4 - I Love CS",
          link: "/Micromouse"
        }
      ],
    }
  },
}
</script>

<style scoped>
.sidebar {
  margin: 35px 0px;
  padding: 0px 90px 0px 35px;
  border-left: 1px solid rgba(31, 104, 145, 0.5);
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
.sidebar-project {
  margin-top: 7px;
  margin-bottom: 7px;
  margin-left: 5px;

  text-align: left;
  font-size: 13px;
  font-weight: 500;
  line-height: 20px;
  padding-left: 25px;
  text-indent: -25px;
}
.sidebar-media {
  position: relative;
  height: 20px;
  width: 90px;
  left: 5px;

  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 20px;
  grid-column-gap: 15px;
  grid-template-areas: "facebook slack instagram";
}
.facebook {
  height: 20px;
  width: 20px;

  grid-area: facebook;
}
.slack {
  height: 20px;
  width: 20px;

  grid-area: slack;
}
.instagram {
  height: 20px;
  width: 20px;

  grid-area: instagram;
}
</style>
