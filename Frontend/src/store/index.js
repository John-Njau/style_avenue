import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const state = {
  isLoading: false,
  categories: [],
  products: [],
  cart: [],
  cartTotal: 0,
  orders: [],
  order: {},
  isAuthenticated: false,
  token: "",
  // email: "",
  // password: "",
  // confirmPassword: "",
  // errors: [],
};

const actions = {
  getCategories({ commit }) {
    axios
      .get("/api/categories/")
      .then((res) => {
        commit("SET_CATEGORIES", res.data);
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  getProducts({ commit }) {
    axios
      .get("/api/products/")
      .then((res) => {
        commit("SET_PRODUCTS", res.data);
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};

const mutations = {
  initializeStore(state) {
    if (localStorage.getItem("token")) {
      state.token = localStorage.getItem("token");
      state.isAuthenticated = true;
    } else {
      state.token = "";
      state.isAuthenticated = false;
    }
  },

  SET_CATEGORIES(state, categories) {
    state.categories = categories;
  },
  SET_PRODUCTS(state, products) {
    state.products = products;
  },
  setToken(state, token) {
    state.token = token;
    state.isAuthenticated = true;
  },
  removeToken(state) {
    state.token = "";
    state.isAuthenticated = false;
  },
};

// const setters = {
//   getEmail(state) {
//     return state.email;
//   },
//   getPassword(state) {
//     return state.password;
//   },
//   getConfirmPassword(state) {
//     return state.confirmPassword;
//   },
//   getErrors(state) {
//     return state.errors;
//   }

// };

const getters = {};

const modules = {};

export default new Vuex.Store({
  state,
  getters,
  // setters,
  actions,
  mutations,
  modules,
});
