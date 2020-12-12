<template>
  <div class="wrapper">
    <div class="head-bg"></div>
    <div class="container">
      <list-of-articles
        v-on:edit-articles='editArticle'
        v-on:create-articles='createArticles'
        :items="items"
        >
      </list-of-articles>
    </div>
    <Wysiwyg v-on:close-wysiwyg="closeModal" v-show="visible" :item="item"></Wysiwyg>
  </div>
</template>

<script>

import router from '@/router'
import Header from '@/components/Header'
import Wysiwyg from '@/components/Wysiwyg'
import ListOfArticles from '@/components/ListOfArticles'
import axios from "axios";


export default {
  name: 'Article',
  components: {
    Wysiwyg,
    Header,
    ListOfArticles
  },
  data: () => ({
      errors: [],
      visible: false,
      items: [],
      item: {}
  }),
  created () {
    axios.get('api/articles')
      .then(response => {
        this.items = response.data
      })
      .catch(e => {
        this.errors.push(e)
      })
  },
  methods: {
    navigateBack () {
      router.go(-1)
    },
    createArticles: function () {
      this.visible = true;
    },
    editArticle: function (item){
      this.visible = true;
      this.item = item;
    },
    closeModal: function () {
      this.visible = false;
    }
  }
}

</script>

<style scoped>
  .wrapper {
    position: absolute;
    top: 0;
    width: 100%;
    height: auto;
  }
</style>
