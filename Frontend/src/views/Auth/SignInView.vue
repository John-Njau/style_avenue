<template>
  <div class="sign-in">
    <SignIn />
  </div>
</template>

<script>
import SignIn from "@/components/Auth/SignIn.vue";

export default {
  components: {
    SignIn,
    SignIn,
  },
  data() {
    return {
      title: "Style Avenue Studio",
    };
  },
  mounted() {
    document.title = this.title;
  },
};
</script>

<style>
</style>