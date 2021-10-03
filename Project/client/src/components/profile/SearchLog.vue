<template>
  <div class="search-log">
    <div class="search-log-container">
      <div>
        <img class="search-log-img" :src="profileUrl" alt="">
      </div>
      <div>
        <SearchLogElement
        v-for="(log, idx) in logs"
        :key="idx"
        :log="log"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import API from "@/common/drf.js"
import {mapState} from 'vuex'
import SearchLogElement from '@/components/profile/SearchLogElement'

export default {
  name: 'SearchLog',
  components: {
    SearchLogElement,
  },
  data() {
    return {
      logs: [],
    }
  },
  methods: {
    getSearchLogs: function () {
      console.log(API.URL + API.ROUTES.getSearchLogs)
      axios({
        url: API.URL + API.ROUTES.getSearchLogs,
        method: "get",
        headers: {
          Authorization: this.token,
        },
      })
        .then((res) => {
          this.logs = res.data
          console.log(this.logs)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.getSearchLogs()
  },
  computed: {
    ...mapState([
      'token',
      'profileUrl'
    ])
  }
}
</script>

<style>
  .search-log {
    display: flex;
    justify-content: center;
    margin-top: 150px;
  }

  .search-log-container {
    display: flex;
    justify-content: center;
    width: 1190px;
  }

  .search-log-img {
    border-radius: 70%;
    margin-right: 50px;
    object-fit: cover;
    width: 100px;
  }
</style>