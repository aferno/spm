<template>
  <div>
    <Header :theme="post.title" :bg="require('@/assets/post-bg.jpg')"></Header>
    <div>
      <h1>{{ post.title }}</h1>
      <article class="article">
        <a class="article__back-link" style="" v-on:click="navigateBack()">Назад</a>
        <div class="container-article">
          <div class="row">
            <div class="col-lg-12 col-md-12 mx-auto main-article">
              <p v-html="post.article"></p>
            </div>
          </div>
        </div>
      </article>
    </div>

  </div>
</template>
<script>

import axios from 'axios'
import router from '../../router'
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
</style>
