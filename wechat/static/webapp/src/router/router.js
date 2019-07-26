import Vue from "vue";
import VueRouter from "vue-router";

// 引入组件
import Index from "../pages/index.vue";
import Login from "../pages/login.vue";

// 要告诉 vue 使用 vueRouter
Vue.use(VueRouter);

const routes = [
    {
        path:"/",
        name:"index",
        component: Index
    },
    {
        path:"/login",
        name:"login",
        component: Login
    }
]

var router =  new VueRouter({
    routes
})
export default router;