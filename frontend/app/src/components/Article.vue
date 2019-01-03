<template>
  <div>
    <router-link :to="{ name: 'Articles'}">Статьи</router-link>
    <a style="cursor: pointer; text-decoration: underline" v-on:click="navigateBack()">Назад</a>
    <h1>Статья</h1>
    <h2 v-html="post.article"></h2>
  </div>
</template>
<script>

import axios from 'axios'
import router from '../router'

export default {
  name: 'Article',
  data: () => ({
    errors: [],
    post: []
  }),

  created () {
    this.id = this.$route.params.id

    axios.get('/api/article/' + this.id)
      .then(response => {
        this.post = response.data
      })
      .catch(e => {
        this.errors.push(e)
      })
  },

  methods: {
    navigateBack () {
      router.go(-1)
    }
  }
}
</script>

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
