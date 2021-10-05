<template>
  <div class="profile">
    <div class="profile-container">
      <div v-if="isRendered" class="profile-info">
        <img 
        class="profile-image"
        :src="profileUrl" 
        alt="profile-image">
        <div class="profile-name">
          {{name}}
        </div>
      </div>
      <div v-else style="height: 204px;">
      </div>
      <div class="profile-tabs">
        <vs-button v-if="profileId == userId" class="profile-tab" :color="colorx" type="line" @click.native="goProfileUpdate">닉네임 수정</vs-button>
        <vs-button class="profile-tab" :color="colorx" type="line" @click.native="goMyReview">남긴 리뷰</vs-button>
        <vs-button v-if="profileId == userId" class="profile-tab" :color="colorx" type="line" @click.native="goSearchLog">검색 기록</vs-button>
        <vs-button class="profile-tab" :color="colorx" type="line" onclick="window.open('https://www.notion.so/jiu-park/4a14719b6de04f31bcbd932e8d2032b5')">1:1문의</vs-button>
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
      isRendered: false,
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
          this.isRendered = true
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goProfileUpdate: function () {
      this.$router.push({ name: "ProfileUpdate" , params: { userId: this.userId, name : this.name, profileUrl : this.profileUrl }})
    },
    goMyReview: function () {
      this.$router.push({ name: "MyReview", params: { userId: this.userId }})
    },
    goSearchLog: function () {
      this.$router.push({ name: "SearchLog", params: { userId: this.userId }})
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
    align-items: center;
    margin-top: 150px;
  }

  .profile-container {
    width: 1190px;
    min-height: 650px;
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