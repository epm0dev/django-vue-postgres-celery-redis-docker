import Vue from 'vue'
import VueRouter from 'vue-router'
import Posts from './views/Posts'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'posts',
            component: Posts,
        },
    ]
})