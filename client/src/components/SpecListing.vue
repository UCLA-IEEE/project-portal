<template>
  <div class="listing">
    <router-link v-for="post in posts" :key="post.id" :to="post.link">
      <ListingTile :post="post"></ListingTile>
    </router-link>
  </div>
</template>

<script>
import ListingTile from './ListingTile'
export default {
  name: "SpecListing",
  props: {
    project: String
  },
  components: {
    ListingTile
  },
  data() {
    return {
      posts: [
        {
          id: 1,
          title: "Mouse Assignment",
          body: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset",
          link: "/Micromouse"
        },
        {
          id: 2,
          title: "Eagle Tutorial",
          body: "I'm writing some random filler text because I want this tile to have some text but not as much as the last one. Maybe a little bit more than that though so it can wrap.",
          link: "/Micromouse"
        },
        {
          id: 3,
          title: "Vue Info",
          body: "Features Templates Vue uses an HTML-based template syntax that allows binding the rendered DOM to the underlying Vue instance’s data. All Vue templates are valid HTML that can be parsed by spec-compliant browsers and HTML parsers. Under the hood, Vue compiles the templates into virtual DOM render functions. Combined with the reactivity system, Vue is able to calculate the minimal number of components to re-render and apply the minimal amount of DOM manipulations when the app state changes. Reactivity Vue features a reactivity system that uses plain JavaScript objects and optimized re-rendering. Each component keeps track of its reactive dependencies during its render, so the system knows precisely when to re-render, and which components to re-render.[9] Components Vue components extend basic HTML elements to encapsulate reusable code. At a high level, components are custom elements to which the Vue’s compiler attaches behavior. In Vue, a component is essentially a Vue",
          link: "/Micromouse"
        },
        {
          id: 4,
          title: "Filler",
          body: "This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works.",
          link: "/Micromouse"
        },
        {
          id: 5,
          title: "Filler",
          body: "This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works.",
          link: "/Micromouse"
        },
        {
          id: 6,
          title: "Filler",
          body: "This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works.",
          link: "/Micromouse"
        },
        {
          id: 7,
          title: "Filler",
          body: "This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works. This is just a filler tile to make sure scrolling works.",
          link: "/Micromouse"
        },
      ]
    }
  }
}
</script>

<style scoped>
.listing {
  margin-left: 130px;
  margin-right: 40px;
}

.listing a:hover {
  text-decoration: none;
}

@media all and (max-width: 950px) {
  .listing {
    margin-left: 15px;
    margin-right: 15px;
  }
}
</style>
