import Vue from 'vue'
import Router from 'vue-router'
import Articles from '@/components/pages/Articles'
import Article from '@/components/pages/Article'
import Admin from '@/components/pages/Admin'
import About from '@/components/pages/About'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Articles',
      component: Articles
    },
    {
      path: '/Articles',
      name: 'home',
      component: Articles
    },
    {
      path: '/article/:id',
      name: 'Article',
      component: Article
    },
    {
      path: '/admin',
      name: 'Admin',
      component: Admin
    },
    {
      path: '/about',
      name: 'About',
      component: About
    }
  ]
})
