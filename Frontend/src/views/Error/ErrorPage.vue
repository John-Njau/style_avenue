<template>
  <section class="container-fluid">
    <div class="error-page container">
      <h1>404</h1>
      <h3>Page not found</h3>
      <p>
        The page you are looking for might have been removed had its name
        changed or is temporarily unavailable.
      </p>
      <router-link to="/" class="btn btn-home">Home</router-link>
    </div>
  </section>
</template>
  
  <script>
export default {
  name: "Error",
  data() {
    return {
      title: "Page Not Found",
    };
  },
  mounted() {
    document.title = this.title;
  },
};
</script>
  
  <style>
.error-page,
.container-fluid {
  background-color: rgb(238, 233, 227);
  height: 100vh;
  margin: auto auto;
}
.btn-home{
  background-color: rgb(131, 87, 35) !important;
  color: #ffffff!important;
  border: 1px solid black;
  border-radius: 5px;
  padding: 10px 20px;
  text-decoration: none;
}
</style>