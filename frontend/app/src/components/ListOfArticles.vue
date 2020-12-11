<template>
  <div class="article-list">
    <div class="article-list__title">
      Список записей
    </div>
    <div class="list-items">
      <div class="list-items__item"
           v-for="(item, index) in items"
           v-bind:key="item.id"
           v-bind:item="item"
      >
        <div class="list-items__title">{{item.title}}</div>
        <div class="list-items__date-create">{{item.creationDate}}</div>
        <div class="list-items__controls">
          <div class="list-items__edit" @click="edit(item)"><img src="@/assets/icons/edit.png" alt=""></div>
          <div class="list-items__delete" @click="del(index, items)"><img src="@/assets/icons/trash.png" alt=""></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'ListOfArticles',
  data: function() {
    return {
        items: [
          {
            id: 1,
            title: 'Event 1',
            creationDate: '2015-09-10'
          },
          {
            id: 2,
            title: 'Event 2',
            creationDate: '2015-10-02'
          }
        ]
      };
},
  methods: {
    edit: (item) => {
      console.log(item)
    },
    del: (idx, items) => {
      items.splice(idx, 1)
    }
  }
}
</script>

<style scoped>
</style>
