<template>
    <div class="dropdown">
        <button href='#' ref="button" @click="$emit('open') " class="glyphicon glyphicon-chevron-down" id="arrow"
            type="button">
        </button>
    </div>
    
</template>

<script>
export default {
    name: "DropdownButton",
    props: {
        btnClass: { type: String, default: 'btn-default' },
        text: String
    }
}
</script>

<style>
#arrow {
    margin-top: 10px;
    grid-column-start: 3;
    grid-column-end: 4;
    background: transparent;
    border: none !important;
}
</style>