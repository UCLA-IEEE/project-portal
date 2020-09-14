<template>
    <div id="login">
        <h1>Login</h1>
        <p class='subtitle'>Sign in to track your project progress!</p>
        <label for="username">Email</label>
        <input type="text" id='username' name="username" v-model="username" placeholder="joebruin@g.ucla.edu"/>
        <label for="password">Password</label>
        <input type="password" id='password' name="password" v-model="password" placeholder="Password" @keyup.enter="handleLogin()"/>
        <p class='error-message' v-show="isValid()">Invalid username or password.</p>
        <button type="button" v-on:click="handleLogin()">Login</button>
    </div>
</template>

<script>
    export default {
        name: 'Login',
        data() {
            return {
                username: '',
                password: '',
                submitted: false,
                accepted: true
            }
        },
        methods: {
            handleLogin() {
              this.submitted = true;
              const { username, password } = this;

              // Stop here if form is invalid
              if (!(username && password)) {
                return;
              }

              this.$store.dispatch('login', { username, password })
              .then(() => {
                if (this.$store.getters.authenticated) {
                  this.accepted = true;
                  this.$router.replace({ name: 'Secure' });
                }
                else {
                  this.accepted = false;
                }
              })
            },
            isValid() {
              return this.submitted && (!this.password || !this.username || !this.accepted);
            }
        }
    }
</script>

<style scoped>
    #login {
        width: 400px;
        border: 1px solid #CCCCCC;
        border-radius: 12px;
        margin: auto;
        margin-top: 100px;
        padding: 15px;
        color: #1F6891;
    }
    #login h1 {
      font-size: 16px;
      text-transform: uppercase;
      margin: 0;
    }
    .subtitle {
      font-size: 14px;
      margin: 0 0 10px 0;
    }
    #login button {
      background-color: #1F6891;
      color: white;
      border-radius: 5px;
      font-size: 12px;
      padding: 5px 20px;
      border: 0;
      transition: background-color 0.3s ease;
    }
    #login button:hover {
      background-color: #68A0BF;
      cursor: pointer;
    }
    label {
      font-size: 14px;
      font-weight: normal;
    }
    input, select {
      width: 100%;
      padding: 5px 10px;
      margin: 8px 0;
      display: inline-block;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
    }
    .error-message {
      color: #d02626;
      margin: 0 0 10px 0;
      font-size: 12px;
    }
</style>
