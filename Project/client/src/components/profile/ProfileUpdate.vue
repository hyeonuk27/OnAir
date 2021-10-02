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
          <input type="input" class="form__field" :value="newName" id='name' required @input="newName=$event.target.value"/>
          <label for="name" class="form__label">{{newNameLength}}</label>
        </div>
        <vs-button class="profile-update-button" color="#B9A6C9" type="flat" icon="done" :disabled="newName.length > 20" @click="profileUpdate">Done</vs-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import API from "@/common/drf.js"
import {mapState, mapActions} from 'vuex'

export default {
  name: 'ProfileUpdate',
  data() {
    return {
      newName: "",
      counterDanger: false,
    }
  },
  methods: {
    ...mapActions(
      ['setName']
      ),
    profileUpdate: function () {
      axios({
        url: API.URL + API.ROUTES.updateProfile,
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
    }
  },
  created() {
    this.newName = this.name
  },
  computed: {
    ...mapState([
      'name',
      'profileUrl',
      'token'
    ]),
    newNameLength: function () {
      return this.newName.length.toString() + '/20'
    }
  }
}
</script>

<style>
  .form__group {
    position: relative;
    padding-top: 15px;
    margin-top: 100px;
    margin-left: 300px;
    width: 600px;
  }

  .form__field {
  font-family: inherit;
  width: 100%;
  border: 0;
  border-bottom: 2px solid #656F8C;
  outline: 0;
  font-size: 18px;
  color: #84898C;
  padding: 1px;
  background: transparent;
  transition: border-color 0.2s;
}
.form__field::placeholder {
  color: transparent;
}
.form__field:placeholder-shown ~ .form__label {
  font-size: 12px;
  cursor: text;
  top: 20px;
}

.form__label {
  position: absolute;
  top: 0;
  display: block;
  transition: 0.2s;
  font-size: 12px;
  color: #9b9b9b;
}

.form__field:focus {
  font-weight: 400;
  border-width: 3px;
  border-image: linear-gradient(to right, #3D2F6B, #D4C6E2);
  border-image-slice: 1;
}
.form__field:focus ~ .form__label {
  position: absolute;
  top: 0;
  display: block;
  transition: 0.2s;
  font-size: 12px;
  color: #B9A6C9;
  font-weight: 700;
}

/* reset input */
.form__field:required, .form__field:invalid {
  box-shadow: none;
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
    width: 1190px;
  }
</style>