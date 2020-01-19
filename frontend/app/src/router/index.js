import Vue from 'vue'
import Router from 'vue-router'
import Articles from '@/components/Articles'
import Article from '@/components/Article'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/articles',
      name: 'Articles',
      component: Articles
    },
    {
      path: '/article/:id',
      name: 'Article',
      component: Article
    },
    {
      path: '/admin',
      name: 'Article',
      component: Article
    }

  ]
})
