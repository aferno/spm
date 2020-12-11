<template>
  <div class="wrapper">
    <div class="head-bg"></div>
    <div class="container">

      <list-of-articles></list-of-articles>
      <p>Lorem ipsum dolor sit amet.</p>
      <quillEditor @change="onEditorChange($event)"></quillEditor>
    </div>
  </div>
</template>

<script>

import router from '@/router'
import Header from '@/components/Header'
// import Wysiwyg from '@/components/Wysiwyg'
import ListOfArticles from '@/components/ListOfArticles'

import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

import { quillEditor } from 'vue-quill-editor'

export default {
  name: 'Article',
  components: {
    Header,
    ListOfArticles,
    quillEditor
  },
  data: () => ({
    errors: []
  }),
  methods: {
    navigateBack () {
      router.go(-1)
    },
    onEditorChange({ quill, html, text }) {
      console.log(JSON.stringify({title: "Piska", content: html}))

      this.content = html.json;
    }
  }
}

</script>

<style>
  .head-bg {

  }
  .wrapper {
    position: absolute;
    top: 0;
    width: 100%;
    height: 100%;
  }
</style>
