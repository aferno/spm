<template>
  <div class="wrapper">
    <div class="head-bg"></div>
    <div class="container">
      <list-of-articles></list-of-articles>
      <p>Lorem ipsum dolor sit amet.</p>
      <Wysiwyg></Wysiwyg>
    </div>
  </div>
</template>

<script>

import router from '@/router'
import Header from '@/components/Header'
import Wysiwyg from '@/components/Wysiwyg'
import ListOfArticles from '@/components/ListOfArticles'


export default {
  name: 'Article',
  components: {
    Wysiwyg,
    Header,
    ListOfArticles
  },
  data: () => ({
    errors: []
  }),
  methods: {
    navigateBack () {
      router.go(-1)
    }
  }
}

</script>

<style scoped>
  .wrapper {
    position: absolute;
    top: 0;
    width: 100%;
    height: 100%;
  }
</style>
