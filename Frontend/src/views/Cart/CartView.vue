<template>
  <main class="cartview-main">
    <Navbar />
    <Cart class="container m-3" />
    <Footer />
  </main>
</template>

<script>
import Cart from "@/components/Cart/Cart.vue";
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "CartView",
  components: {
    Cart,
    Navbar,
    Footer,
  },
  data() {
    return {
      title: "Cart | Style Avenue Studio",
    };
  },
  mounted() {
    document.title = this.title;
  },
};
</script>

<style>
.cartview-main {
  height: 100%;
}
</style>