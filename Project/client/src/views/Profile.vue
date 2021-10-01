<template>
  <div class="profile">
    <div class="profile-container">
      <div class="profile-info">
        <img 
        class="profile-image"
        :src="profileUrl" 
        alt="profile-image">
        <div class="profile-name">
          {{name}}
        </div>
      </div>
      <div class="profile-tabs">
        <vs-button v-if="profileId == userId" class="profile-tab" :color="colorx" type="line">회원정보수정</vs-button>
        <vs-button class="profile-tab" :color="colorx" type="line">남긴 리뷰</vs-button>
        <vs-button v-if="profileId == userId" class="profile-tab" :color="colorx" type="line">검색 기록</vs-button>
        <vs-button class="profile-tab" :color="colorx" type="line">1:1문의</vs-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import API from "@/common/drf.js"

export default {
  name: 'Profile',
  data() {
    return {
      colorx:'#656F8C',
      profileId: '',
      userId: localStorage.getItem('userId'),
      name: '',
      profileUrl: '',
    }
  },
  methods: {
    getProfile: function () {
      axios({
        url: API.URL + API.ROUTES.getProfile + this.profileId + '/',
        method: "get",
      })
        .then((res) => {
          this.name = res.data.name
          this.profileUrl = res.data.profile_url
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.profileId = this.$route.params.userId
    this.getProfile()
  }
}
</script>

<style>
  .profile {
    display: flex;
    justify-content: center;
    margin-top: 99.19px;
  }

  .profile-container {
    width: 1190px;
  }

  .profile-image {
    border-radius: 70%;
    object-fit: cover;
    height: 150px;
    width: 150px;
  }

  .profile-info {
    margin: 60px 0px;
  }

  .profile-name {
    margin-top: 30px;
  }

  .profile-tab {
    margin: 0 20px;
    width: 120px;
  }

  .profile-tabs {
    margin-top: 70px;
  }
</style>