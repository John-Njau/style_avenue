<template>
  <div class="m-0 p-0 sticky-top">
    <b-navbar toggleable="lg" type="dark" class="px-2 navbar">
      <img
        src="../assets/images/style_avenue_logo.jpg"
        alt=""
        class="img-fluid logo"
      />
      <b-navbar-brand href="/">Style Avenue Studio</b-navbar-brand>

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
            <b-dropdown-item href="#">Make Up Session</b-dropdown-item>
            <b-dropdown-item href="#">Make Up Classes</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown class="my-account">
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <em class="bold">My Account</em>
            </template>
              <template v-if="$store.state.isAuthenticated">

            <div class="m-2 p-2">
              <router-link to="/about">Profile</router-link> <br />
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
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <hr class="hr mt-0 mb-0" />
    <div class="options text-white m-0 p-0">
      <ul>
        <li>
          <router-link to="/category">Make Up</router-link>
        </li>
        <li>
          <router-link to="/category">Fragrance</router-link>
        </li>
        <li>
          <router-link to="/category">Hair</router-link>
        </li>
        <li>
          
          <router-link to="/booking">Book</router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";


export default {
  methods: {
    signOut(){
      axios.defaults.headers.common["Authorization"] ="";

      localStorage.removeItem("token");
      localStorage.removeItem("email");
      localStorage.removeItem("userId");

      localStorage.removeItem("username");

      this.$store.commit("removeToken");

      this.$router.push("/")
    }
  },
};
</script>

<style>
.search,
.categories,
.my-account {
  width: 200px;
  margin: auto;
}
router-link {
  color: #42b983;
  text-decoration: none;
  text-justify: newspaper;
}
.logo {
  width: 40px;
  /* height: 90px; */
  /* margin-top: -10px; */
  /* border-block: 1px solid #080705; */

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
  border: 2px solid #f0f0d6;
  width: 100%;
  opacity: 0.8;
  /* margin-top: 10px; */
  /* margin-bottom: 10px; */
}
</style>