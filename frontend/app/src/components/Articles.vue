<template>
  <div class="hello">
    <Header :theme="theme" :bg="require('@/assets/home-bg.jpg')"></Header>
    <h1>Статьи</h1>
    <!-- <input v-model="message" placeholder="Поиск по сайту">
    <p>Request to the server with {{ message }}</p> -->
    <h2 v-for="post in posts" :key="post" class="article-title">
      <router-link :to="{ name: 'Article', params: { id: post.id }}">{{ post.title }}</router-link>
    </h2>
    <div class="container">
          <div class="row">
            <div class="col-lg-12 mx-auto">
              <div v-for="post in posts" :key="post" class="article-preview-block">
                <div v-html="post.article" class="article-preview"></div>
              </div>
            </div>
          </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'
import Header from '@/components/Header'

export default {
  name: 'Articles',
  components: {
    Header
  },
  data: () => ({
    message: 'GGGGG!!!!',
    posts: [],
    errors: [],
    post: [],
    theme: 'Блог о всем'
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
.article-title {
  color: rgb(44, 62, 80) !important;
}
.article-preview {
  height: 150px;
  overflow: hidden;
  font-size: 20px;
}
</style>
