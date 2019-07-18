<template>
    <div class="member-popup-content">
        <div class="member-namecard">
            <p id='member-popup-title'>{{this.member.name}}</p>
            <p v-for="project in this.member.projects" :key='project.id'>{{project}}</p>
            <p id='member-popup-subtitle'>About</p>
            <ul id="member-info">
                <li>Email: {{this.member.email}}</li>
                <li>Year: {{this.member.year}}</li>
                <li v-if="this.member.deposit">Deposit: Paid</li>
                <li v-else>Deposit: Not Paid</li>
                <li v-if="this.member.box">Box: Collected</li>
                <li v-else>Box: Not Collected</li>
                <li v-if="this.member.labSafety">Lab Safety: Completed</li>
                <li v-else>Lab Safety: Not Completed</li>
                <li v-if="this.member.shopSafety">Shop Safety: Completed</li>
                <li v-else>Shop Safety: Not Completed</li>
            </ul>
        </div>
        <div class="member-checkpoints">
            <div id="popup-member-progress-block">
                <p id="popup-member-progress-percent">{{ calculatePercentage().toFixed(0) }}%</p>
                <div class="popup-member-total-progress">
                    <div class="popup-member-current-progress"
                    :style="{ width: this.calculatePercentage() + '%'} "></div>
                </div> 
                <span class="close-popup" @click="$emit('popup')">&times;</span>
            </div>
            <div class="popup-project-list">
                <p id="member-popup-subtitle">Projects</p>
                <div id="member-popup-checkpoint-container" v-for="project in this.projects" :key='project.id'>
                    <div id="member-popup-checkpoint-incomplete" v-if="member.checkpoints[project.id-1]">
                    </div>
                    <div id="member-popup-checkpoint-complete" v-else>
                    </div>
                    <p id='member-popup-project-name'>{{project.title}}: {{project.subtitle}}</p>
                </div>
            </div>
        </div>  
    </div>
</template>

<script>
export default {
    name: "MemberPopup",
    props: {
        member: Object,
        calculatePercentage: Function,
        projects: Array
    }
}
</script>

<style>
.member-popup-content {
    display: grid;
    grid-template-columns: 2fr 3fr;
    background-color: #fefefe;
    margin: 15% auto;
    padding: 50px;
    border: 1px solid #888;
    width: 60%;
    font-weight: bold;
    line-height: 30px;
    border-radius: 10px;
    font-size: 15px;
}

.member-namecard {
    grid-column: 1/2;
    border-right: solid #1F6891 1px;
}
.close-popup {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    grid-column: 3/4;
    margin-right: 15px;
}

.close-popup:hover, .close-popup:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}

.popup-member-total-progress {
    background-color: #EFEFEF;
    margin-top: 15px;
    margin-bottom: 15px;
    border-radius: 5px;
    height: 20%;
    width: 90%;
    grid-column: 2/3;
    margin-left: 10px;
}

.popup-member-current-progress {
    background-color: #1F6891;
    height: 100%;
    border-radius: 5px;
}

.member-checkpoints {
    margin-left: 25px;
}
#member-info {
    list-style: none;
    padding-left: 0px;
}
#member-popup-title {
    font-size: 25px;
    color: #1F6891;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
}
#member-popup-subtitle {
    font-size: 20px;
    color: #1F6891;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
}

#popup-member-progress-block {
    grid-column-start: 2;
    grid-column-end: 3;
    height: 60px;
    display: grid;
    grid-template-columns: 5% 85% 10%;
    grid-column-gap: 20px;
}

#popup-member-progress-percent {
    grid-column: 1/2;
    margin-top: 7px;
    color: #1F6891;
    font-size: 18px;
}

#member-popup-checkpoint-container {
    display:grid;
    grid-template-columns: 90% 10%;
    grid-template-rows: 1fr;
    width: 100%;
    height: 35px;
}

#member-popup-checkpoint-incomplete {
    grid-column: 2/3;
    grid-row: 1/2;
    border: solid 2px #1F6891;
    margin: 3px 7px 9px 7px;
    border-radius: 20px;
}

#member-popup-checkpoint-complete {
    grid-column: 2/3;
    grid-row: 1/2;
    background-color: #1F6891;
    margin: 3px 7px 9px 7px;
    border-radius: 20px;
}

#member-popup-project-name {
    grid-column: 1/2;
    grid-row:1/2;
}

@media(max-width: 1220px)
{
    .member-popup-content {
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: 2fr 3fr;
    }

    .member-namecard {
        grid-template-columns: 1/2;
        grid-template-rows: 1/2;
        border-bottom: solid #1F6891 1px;
        border-right: none;
    }

    #member-popup-checkpoint-container {
        grid-template-columns: 70% 30%;
        height: 80px;
    }

    #member-popup-checkpoint-incomplete {
        margin: 15px 15px;
    }

    #member-popup-checkpoint-complete {
        margin: 15px 15px;
    }
} 

</style>