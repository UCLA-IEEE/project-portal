<template>
  <div class="container">
        <div class="checkoffs">
            <h1 class="title" id="checkoff-title">Checkoffs</h1>
            <CheckoffTile v-for="project in projects" :project='project' :key="project.id"></CheckoffTile>
        </div>
        <div class="roster">
            <div id="roster-contents">
                <h1 class="title" id="roster-title">Roster</h1>
                <hr>
                <input type="text" placeholder="Search members">
                <RosterTile v-for="member in members" :member='member' :key='member.id'></RosterTile>
            </div>
        </div>
    </div>
</template>

<script>
import CheckoffTile from './CheckoffTile'
import RosterTile from './RosterTile'

export default {
  name: 'Checkoffs', //this is the name of the component
  components: {
      CheckoffTile,
      RosterTile
  },
  data() {
      return {
          projects: [
              {
                  id: 1,
                  title: "Project 1",
                  subtitle: "Something Something",
                  progress: 67
              },
              {
                  id: 2,
                  title: "Project 2",
                  subtitle: "Breadboarding: Checkpoint 1",
                  progress: 67
              },
              {
                  id: 3,
                  title: "Project 2",
                  subtitle: "Breadboarding: Checkpoint 2",
                  progress: 67
              },
              {
                  id: 4,
                  title: "Project 3",
                  subtitle: "I Love Computer Science",
                  progress: 67
              },
              {
                  id: 5,
                  title: "Project 4",
                  subtitle: "Something pt 2: Electric Boogaloo",
                  progress: 67
              }
          ],
          members: [
            {
                id: 1,
                name: "Kathy Daniels",
                progress: 50
            },
            {
                id: 2,
                name: "Robert Peralta",
                progress: 80
            },
            {
                id: 3,
                name: "Michelle Lam",
                progress: 60
            },
            {
                id: 4,
                name: "Jiwan Kang",
                progress: 40
            },
            {
                id: 5,
                name: "Michelle Tan",
                progress: 90
            },
            {
                id: 6,
                name: "Serene Kamal",
                progress: 40
            },
            {
                id: 7,
                name: "Eugene Lo",
                progress: 60
            },
            {
                id: 8,
                name: "John Doe",
                progress: 100
            },
            {
                id: 9,
                name: "Josephine Bruin",
                progress: 30
            },
            {
                id: 10,
                name: "Jeffrey Chan",
                progress: 50
            },
            {
                id: 11,
                name: "Robert Downey, Jr.",
                progress: 10
            },
            {
                id: 12,
                name: "Anonymous",
                progress: 0
            },
            {
                id: 13,
                name: "Josephine Bruin",
                progress: 90
            },
            {
                id: 14,
                name: "Maggie Huang",
                progress: 40
            },
            {
                id: 15,
                name: "Robert Peralta",
                progress: 50
            },
            {
                id: 16,
                name: "Robert Zalog",
                progress: 80
            },
            {
                id: 17,
                name: "Kathy Daniels",
                progress: 100
            },
            {
                id: 18,
                name: "Roselyn Lee",
                progress: 80
            },
            {
                id: 19,
                name: "Maggie Huang",
                progress: 20
            },
            {
                id: 20,
                name: "Roselyn Lee",
                progress: 30
            },
            {
                id: 21,
                name: "Jeffrey Chan",
                progress: 10
            }
        ]
      }
  }
}
</script>

<style>
    .container {
    display: grid;
    grid-template-columns: 70% 30%;
    grid-column-gap: 50px;
    margin: 25px 100px;
    }

    .checkoffs {
        background: #FFFFFF;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);   
        grid-column-start: 1;
        grid-column-end: 2;
}

    .roster {
        text-align: left;
        grid-column-start: 2;
        grid-column-end: 3;
        border-left: 1px solid rgb(124, 158, 179);
    }

    .title {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        color: #1F6891;
        font-weight: 450;
        text-transform: uppercase;
        margin-top: 25px;
    }


    #roster-title {
        font-size: 18px;
        line-height: 24px;
    }
    
    #roster-contents {
        margin-left: 40px;
        line-height: 40px;
    }

    #member-progress {
        width: 30%;
        display: inline-block;
    }

    input {
        height: 24px;
        border: 1px solid rgb(124, 158, 179);
        border-radius: 5px;
        padding-left: 10px;
        width: 90%;
    }


 

</style>
