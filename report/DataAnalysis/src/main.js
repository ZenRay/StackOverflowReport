// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle'
import NavBar from './components/NavBar'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#nav',
  components: { NavBar },
  template: '<NavBar/>'
})
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
