<template>
    <header class="masthead" :style="{'background-image': 'url(' + bg + ')'}">
        <div class="overlay"></div>
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-md-10 mx-auto">
                    <div class="site-heading">
                        <h1>{{ theme }}</h1>
                        <span class="subheading">Блог о самом интересном</span>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <!-- <img src="./assets/home-bg.jpg"> -->
     <!-- <router-link :to="{ name: 'HelloWorld' }">Hello Page</router-link>
    <router-view/> -->
</template>

<script>
export default {
  name: 'Header',
  props: ['theme', 'bg']
}
</script>
<style scoped>
.masthead {
  /* background-image: url(../assets/home-bg.jpg); */
  z-index: 10;
}
</style>
