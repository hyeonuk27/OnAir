<template>
  <div class="profile-update">
    <div class="profile-update-container"> 
      <div class="profile-info">
        <img 
          class="profile-image"
          :src="profileUrl" 
          alt="profile-image">
        <div class="profile-name">
          20자 이내의 닉네임으로 변경해주세요.
        </div>
        <div class="form__group field">
          <input 
            type="input" 
            id='name' required 
            class="form__field" 
            :value="newName" 
            @input="newName=$event.target.value"
            @keypress.enter="profileUpdate"
          />
          <label for="name" class="form__label">{{newNameLength}}</label>
        </div>
        <vs-button 
          class="profile-update-button" 
          color="#B9A6C9" 
          type="flat" 
          icon="done" 
          :disabled="newName.length > 20" 
          @click="profileUpdate"
        >
          Done
        </vs-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import API from '@/common/drf.js'
import {mapState, mapActions} from 'vuex'

export default {
  name: 'ProfileUpdate',
  data() {
    return {
      newName: '',
      counterDanger: false,
    }
  },
  methods: {
    ...mapActions([
      'setName'
    ]),
    profileUpdate: function () {
      axios({
        url: API.URL + API.ROUTES.updateProfile,
        method: 'put',
        headers: {
          Authorization: this.token,
        },
        data: {
          name: this.newName,
        },
      })
      .then((res) => {
        this.$vs.notify({
          title:'수정 완료', text:`✈ On:Air > ${res.data.name}님 환영합니다.`, color:'#D4C6E2', position:'top-right'
        })
        localStorage.setItem('name', res.data.name)
        this.setName(res.data.name)
        this.$router.go(-1)
      })
    }
  },
  created() {
    this.newName = this.name
  },
  computed: {
    ...mapState([
      'name',
      'profileUrl',
      'token',
    ]),
    newNameLength: function () {
      return this.newName.length.toString() + '/20'
    }
  }
}
</script>

<style>
.form__field {
  background: transparent;
  border: 0;
  border-bottom: 2px solid #656F8C;
  color: #84898C;
  font-family: inherit;
  font-size: 18px;
  outline: 0;
  padding: 1px;
  transition: border-color 0.2s;
  width: 100%;
}
.form__field:focus {
  border-image: linear-gradient(to right, #3D2F6B, #D4C6E2);
  border-image-slice: 1;
  border-width: 3px;
  font-weight: 400;
}
.form__field:focus ~ .form__label {
  color: #B9A6C9;
  display: block;
  font-size: 12px;
  font-weight: 700;
  position: absolute;
  top: 0;
  transition: 0.2s;
}
.form__field::placeholder {
  color: transparent;
}
.form__field:placeholder-shown ~ .form__label {
  cursor: text;
  font-size: 12px;
  top: 20px;
}
.form__field:required, .form__field:invalid {
  box-shadow: none;
}
.form__group {
  padding-top: 15px;
  position: relative;
  margin-left: 300px;
  margin-top: 100px;
  width: 600px;
}
.form__label {
  color: #9b9b9b;
  display: block;
  font-size: 12px;
  position: absolute;
  top: 0;
  transition: 0.2s;
}
.profile-update {
  display: flex;
  justify-content: center;
  margin-top: 150px;
}
.profile-update-button {
  margin-left: 812px;
}
.profile-update-container {
  min-height: 650px;
  width: 1190px;
}
</style>