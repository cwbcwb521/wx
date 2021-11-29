import Vue from "vue";
import VueRouter from "vue-router";

// 引入组件
import Index from "../pages/index.vue";
import Home from "../pages/home.vue";
import User from "../pages/user.vue";
import Jisuan from "../pages/jisuan.vue";

// 要告诉 vue 使用 vueRouter
Vue.use(VueRouter);

const routes = [
    {
        path:"/",
        name:"index",
        component: Index,
        redirect:"/home",
        children:[
            {
                path:"/home",
                name:"home",
                component: Home
            },
            {
                path:"/user",
                name:"user",
                component: User
            },
            {
                path:"/jisuan",
                name:"jisuan",
                component: Jisuan
            }
        ]
    },
    
]

var router =  new VueRouter({
    routes
})
export default router;