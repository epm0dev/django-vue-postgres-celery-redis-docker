<template>
    <div class="posts">
        <h1>Hello World!</h1>
        <ul>
            <li v-for="car in APIData" :key="car.url">{{car.manufacturer}} {{car.model}} with a {{car.engine_size}}L V{{car.engine_cylinders}} engine</li>
        </ul>
    </div>
</template>

<script>
    import { getAPI } from '../axios-api'
    export default {
        name: 'Posts',
        data () {
            return {
                APIData: []
            }
        },
        created () {
            getAPI.get('/cars/',)
                .then(response => {
                    console.log('Post API has received data')
                    console.log(response.data.results)
                    this.APIData = response.data.results
                })
                .catch(err => {
                    console.log(err)
                })
        }
    }
</script>

<style scoped>

</style>