<template>
    <div>
        <div class="banner"></div>
        <h1>This is the Home page</h1>
        <h1>Welcome to my home page, here is a list of all my posts</h1>
        <hr>
        <h2>{{ posts }}</h2>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
          posts: []
        }
    },
    created() {
        axios.get('http://127.0.0.1:8000/api/posts').then((res) => {
        this.posts = res.data
        console.log(res.data)
        })
    },
}
</script>

