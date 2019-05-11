<template>
  <div class="tile">
    <p class="title">{{post.title}}</p>
    <p class="body">{{post.body|truncate}}</p>
  </div>
</template>

<script>
export default {
  name: "ListingTile",
  props: {
    post: Object
  },
  filters: {
    truncate: function(str) {
      if (str.length > 500)
        str = str.substr(0, 497) + "..."
      return str
    }
  }
}
</script>

<style>
.tile {
  padding: 8px 25px;
  margin: 20px 0px;
  border-left: 12px solid #1f6891;
  box-shadow: 0px 5px 5px rgba(0, 0, 0, 0.2);
  background-color: white;
}
.title {
  text-align: left;
  margin: 0px 0px 7px 0px;

  text-align: left;
  font-size: 14px;
  font-weight: 500;
  text-transform: uppercase;
  color: #1F6891;
}
.body {
  margin: auto;

  text-align: left;
  font-size: 14px;
  font-weight: 500;
}
</style>
