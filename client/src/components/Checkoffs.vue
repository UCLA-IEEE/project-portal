<template>
  <div class="container">
        <div class="checkoffs">
            <h1 class="title" id="checkoff-title">Checkoffs</h1>
            <CheckoffTile v-for="project in projects" :project='project' :key="project.id"></CheckoffTile>
        </div>
        <div class="roster">
            <div >
                <h1 class="title" id="roster-title">Roster</h1>
                <hr>
                <input type="text" placeholder="Search members">
                <RosterTile v-for="member in members" :member='member' id="roster-contents" :key='member.id'></RosterTile>
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
                  progress: 2,
                  total: 3
              },
              {
                  id: 2,
                  title: "Project 2",
                  subtitle: "Breadboarding: Checkpoint 1",
                  progress: 2,
                  total: 3
              },
              {
                  id: 3,
                  title: "Project 2",
                  subtitle: "Breadboarding: Checkpoint 2",
                  progress: 1,
                  total: 3
              },
              {
                  id: 4,
                  title: "Project 3",
                  subtitle: "I Love Computer Science",
                  progress: 2,
                  total: 3
              },
              {
                  id: 5,
                  title: "Project 4",
                  subtitle: "Something pt 2: Electric Boogaloo",
                  progress: 1,
                  total: 3
              }
          ],
          members: [
            {
                id: 1,
                name: "Kathy Daniels",
                progress: 5,
                total: 10
            },
            {
                id: 2,
                name: "Robert Peralta",
                progress: 8,
                total: 10
            },
            {
                id: 3,
                name: "Michelle Lam",
                progress: 6,
                total: 10
            },
            {
                id: 4,
                name: "Jiwan Kang",
                progress: 4,
                total: 10
            },
            {
                id: 5,
                name: "Michelle Tan",
                progress: 9,
                total: 10
            },
            {
                id: 6,
                name: "Serene Kamal",
                progress: 4,
                total: 10
            },
            {
                id: 7,
                name: "Eugene Lo",
                progress: 6,
                total: 10
            },
            {
                id: 8,
                name: "John Doe",
                progress: 10,
                total: 10
            },
            {
                id: 9,
                name: "Josephine Bruin",
                progress: 3,
                total: 10
            },
            {
                id: 10,
                name: "Jeffrey Chan",
                progress: 5,
                total: 10
            },
            {
                id: 11,
                name: "Robert Downey, Jr.",
                progress: 1,
                total: 10
            },
            {
                id: 12,
                name: "Anonymous",
                progress: 0,
                total: 10
            },
            {
                id: 13,
                name: "Josephine Bruin",
                progress: 9,
                total: 10
            },
            {
                id: 14,
                name: "Maggie Huang",
                progress: 4,
                total: 10
            },
            {
                id: 15,
                name: "Robert Peralta",
                progress: 5,
                total: 10
            },
            {
                id: 16,
                name: "Robert Zalog",
                progress: 8,
                total: 10
            },
            {
                id: 17,
                name: "Kathy Daniels",
                progress: 10,
                total: 10
            },
            {
                id: 18,
                name: "Roselyn Lee",
                progress: 8,
                total: 10
            },
            {
                id: 19,
                name: "Maggie Huang",
                progress: 2,
                total: 10
            },
            {
                id: 20,
                name: "Roselyn Lee",
                progress: 3,
                total: 10
            },
            {
                id: 21,
                name: "Jeffrey Chan",
                progress: 1,
                total: 10
            }
        ]
      }
  }
}
</script>

<style>
    .container {
    display: grid;
    grid-template-columns: 5fr 2fr;
    grid-column-gap: 25px;
    margin-top: 25px;
    }

    .checkoffs {
        background: #FFFFFF;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);   
        grid-column: 1 / 2;
        margin-left: 25px;
    }

    .roster {
        text-align: left;
        grid-column: 2 / 3;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);
        background: #FFFFFF;
        padding: 30px;
        margin-right: 25px;
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
        margin-bottom: 10px;
    }

    hr {
    border-color: #1F6891;
    background-color: #1F6891;
    }

    @media (max-width: 768px) {
        .container {
            display: grid;
            grid-column-gap: 0px;
            grid-template-columns: 1fr;
            grid-template-rows: auto auto;
            grid-row-gap: 25px;
        }

        .checkoffs {
            grid-column: 1 / 2;
            grid-row: 1 / 2;
            margin-left: 0px;
        }

        .roster {
            grid-column: 1 / 2;
            grid-row: 2 / auto;
            margin-right: 0px;
        }

        #roster-contents {
            line-height: 30px;
        }

    } 
</style>
