<template>
    <div id="login">
        <h1>Login</h1>
        <p>Sign in to track your project progress!</p>
        <label for="username">Email</label>
        <input id='username' type="text" name="username" v-model="input.username" placeholder="joebruin@g.ucla.edu" />
        <label for="password">Password</label>
        <input id='password' type="text" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click="login()">Login</button>
    </div>
</template>

<script>
    export default {
        name: 'Login',
        data() {
            return {
                input: {
                    username: "",
                    password: ""
                }
            }
        },
        methods: {
            login() {
                if(this.input.username != "" && this.input.password != "") {
                    if(this.input.username == this.$parent.mockAccount.username && this.input.password == this.$parent.mockAccount.password) {
                        this.$emit("authenticated", true);
                        this.$router.replace({ name: "Secure" });
                    } else {
                        console.log("The username and / or password is incorrect");
                    }
                } else {
                    console.log("A username and password must be present");
                }
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
    #login p {
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
      transition: background-color 0.3s ease, color 0.3s ease;
    }
    #login button:hover {
      background-color: #68A0BF;
      cursor: pointer;
    }
    label {
      font-size: 14px;
    }
    input[type=text], select {
      width: 100%;
      padding: 5px 10px;
      margin: 8px 0;
      display: inline-block;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
    }
</style>
