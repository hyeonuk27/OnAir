<template>
  <div class="profile">
    <div class="profile-container">
      <div class="profile-info">
        <img 
        class="profile-image"
        src="@/assets/main.jpg" 
        alt="profile-image">
        <div class="profile-name">
          온에어
        </div>
      </div>
      <div class="profile-tabs">
        <vs-button class="profile-tab" :color="colorx" type="line">회원정보수정</vs-button>
        <vs-button class="profile-tab" :color="colorx" type="line">내가 남긴 리뷰</vs-button>
        <vs-button class="profile-tab" :color="colorx" type="line">검색 기록</vs-button>
        <vs-button class="profile-tab" :color="colorx" type="line">1:1문의</vs-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Profile',
  data() {
    return {
      colorx:'#656F8C',
    }
  },
  methods: {

  },
  created() {

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
    height: 180px;
    width: 180px;
  }

  .profile-info {
    margin: 30px 0px;
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