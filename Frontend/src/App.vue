<template>
  <div id="app">
    <!-- <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav> -->
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
.options ul {
  list-style-type: none;
  display: flex;
  /* flex-direction: column; */
  background-color: #080705;
  justify-content: center;
  padding: 0;
  margin: 0;
}
.options ul li {
  padding: 5px;
  margin: 5px 10px;
  border: 1px solid #080705;
  border-radius: 5px;
  text-align: center;
  background-color: #e2962d;
}

.options ul li:hover {
  background-color: #080705;
  color: #fafafa;
  box-shadow: 1px 1px 1px 1px rgb(252, 251, 248);
}
</style>
