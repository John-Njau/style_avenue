<template>
  <div class="">
    <Navbar class="" />
    <div class="landing">
      <LandingPage />
    </div>
    <About />
    <Footer class="" />
  </div>
</template>

<script>
// @ is an alias to /src
import LandingPage from "@/components/LandingPage/LandingPage.vue";
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import About from "@/components/LandingPage/About.vue";

export default {
  name: "HomeView",
  components: {
    LandingPage,
    Navbar,
    Footer,
    About,
  },
  data() {
    return {
      title: "Home | Style Avenue Studio",
    };
  },
  mounted() {
    document.title = this.title.toUpperCase();
  },
};
</script>
<style scoped>
.landing {
  /* margin: 30px; */
  /* font-family: "Akshar", sans-serif; */
  /* font-family: "Montserrat", sans-serif; */
  /* font-family: "Nunito Sans", sans-serif; */
  /* font-family: "Poppins", sans-serif; */
  /* font-family: "Raleway", sans-serif; */
  font-family: 'Noto Sans Buhid', sans-serif;
font-family: 'Roboto Condensed', sans-serif;
}
</style>
