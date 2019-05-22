<template>
    <div class="member-progress">
        <div id="member-name">    
            <p>{{ member.name }}</p>
        </div>
        <div id="member-progress">
            <p>{{ member.progress }}%</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'RosterTile',
    props: {
        member: Object
    }
}
</script>

<style>
.member-progress {
    height: 30px;
}

#member-name {
    font-weight: bold;
    width: 60%;
    display: inline-block;
}
</style>