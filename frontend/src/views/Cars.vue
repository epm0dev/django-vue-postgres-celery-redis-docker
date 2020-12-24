<template>
    <div>
        <NavBar></NavBar>
        <h1>Hello World!</h1>
        <ul>
            <li v-for="car in APIData" :key="car.url">{{ car.manufacturer }} {{ car.model }} with a
                {{ car.engine_size }}L V{{ car.engine_cylinders }} engine
            </li>
        </ul>
    </div>
</template>

<script>
import NavBar from '../components/Navbar'
import {getAPI} from '../axios-api'
import {mapState} from 'vuex'

export default {
    name: 'Cars',
    onIdle() {
        this.$store.dispatch('userLogout')
            .then(() => {
                this.$router.push({name: 'login'})
            })
    },
    components: {
        NavBar
    },
    computed: mapState(['APIData']),
    created() {
        getAPI.get('/cars/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
            .then(response => {
                this.$store.state.APIData = response.data
            })
            .catch(err => {
                console.log(err)
            })
    }
}
</script>

<style scoped>
</style>