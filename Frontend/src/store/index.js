import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const state = {
  isLoading: false,
  categories: [],
  products: [],
  isAuthenticated: false,
  token: "",
  category: {},
  user: {},
  cart: [],
  // cartTotal: 0,
  // orders: [],
  // order: {},
  // email: "",
  // password: "",
  // confirmPassword: "",
  // errors: [],
};

const actions = {
  getCategories({ commit }) {
    axios
      .get("/categories/")
      .then((res) => {
        commit("SET_CATEGORIES", res.data);
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  getCategory({ commit }, payload) {
    axios
      .get(`/categories/${payload}/`)
      .then((res) => {
        commit("SET_CATEGORY", res.data);
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  getProducts({ commit }) {
    axios
      .get("/products/")
      .then((res) => {
        commit("SET_PRODUCTS", res.data);
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  getProductsCategory({ commit }, payload) {
    axios
      .get("/products/category/" + payload)
      .then((res) => {
        commit("SET_PRODUCTS", res.data);
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },

  userProfile({ commit }) {
    axios
      .get("/auth/users/1")
      .then((res) => {
        commit("SET_USER", res.data);
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

  SET_USER(state, user) {
    state.user = user;
  },

  SET_CATEGORIES(state, categories) {
    state.categories = categories;
  },
  SET_CATEGORY(state, category) {
    state.category = category;
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
