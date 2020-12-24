<template>
    <div>
        <nav>
            <ul class="navbar-nav mr-auto">
                <li class="nav-item" v-if="accessToken=null">
                    <router-link :to="{ name:'login' }">Login</router-link>
                </li>
                <li class="nav-item" v-if="accessToken!=null">
                    <router-link :to="{ name:'logout' }">Logout</router-link>
                </li>
            </ul>
        </nav>
    </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
    name: 'Navbar',
    computed: mapState(['accessToken'])
}
</script>

<style scoped>
</style>