import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const state = {
    isLoading: false,
    categories: [],
    category: {},
    products: [],
    product: {},
    isAuthenticated: false,
    token: "",
    quantity: "",
    cart: {
        items: [],
    },
};

const actions = {
    getCategories({commit}) {
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
    getCategory({commit}, payload) {
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
    getProducts({commit}) {
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
    getProductsCategory({commit}, payload) {
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

    userProfile({commit}) {
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
    searchProducts({commit}, payload) {
        axios
            .get("/products/search/" + payload)
            .then((res) => {
                commit("SET_PRODUCTS", res.data);
                console.log(res.data);
            })
            .catch((err) => {
                console.log(err);
            });
    },
    showPassword() {
        $(".toggle-password").click(function () {
            $(this).children().toggleClass("mdi-eye-outline mdi-eye-off-outline");
            let input = $(this).prev();
            input.attr("type", input.attr("type") === "password" ? "text" : "password");
        })
    }
};

const mutations = {

    initializeStore(state) {
        if (localStorage.getItem("cart")) {
            state.cart = JSON.parse(localStorage.getItem("cart"));
        } else {
            localStorage.setItem("cart", JSON.stringify(state.cart));
        }

        if (localStorage.getItem("token")) {
            state.token = localStorage.getItem("token");
            state.isAuthenticated = true;
        } else {
            state.token = "";
            state.isAuthenticated = false;
        }
    },

    addToCart(state, item) {
        const exists = state.cart.items.filter(
            (i) => i.product.id === item.product.id
        );
        if (exists.length) {
            exists[0].quantity =
                parseInt(exists[0].quantity) + parseInt(item.quantity);
        } else {
            state.cart.items.push(item);
        }

        localStorage.setItem("cart", JSON.stringify(state.cart));
    },

    setIsLoading(state, status) {
        state.isLoading = status;
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

    clearCart(state) {
        state.cart.items = [];
        localStorage.setItem("cart", JSON.stringify(state.cart));
    },
};


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
