<template>
  <main class="">
    <Navbar />
    <Booking />
    <Footer />
  </main>
</template>

<script>
import Booking from "@/components/Booking/booking.vue";
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

export default {
  components: {
    Booking,
    Navbar,
    Footer,
  },
  data() {
    return {
      title: "Book | Style Avenue Studio",
    };
  },

  mounted() {
    document.title = this.title.toUpperCase();
  },
};
</script>

<style>
</style>
