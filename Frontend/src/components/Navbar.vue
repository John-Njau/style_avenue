<template>
  <nav class="p-0 sticky-top">
    <b-navbar toggleable="lg" type="dark" class="px-2 navbar">
      <img
        src="../assets/images/style_avenue_logo.jpg"
        alt=""
        class="img-fluid logo"
      />
      <b-navbar-brand class="text-uppercase fw-bold" href="/"
        >Style Avenue Studio</b-navbar-brand
      >

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" class="navbar-right" is-nav>
        <!-- Right aligned nav items -->
        <div class="search"></div>
        <b-navbar-nav class="ml-auto">
          <b-nav-form class="search">
            <b-form-input
              size="sm"
              class="m-sm-2 my-2 my-sm-0"
              placeholder="Search"
            ></b-form-input>
            <!-- <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button> -->
          </b-nav-form>

          <b-nav-item-dropdown text="Book" class="categories" right>
            <b-dropdown-item href="/booking">Make Up Session</b-dropdown-item>
            <b-dropdown-item href="/booking">Make Up Classes</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown class="my-account">
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <span class="bold">Account</span>
            </template>
            <template v-if="$store.state.isAuthenticated">
              <div class="m-2 p-2">
                <router-link to="/profile">Profile</router-link> <br />
                <div class="is-danger" @click="signOut()">Sign Out</div>
              </div>
            </template>
            <template v-else>
              <div class="m-2 p-2">
                <router-link to="/signin">Log in</router-link> <br />
                <router-link to="/signup">Sign up</router-link>
              </div>
            </template>
          </b-nav-item-dropdown>
          <b-nav-item class="text-center">
            <router-link to="/cart">
              <i class="fas fa-shopping-cart"></i>
              <span class="badge badge-pill badge-light h2">
                {{ $store.state.cart.length }}
              </span>
            </router-link>
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <hr class="hr mt-0 mb-0" />
    <div class="options text-white m-0 p-0">
      <ul v-for="category in categories.results" :key="category.id">
        <li>
          <router-link
            class="nav-btns"
            :to="{ name: 'category', params: { id: category.id } }"
            >{{ category.name }}</router-link
          >
        </li>
      </ul>
      <ul>
        <li>
          <router-link class="nav-btns" to="/booking">Book</router-link>
        </li>
        <li>
          <router-link class="nav-btns" to="/classes">Classes</router-link>
        </li>
      </ul>
      <!-- <li v-if="category.id">
          <router-link :to="{ name: 'category', params: { id: category.id } }">Fragrance</router-link>
        </li>
        <li v-if="category.id">
          <router-link to="/category">HairCare</router-link>
        </li>
        <li>
          <router-link to="/category">SkinCare</router-link>
        </li>
        <li>
          <router-link to="/booking">Book</router-link>
        </li>
        <li>
          <router-link to="/classes">Classes</router-link>
        </li> -->
    </div>
  </nav>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      title: "Style Avenue Studio",
    };
  },
  methods: {
    signOut() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("email");
      localStorage.removeItem("userId");

      localStorage.removeItem("username");

      this.$store.commit("removeToken");

      this.$router.push("/");
    },
  },
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    },

    categories() {
      return this.$store.state.categories;
    },
  },
  mounted() {
    this.$store.dispatch("getCategories");
    console.log(this.$store.state.isAuthenticated);
  },
};
</script>

<style>
.search,
.categories,
.my-account {
  width: auto;
  margin: auto;
}

/* .nav-btns {
  color: rgb(32, 29, 29);
  text-decoration: none;
} */

nav a {
  font-weight: lighter;
  color: #1d1b1b;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #f2f5ec;
  /* background-color: #443742; */
  border-radius: 3px;
}

.nav-btns:hover {
  color: #ebe8e2;
  text-decoration: none;
}

.options {
  padding: 0;
  margin: 0;
  /* height: 40px; */
  display: flex;
  /* justify-content: space-around; */
  justify-content: center;
  align-items: center;
  font-size: 1.2rem;
  letter-spacing: 1px;
  text-decoration: none;
  text-align: center;
  list-style: none;
  /* background-color: #121211; */
  background-color: #be8b2c;
}

.options ul {
  backface-visibility: hidden;
  list-style-type: none;
  display: flex;
  /* flex-direction: column; 
  /* /* background-color: #080705;  */
  justify-content: center;
  padding: 0;
  margin: 0;
}

.logo {
  width: 40px;
  border-radius: 50%;
  margin: 0 5px;
  position: relative;
}
.navbar {
  background-color: #be8b2c;
  /* box-shadow: 1px 1px 1px 1px rgb(190, 139, 44); */
  /* border-radius: 3px; */
}

.hr {
  /* border: 2px solid #f0f0d6; */
  /* border: 2px solid #141414; */
  border: 2px solid #131212;
  width: 100%;
  opacity: 1.8;
  /* margin-top: 10px; */
  /* margin-bottom: 10px; */
}
nav {
  padding: 30px;
}

/* .options ul {
  list-style-type: none;
  display: flex;
  /* flex-direction: column; 
  /* background-color: #080705; 
  /* justify-content: center; 
  padding: 0;
  margin: 0;
} */
.options ul li {
  padding: 5px;
  margin: 5px 10px;
  border-radius: 5px;
  text-align: center;
  background-color: #e2962d;
}

.options ul li:hover {
  background-color: #443742;
  color: #fafafa !important;
  box-shadow: 1px 1px 1px 1px #e2962d;
}
</style>