<template>
    <div class="project-progress">
        <div id="title-block">
            <p>{{ project.title }} - {{ project.subtitle }}</p>
        </div>
        <div id="progress-block">
            <p>{{ project.progress }}%</p>
        </div>
        <div class="dropdown">

        </div>
    </div>       
</template>

<script>
export default {
    name: 'CheckoffTile',
    props: {
        project: Object
    }
}
</script>

<style>
.project-progress {
    margin: 0px 40px;
    text-align: left;
    border-top: 1px solid #1F6891;
}

#checkoff-title {  
    font-size: 24px;
    line-height: 32px;
    text-align: center;
}

#title-block {
    font-weight: bold;
    margin-left: 40px;
    width: 60%;
    display: inline-block;
    height: 10px;
}

#progress-block {
    width: 30%;
    display: inline-block;
    height: 10px;
}

.dropdown {
    background-color: #EFEFEF;
    border-top: 5px solid 
}
</style>

