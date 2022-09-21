<template>
  <main class="">
    <Navbar />
    <!-- <router-link to="/">Home</router-link> -->
    <Category class="container mt-5"/>
    <Footer />
  </main>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import Category from "@/components/Category/category.vue";

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