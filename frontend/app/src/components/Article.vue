<template>
  <div>
    <Header :theme="post.title" :bg="require('@/assets/post-bg.jpg')"></Header>
    <div class="article">
      <h1>Статья #{{ post.id }}</h1>
      <article>
        <div class="container">
          <div class="row">
            <div class="col-lg-12 col-md-12 mx-auto main-article">
              <p v-html="post.article"></p>
              <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati provident dolores laborum
                 laudantium odit nihil numquam tenetur ad, ullam debitis consequuntur mollitia hic similique
                  neque rem quis delectus soluta iste veritatis aut, dolor velit? Minima quia aperiam quidem 
                  vel quisquam, nesciunt illo numquam neque illum fuga itaque porro dolore, recusandae molestiae
                   animi alias temporibus rerum possimus sint aliquam cum, ut inventore et facilis. Dignissimos
                    modi vitae illo dolorum iure ex a explicabo debitis harum voluptatibus, nesciunt laborum, 
                    dicta quos quo impedit sint asperiores quia facilis deserunt. Doloremque, dolorem voluptatum 
                    ea id culpa maxime earum. Itaque cupiditate quas praesentium optio a!</p>
            </div>
          </div>
        </div>
      </article>
      <a class="article__back-link" style="" v-on:click="navigateBack()">Назад</a>
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
    width: 100%;
    left: 0 !important;
    padding: 0 !important;
    border-radius: 0 !important
  }
}
.article__back-link {
  cursor: pointer; 
  border-radius: 10px;
  background-color: #42b983;
  position: fixed;
  font-size: 25px;
  padding: 15px 30px;
  left: 20px;
  bottom: 10%;
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
 