<template>
  <div>
    <Header :theme="post.title" :bg="require('@/assets/post-bg.jpg')"></Header>
    <div>
      <h1>{{ post.title }}</h1>
      <article class="article">
        <a class="article__back-link" style="" v-on:click="navigateBack()">Назад</a>
        <div class="container">
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

.article {
  display: flex;
  flex-direction: column;
  position: relative;
}
@media (max-width: 1400px){
  .container {
    max-width: 800px;
  }
}
@media (max-width: 1100px){
  .container {
    max-width: 600px;
  }
}
@media (max-width: 998px){
  .container {
    max-width: 800px;
  }
  .article__back-link {
    bottom: 0 !important;
    position: fixed !important;
    overflow: hidden;
    z-index: 999;
    width: 100%;
    left: 0 !important;
    padding: 0 !important;
    border-radius: 0 !important
  }
  .main-article {
    padding-bottom: 20px;
  }
}
.article__back-link {
  cursor: pointer;
  border-radius: 10px;
  background-color: #42b983;
  position: absolute;
  font-size: 25px;
  padding: 15px 30px;
  left: 20px;
  bottom: 40%;
  text-decoration: underline;
}
.article__back-link:hover {
  background-color: #50dd9e;
}
.article__back-link:active {
  background-color: #38996d;
}

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
