<template>
  <main>
    <section>
      My Profile
      <h1>
        {{ profile.name }}
        {{ name }}
        {{ isAuthenticated }}
        <template>
          <div v-if="user">
            {{ user.results }}
          </div>
          <div v-else>No user Found</div>
        </template>
      </h1>
    </section>
  </main>
</template>

<script>
import axios from "axios";

export default {
  components: {},
  data() {
    return {
      profile: {
        name: "John Doe",
        email: "",
      },
    };
  },
  methods: {
    getUserProfile() {
      axios
        .get("http://localhost:8000/profile")
        .then((response) => {
          this.profile = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    this.getUserProfile();
    this.$store.dispatch("userProfile");
  },

  computed: {
    name() {
      return this.profile.name;
    },
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    },
    user() {
      return this.$store.state.user;
    },
  },
};
</script>

<style>
</style>