<template>
    <div class="project-progress">
        <div id="title-block">
            <p>{{ project.title }} - {{ project.subtitle }}</p>
        </div>
        <div id="progress-block">
            <p>{{ project.progress }}%</p>
        </div>
        <DropdownButton v-on:open='setOpen'></DropdownButton>
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
        }
    }
}


</script>

<style>
.project-progress {
    display: grid;
    grid-template-columns: 60% 30% 10%;
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

#title-block {
    margin-top: 10px;
    font-weight: bold;
    margin-left: 40px;
    grid-column-start: 1;
    grid-column-end: 2;
    grid-row-start: 1;
    grid-row-end: 2;
    position: relative;
}

#progress-block {
    margin-top: 10px;
    grid-column-start: 2;
    grid-column-end: 3;
    grid-row-start: 1;
    grid-row-end: 2;
    position: relative;
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

</style>

