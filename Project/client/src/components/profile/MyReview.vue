<template>
  <div>
  </div>
</template>

<script>
import axios from "axios"
import API from "@/common/drf.js"
import {mapState} from 'vuex'

export default {
  name: 'MyReview',
  data() {
    return {

    }
  },
  methods: {
    getMyReviews: function () {
      axios({
        url: API.URL + API.ROUTES.getMyReviews + this.userId + '/reviews/',
        method: "put",
        headers: {
          Authorization: this.token
        },
        data: {
          name: this.newName
        }
      })
        .then((res) => {
          this.$vs.notify({
            title:'수정 완료', text:`✈ On:Air > ${res.data.name}님 환영합니다.`, color:'#D4C6E2', position:'top-right'
          })
          localStorage.setItem('name', res.data.name)
          this.setName(res.data.name)
          this.$router.go(-1)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {

  },
  computed: {
    ...mapState([
      'userId'
    ])
  }
}
</script>

<style>

</style>