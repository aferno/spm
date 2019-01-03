import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Articles from '@/components/Articles'
import Article from '@/components/Article'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/articles',
      name: 'Articles',
      component: Articles
    },
    {
      path: '/article/:id',
      name: 'Article',
      component: Article
    }
  ]
})
