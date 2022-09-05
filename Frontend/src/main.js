import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'jquery/src/jquery.js'
import 'bootstrap/dist/js/bootstrap.min.js'

axios.defaults.baseURL = 'http://127.0.0.1:8000/';


Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

new Vue({
  router,
  store,
  axios,
  render: h => h(App)
}).$mount('#app')
