<template>
  <main class="container profile">
    <Navbar />
    <Profile />
    <Footer />
  </main>
</template>
<script>
import Profile from "@/components/Profile/Profile.vue";
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

export default {
  components: {
    Profile,
    Navbar,
    Footer,
  },
  data() {
    return {
    
      title: "Profile | Style Avenue Studio",
    };
  },
  mounted() {
    document.title = this.title.toUpperCase();
    
  },
};
</script>