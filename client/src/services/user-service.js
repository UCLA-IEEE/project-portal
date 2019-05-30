import axios from "axios";

export const userService = {
  login
};

function login(username, password) {
  return axios({
    method: "POST",
    "url": "http://localhost:5000/auth/login",
    "data": {
      username: username,
      password: password
    },
    "headers": { "Content-Type": "application/json",
                 "Access-Control-Allow-Origin": '*' }
  });
}
