<template>
  <div id="app">
    <!-- <nav> -->
    <!-- <router-link to="/">Home</router-link> | 
      <router-link to="/about">About</router-link> -->
    <!-- </nav> -->
    <div
        class="is-loading-bar has-text-centered"
        v-bind:class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-dual-ring"></div>
    </div>

    <router-view :key="$route.fullPath"/>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
  beforeCreate() {
    this.$store.commit("initializeStore");
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Combo&family=Noto+Sans+Buhid&family=Oswald:wght@500&family=Roboto+Condensed&display=swap");
// @import '../node_modules/bulma';

#app {
  //font-family: Avenir, Helvetica, Arial, sans-serif;
  //font-family: "Noto Sans Buhid", sans-serif;
  font-family: "Roboto Condensed", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  scroll-behavior: smooth;
  color: #0e151d;
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
