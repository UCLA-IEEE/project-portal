<template>
    <div class="roster-container">
        <div class="member-progress" @click="setPopup" ref="popup">
            <div id="member-name">    
                <p>{{ member.name }}</p>
            </div>
            <div id="member-progress-block">
                <div class="member-total-progress">
                    <div class="member-current-progress"
                    :style="{ width: calculatePercentage() + '%'} "></div>
                </div> 
            </div>
        </div>
        <div v-if="popup" class="member-popup">
            <MemberPopup v-on:popup="setPopup" :member='member' :projects='projects' :calculatePercentage='calculatePercentage'></MemberPopup>
        </div>
    </div>
   
</template>

<script>
import MemberPopup from './MemberPopup'
export default {
    name: 'RosterTile',
    data() {
        return {
            popup: false
        }
    },
    props: {
        member: Object,
        projects: Object
    },
    components: {
        MemberPopup
    },
    methods: {
        calculatePercentage() {
            return (this.member.progress / this.member.total) * 100;
        },
        setPopup() {
            this.popup = !this.popup;
        }
    }
}
</script>

<style>
.member-progress {
    height: 30px;
    display: grid;
    grid-template-columns: 2fr 1fr;
    cursor: pointer;
}

.member-popup {
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0, 0, 0);
    background-color: rgba(0, 0, 0, 0.4);
}


#member-name {
    font-weight: bold;
    grid-column-start: 1;
    grid-column-end: 2;
}

#member-progress-block {
    grid-column-start: 2;
    grid-column-end: 3;
}

#member-link, #member-link:visited, #member-link:hover, #member-link:active{
    color: black;
    text-decoration: none;
}


.member-total-progress {
    background-color: #EFEFEF;
    margin-top: 15px;
    margin-bottom: 15px;
    border-radius: 5px;
    height: 20%;
}

.member-current-progress {
    background-color: #1F6891;
    height: 100%;
    border-radius: 5px;
}

@media (max-width: 1000px) {
    .member-progress {
        height: auto;
        grid-template-columns: 1fr;
        grid-template-rows: 1fr 1fr;
    }
    #member-name {
        grid-row: 1/2;
        grid-column: 1/2;
    }
    #member-progress-block {
        grid-row: 2/auto;
        grid-column: 1/2;
        width: 50%;
    }
    .member-total-progress {
        margin-top: 0px;
        margin-bottom: 0px; 
    }
}
</style>