<template>
    <div>
        <h1>Please sign in</h1>
        <p v-if="incorrectAuth">Incorrect username or password entered - please try again</p>
        <form v-on:submit.prevent="login">
            <div>
                <label for="user">Username</label>
                <input type="text" name="username" id="user" v-model="username">
            </div>
            <div class="form-group">
                <label for="pass">Password</label>
                <input type="password" name="password" id="pass" v-model="password">
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'login',
    data() {
        return {
            username: '',
            password: '',
            incorrectAuth: false
        }
    },
    methods: {
        login() {
            this.$store.dispatch('userLogin', {
                username: this.username,
                password: this.password
            })
                .then(() => {
                    this.$router.push({name: 'cars'})
                })
                .catch(err => {
                    console.log(err)
                    this.incorrectAuth = true
                })
        }
    }
}
</script>

<style scoped>
</style>