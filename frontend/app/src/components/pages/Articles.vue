<template>
  <div class="hello">
    <Header :theme="theme" :bg="require('@/assets/home-bg.jpg')"></Header>
    <h1>{{posts.length}} Статей</h1>
    <!-- <input v-model="message" placeholder="Поиск по сайту">
    <p>Request to the server with {{ message }}</p> -->
    <div class="articles">
      <div class="articles__container container">
        <div class="articles__item" v-for="post in posts" :key="post">
            <router-link class="articles__title" :to="{ name: 'Article', params: { id: post.id }}">{{ post.title }}</router-link>
          <div class="articles__preview">
            <div class="articles__text" v-html="post.article"></div>
            <div class="articles__overlay"></div>
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
    theme: 'Блог обо всем'
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
