<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
      <div class="container">
        <a class="navbar-brand" href="/">Блог</a>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <router-link :to="{ name: 'Articles' }" class="nav-link">Статьи</router-link>
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'About' }" class="nav-link">О блоге</router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="post.html">Самое интересное</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="contact.html">Контакты</a>
                </li>
              </ul>
            </div>
          </div>
    </nav>
    <!-- <img src="./assets/home-bg.jpg"> -->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style src="./assets/css/main.css"></style>
<style src="./assets/css/clean-blog.css"></style>
<style scoped>
.masthead {
  background-image: url(assets/home-bg.jpg);
}
</style>
