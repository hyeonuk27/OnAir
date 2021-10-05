<template>
  <div>
    <div class="login-container">
      <div>
        <img src="@/assets/login.png" style="width: 500px;" alt="login-image">
      </div>
      <div class="d-flex justify-content-center m-2">
        <LoginButton />
      </div>

    </div>
  </div>
</template>

<script>
import LoginButton from "@/components/auth/LoginButton"

export default {
  name: 'Login',
  components: {
    LoginButton,
  },
  methods: {

  },
  
}
</script>

<style>
  .login-container {
    margin-top: 20vh;
  }
</style>