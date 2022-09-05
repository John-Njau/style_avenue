<template>
  <main class="container">
    <Navbar />
    <router-link to="/">Home</router-link>
    <Category />
    <Footer />
  </main>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import Category from "@/components/category/category.vue";

export default {
  name: "CategoryView",
  components: {
    Navbar,
    Footer,
    Category,
  },
};
</script>

<style>
</style>