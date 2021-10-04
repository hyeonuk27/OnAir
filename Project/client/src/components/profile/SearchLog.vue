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
      <div class="search-log-default" v-if="logs.length == 0">
        검색 내역이 없습니다.
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

  .search-log-default {
    border: 1px solid rgba(180, 180, 180, 0.658);
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.151);
    width: 1000px;
    height: 150px;
    padding: 40px;
  }

  .search-log-img {
    border-radius: 70%;
    margin-right: 50px;
    object-fit: cover;
    width: 100px;
  }
</style>