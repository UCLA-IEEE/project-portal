<template>
  <div id="login-wrapper">
    <div id="login" class="card shadow--2dp text-center">
      <h1>Sign In</h1>
      <h3>Sign in to track your project progress</h3>

      <form @submit.prevent="handleLogin()">
        <label for="username">Username</label>
        <input type="text" id="username" name="username" v-model="username" placeholder="joebruin" required/>
        <label for="password">Password</label>
        <input type="password" id='password' name="password" v-model="password" placeholder="Password" required/>
        <p :class="['error-message', !accepted ? 'visible' : '']">Invalid username or password</p>
        <button type="submit"><p class="font-fix">Sign In</p></button>
      </form>
      
      <p class="links">
        <router-link :to="{name: 'Register'}">Create an account</router-link> | <router-link :to="{name: 'Reset'}">Forgot my password</router-link>
      </p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Login',
    data() {
      return {
        username: '',
        password: '',
        accepted: true
      }
    },
    methods: {
      handleLogin() {
        this.accepted = true;
        const { username, password } = this;

        this.$store.dispatch('login', { username, password })
        .then(() => {
          if (this.$store.getters.authenticated) {
            this.accepted = true;
            this.$router.push({ name: 'Secure' });
          }
          else {
            this.accepted = false;
          }
        })
      }
    }
  }
</script>

<style>
  #login-wrapper {
    background-color: var(--blue);
    padding-top: calc(50vh - 250px);
    min-height: calc(100vh - 68px);
  }

  #login {
    display: block;
    width: 330px;
    margin: 0 auto;
    padding: 30px;
  }

  #login h1 {
    text-transform: uppercase;
    color: var(--blue);
    margin-top: 0;
  }

  #login h3 {
    margin-top: 0;
  }

  #login label {
    float: left;
    margin-left: 5px;
    margin-bottom: 0;

    font-weight: normal;
  }

  #login input {
    display: block;
    width: 100%;
    margin-bottom: 10px;
    padding-left: 5px;
    padding-top: 0.3em;
  }

  #login .error-message {
    color: var(--red);
    visibility: hidden;
  }

  #login .visible {
    visibility: visible;
  }

  #login .links {
    margin: 20px 0 0;
  }

  /* Media Queries */
  @media only screen and (min-width: 480px) {
    #login {
      width: 440px;
    }
  }
</style>
