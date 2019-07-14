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
                <ul id="member-info">
                    <li v-for="project in this.projects" :key='project.id'>{{project.title}}: {{project.subtitle}}</li>
                </ul>
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
        projects: Object
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

.popup-project-list {
    
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
    grid-template-columns: 5% 90% 5%;
    grid-column-gap: 20px;
}

#popup-member-progress-percent {
    grid-column: 1/2;
    margin-top: 7px;
    color: #1F6891;
    font-size: 18px;
}
</style>