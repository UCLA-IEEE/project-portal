<template>
    <div class="project-progress">
        <div id="checkoff-title-block">
            <p>{{ project.title }} - {{ project.subtitle }}</p>
        </div>
        <div id="checkoff-progress-block">
            <p id="checkoff-percent">{{ calculatePercentage().toFixed(0) }}%</p>
            <div id="checkoff-total-progress">
                <div id="checkoff-current-progress"
                :style="{ width: calculatePercentage() + '%'} "></div>
            </div> 
        </div>
        <DropdownButton v-on:open='setOpen' id="dropdown-arrow"></DropdownButton>
        <transition name='expand'>
            <div v-if="open" class="dropdown-backdrop">
            </div>
        </transition>
    </div>       
</template>

<script>
import DropdownButton from './DropdownButton'
export default {
    name: 'CheckoffTile',
    data() {
        return {
            open: false
        } 
    },
    components: {
        DropdownButton
    },
    props: {
        project: Object
    },
    methods: {
        setOpen() {
            this.open = !this.open;
        },
        calculatePercentage() {
            return (this.project.progress / this.project.total) * 100;
        }
        ,
        addQuestion() {
            this.project.total += 1;
        },
        completeQuestion() {
            this.project.progress += 1;
        }
    }
}
</script>

<style>
.project-progress {
    display: grid;
    grid-template-columns: 60% 35% auto;
    grid-template-rows: auto auto;
    position: relative;
    margin: auto 40px;
    text-align: left;
    border-top: 1px solid #1F6891;
}
.show {
    display: block;
}
.dropdown-backdrop {
    background-color: #EFEFEF;
    border-top: 5px solid;
    min-height: 200px;
    position: relative;
    width: 100%;
    grid-column-start: 1;
    grid-column-end: 4;
    grid-row-start: 2;
    grid-row-end: 3;
}
#checkoff-title {  
    font-size: 24px;
    line-height: 32px;
    text-align: center;
}
#checkoff-title-block {
    margin-top: 10px;
    font-weight: bold;
    margin-left: 40px;
    grid-column-start: 1;
    grid-column-end: 2;
    grid-row-start: 1;
    grid-row-end: 2;
    position: relative;
}
#checkoff-progress-block {
    margin-top: 10px;
    margin-right: 5px;
    grid-column-start: 2;
    grid-column-end: 3;
    grid-row-start: 1;
    grid-row-end: 2;
    position: relative;
    display: grid;
    grid-template-columns: 15% 85%;
}
#checkoff-total-progress {
    background-color: #EFEFEF;
    grid-column-start: 2;
    grid-column-end: 3;
    margin-bottom: 15px;
    margin-top: 5px;
    border-radius: 5px;
    height: 10px;
}
#checkoff-current-progress {
    background-color: #1F6891;
    height: 100%;
    border-radius: 5px;
}
#checkoff-percent {
    grid-column-start: 1;
    grid-column-end: 2;
}
button:focus {
    outline: 0;
}
button:active{
    background-color: #eee;
    color: #eee;
}
.expand-enter-active, .expand-leave-active {
    transition: all .3s ease-in-out;
    height: 30px;
    padding: 10px;
    background-color: #eee;
    overflow: hidden;
}
.expand-enter, .expand-leave {
    height: 0;
    padding: 0 10px;
    opacity: 0;
}

@media (max-width: 1110px)
{
    .project-progress {
        grid-template-columns: 95% 5%;
        grid-template-rows: 1fr 1fr auto;
    }
    #checkoff-itle-block {
        margin-left: 25px;
        grid-column: 1/2;
        grid-row: 1/2;
    }

    #dropdown-arrow {
        grid-column: 2/3;
        grid-row: 1/2
    }

    #checkoff-progress-block {
        margin-left: 25px;
        grid-column: 1/3;
        grid-row: 2/3;
    }
    .dropdown-backdrop {
        grid-row: 3/4;
    }

    
}
</style>