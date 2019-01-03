<template>
  <div class="hello">
    <h1>Самое интересное</h1>
    <h2 v-for="post in posts" :key="post">
      <router-link :to="{ name: 'Article', params: { id: post.id }}">{{ post.title }}</router-link>
    </h2>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'Articles',
  data: () => ({
    posts: [],
    errors: [],
    post: []
  }),

  created () {
    axios.get('api/articles')
      .then(response => {
        this.posts = response.data
      })
      .catch(e => {
        this.errors.push(e)
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
