import Vue from "vue";
import Vuex from "vuex";
import VueRouter from "vue-router";
import HomeView from "../views/LandingPage/LandingView.vue";
import SignInView from "../views/Auth/SignInView.vue";
import RegisterView from "../views/Auth/SignUpView.vue";
import CategoryView from "../views/Categories/CategoryView.vue";
import ClassesView from "../views/Classes/ClassesView.vue";
import CartView from "../views/Cart/CartView.vue";
import ErrorPage from "../views/Error/ErrorPage.vue";

Vue.use(VueRouter);
Vue.use(Vuex);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/profile",
    name: "profile",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/Profile/ProfileView.vue"),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/signin",
    name: "signin",
    component: SignInView,
  },
  {
    path: "/signup",
    name: "signup",
    component: RegisterView,
  },
  {
    path: "/category/:id",
    name: "category",
    component: CategoryView,
    props: true,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/booking",
    name: "booking",
    component: () => import("../views/Booking/BookingView.vue"),
    meta: {
      requiresAuth: true,
    },
  },

  {
    path: "/classes",
    name: "classes",
    component: ClassesView,
  },
  {
    path: "/cart",
    name: "cart",
    component: CartView,
  },
  //  catchall, 404 page
  {
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: ErrorPage,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});



// router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  // const publicPages = ["/", "/signup", "/signin"];
  // console.log(to.path);
  // const authRequired = !publicPages.includes(to.path);
  // console.log("authRequired", authRequired);
  // const loggedIn = localStorage.getItem("token");
  // console.log("LoggedIn "+loggedIn);

  // if (authRequired && !loggedIn) {
  //   return next("/signin");
  // }

  // next();
// });

export default router;
