<template>
  <div id="app">
    <!-- <nav> -->
      <!-- <router-link to="/">Home</router-link> | 
      <router-link to="/about">About</router-link> -->
    <!-- </nav> -->
    <router-view  :key="$route.path"  />
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Akshar:wght@300&family=Koulen&family=Macondo&family=Montserrat:wght@200;500&family=Nunito+Sans:wght@200&family=Pacifico&family=Poppins:ital,wght@0,100;0,200;0,300;1,300&family=Raleway:ital,wght@0,300;0,500;1,200&display=swap");

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  scroll-behavior: smooth;
  color: #0e151d;
}
</style>
