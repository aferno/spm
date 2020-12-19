<template>
  <div class="wrapper-wysiwyg">
    <div class="modal-wysiwyg">
      <div class="modal-wysiwyg__row">
        <label class="modal-wysiwyg__label" for="article-title">Заголовок статьи</label>
        <span class="modal-wysiwyg__close" @click="$emit('close-wysiwyg')"></span>
      </div>
      <input class="modal-wysiwyg__title" id="article-title" v-model="item.title" placeholder="Article title">
      <label class="modal-wysiwyg__label">Статья</label>
      <quillEditor
        class="modal-wysiwyg__wysiwyg"
        v-model="item.article">
      </quillEditor>
      <button class="modal-wysiwyg__send-button" @click="send()">Отправить</button>
    </div>
  </div>
</template>

<script>
import { quillEditor } from 'vue-quill-editor'
import axios from 'axios'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

export default {
  name: 'Wysiwyg',
  components: {
    quillEditor
  },
  props: ['item'],
  data: function () {
    return {}
  },
  methods: {
    send () {
      if (!this.item.id) {
        axios.post('/api/articles', {
          title: this.item.title,
          article: this.item.article
        }).then((response) => {
          console.log(response)
        }, (error) => {
          console.log(error)
        })
      } else {
        axios.put(`/api/article/${this.item.id}`, {
          title: this.item.title,
          article: this.item.article
        })
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
      }
      this.$emit('close-wysiwyg')
    }
  }
}
</script>

<style scoped>

</style>
