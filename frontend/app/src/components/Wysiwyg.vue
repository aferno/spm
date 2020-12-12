<template>
  <div class="modal-wysiwyg">
    <input class="title-of-article" v-model="title">
    <quillEditor
      v-model="article">
    </quillEditor>
    <button class="send-article" @click="send()">Отправить</button>
  </div>
</template>

<script>
import { quillEditor } from 'vue-quill-editor'

import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'


export default {
name: "Wysiwyg",
  components: {
    quillEditor
  },
  data: function() {
    return {
      title: 'sdsds',
      article: ''
    };
  },
  methods: {
    send() {
      console.log(JSON.stringify({title: this.title, content: this.article}))
    }
  }
}
</script>

<style scoped>

</style>
