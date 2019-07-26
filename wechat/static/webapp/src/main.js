import Vue from 'vue'
import App from './App.vue'

// material UI

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import router from './router/router'

Vue.config.productionTip = false
//material UI
Vue.use(VueMaterial)

// eslint-disable-next-line no-console
console.log(Vue.material)

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
