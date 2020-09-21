// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import axios from 'axios'
// import VueRouter from 'vue-router'
import Routes from './router/index'
import './styles/style.css'


// Vue.use(VueRouter);
Vue.prototype.$axios = axios;

// const router = new VueRouter({
//   routes: Routes,
//   mode: 'history'
// })


Vue.config.productionTip = false



/* eslint-disable no-new */
new Vue({
  el: '#app',
  router: Routes,
  components: { App },
  template: '<App/>'
})


