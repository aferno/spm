<template>
  <div class="preview">
    <div class="preview__container" v-model="article"></div>
  </div>
</template>

<script>
export default {
  name: "ArticlePreview",
  props: ['article']
}
</script>

<style scoped>

</style>
