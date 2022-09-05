<template>
  <Classes />
</template>

<script>
import axios from "axios";
import Classes from "@/components/Classes/classes.vue";

export default {
  components: {
    Classes,
  },
  data() {
    return {
      title: "Classes | Style Avenue Studio",
    };
  },
  mounted() {
    document.title = this.title.toUpperCase();
  },
};
</script>

<style>
</style>