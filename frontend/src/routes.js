import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from './views/Login'
import Logout from './views/Logout'
import Cars from './views/Cars'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/login',
            name: 'login',
            component: Login,
        },
        {
            path: '/logout',
            name: 'logout',
            component: Logout,
        },
        {
            path: '/',
            name: 'cars',
            component: Cars,
            meta: {
                requiresLogin: true
            }
        },
    ]
})