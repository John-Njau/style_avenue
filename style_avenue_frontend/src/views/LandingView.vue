<template>
  <div>
    <Navbar class="container-fluid" />
    <div class="landing container">
      <LandingPage />
    </div>
    <About />
    <Footer class="container-fluid" />
  </div>
</template>

<script>
// @ is an alias to /src
import LandingPage from "@/components/LandingPage.vue";
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import About from "@/components/About.vue";

export default {
  name: "HomeView",
  components: {
    LandingPage,
    Navbar,
    Footer,
    About
},
mounted() {
  document
},
};
</script>cd ..

<style scoped>
.landing {
  margin: 30px;
   /* font-family: "Akshar", sans-serif; */
    /* font-family: "Montserrat", sans-serif; */
    /* font-family: "Nunito Sans", sans-serif; */
    /* font-family: "Poppins", sans-serif; */
    /* font-family: "Raleway", sans-serif; */
}
</style>
