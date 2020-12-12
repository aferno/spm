<template>
  <div>
      <button class="add-new-button" @click="$emit('create-articles')">Добавить новую запись</button>
    <div class="article-list">
      <div class="article-list__title">
        Список записей
      </div>
      <div class="list-items">
        <div class="list-items__item"
             v-model="items"
             v-for="(item, index) in items"
             v-bind:key="item.id"
             v-bind:item="item">
          <router-link class="list-items__title" :to="{ name: 'Article', params: { id: item.id }}">{{ item.title }}</router-link>
<!--          <div  >{{item.title}}</div>-->
          <div class="list-items__controls">
            <div class="list-items__edit" @click="$emit('edit-articles', item)"><img src="@/assets/icons/edit.png" alt=""></div>
            <div class="list-items__delete" @click="del(item.id, items, index)"><img src="@/assets/icons/trash.png" alt=""></div>
          </div>
        </div>
      </div>
    </div>
  </div>


</template>

<script>

import axios from "axios";

export default {
  name: 'ListOfArticles',
  props: ['items'],
  data: function() {
    return {
        // items: []
      };
  },

  methods: {
    edit: (item) => {
      console.log(item)
    },
    del: (id, items, idx) => {
      axios.delete(`api/article/${id}`)
        .then((response) => {
            console.log(response);
          })
          .catch((error) => {
          console.log(error);
          });
      items.splice(idx, 1);
    }
  }
}
</script>

<style scoped>
</style>
