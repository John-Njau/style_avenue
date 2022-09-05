<template>
  <section class="container-fluid">
    <div class="error-page container">
      <h1>404</h1>
      <h3>Page not found</h3>
      <p>
        The page you are looking for might have been removed had its name
        changed or is temporarily unavailable.
      </p>
      <router-link to="/" class="btn btn-secondary">Back to home</router-link>
    </div>
  </section>
</template>
  
  <script>
export default {};
</script>
  
  <style>
.error-page,
.container-fluid {
  background-color: rgb(238, 233, 227);
  height: 100vh;
  margin: auto auto;
}
</style>