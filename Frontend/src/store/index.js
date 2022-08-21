import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const state = {
  user: {},
  token: localStorage.getItem("token") || "",
  isLoggedIn: false,
  isAdmin: false,
  isLoading: false,
  categories: [],
  products: [],
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
  SET_CATEGORIES(state, categories) {
    state.categories = categories;
  },
  SET_PRODUCTS(state, products) {
    state.products = products;
  },
};

const getters = {};

const modules = {};

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations,
  modules,
});
