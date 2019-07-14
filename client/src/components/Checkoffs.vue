<template>
  <div class="checkoffs-container">
        <div class="checkoffs">
            <h1 class="checkoff-title" id="checkoff-title">Checkoffs</h1>
            <CheckoffTile v-for="project in projects" :project='project' :key="project.id"></CheckoffTile>
        </div>
        <div class="roster">
            <div >
                <h1 class="checkoff-title" id="roster-title">Roster</h1>
                <hr>
                <input type="text" placeholder="Search members">
                <RosterTile v-for="member in members" :member='member' :projects='projects' id="roster-contents" :key='member.id'></RosterTile>
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
                projects: ['Open Project Space'],
                progress:   5,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 2,
                name: "Robert Peralta",
                projects: ['Open Project Space'],
                progress: 8,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 3,
                name: "Michelle Lam",
                projects: ['Open Project Space'],
                progress: 6,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 4,
                name: "Jiwan Kang",
                projects: ['Open Project Space'],
                progress: 4,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 5,
                name: "Michelle Tan",
                projects: ['Open Project Space'],
                progress: 9,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 6,
                name: "Serene Kamal",
                projects: ['Open Project Space'],
                progress: 4,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 7,
                name: "Eugene Lo",
                projects: ['Open Project Space'],
                progress: 6,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 8,
                name: "John Doe",
                projects: ['Open Project Space'],
                progress: 10,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 9,
                name: "Josephine Bruin",
                projects: ['Open Project Space'],
                progress: 3,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 10,
                name: "Jeffrey Chan",
                projects: ['Open Project Space'],
                progress: 5,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 11,
                name: "Robert Downey, Jr.",
                projects: ['Open Project Space'],
                progress: 1,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 12,
                name: "Anonymous",
                projects: ['Open Project Space'],
                progress: 0,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 13,
                name: "Josephine Bruin",
                projects: ['Open Project Space'],
                progress: 9,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 14,
                name: "Maggie Huang",
                projects: ['Open Project Space'],
                progress: 4,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 15,
                name: "Robert Peralta",
                projects: ['Open Project Space'],
                progress: 5,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 16,
                name: "Robert Zalog",
                projects: ['Open Project Space'],
                progress: 8,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 17,
                name: "Kathy Daniels",
                projects: ['Open Project Space'],
                progress: 10,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 18,
                name: "Roselyn Lee",
                projects: ['Open Project Space'],
                progress: 8,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 19,
                name: "Maggie Huang",
                projects: ['Open Project Space'],
                progress: 2,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 20,
                name: "Roselyn Lee",
                projects: ['Open Project Space'],
                progress: 3,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            },
            {
                id: 21,
                name: "Jeffrey Chan",
                projects: ['Open Project Space'],
                progress: 1,
                total: 10,
                email: "danielskathy@gmail.com",
                year: "Junior",
                deposit: true,
                box: true,
                labSafety: true,
                shopSafety: true,
                checkpoints: [true, true, true, false, false]
            }
          ]
      }
  }
}
</script>

<style>
    .checkoffs-container {
        display: grid;
        grid-template-columns: 5fr 2fr;
        grid-column-gap: 25px;
        margin: 25px 125px;
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

    .checkoff-title {
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
        .checkoffs-container {
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
