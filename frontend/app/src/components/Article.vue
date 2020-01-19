<template>
  <div>
    <Header :theme="post.title" :bg="require('@/assets/post-bg.jpg')"></Header>
    <a style="cursor: pointer; text-decoration: underline" v-on:click="navigateBack()">Назад</a>
    <h1>Статья #{{ post.id }}</h1>
    <article>
      <div class="container">
        <div class="row">
          <div class="col-lg-12 col-md-12 mx-auto main-article">
            <p v-html="post.article"></p>
          </div>
        </div>
      </div>
    </article>
  </div>
</template>
<script>

import axios from 'axios'
import router from '../router'
import Header from '@/components/Header'

export default {
  name: 'Article',
  components: {
    Header
  },

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
