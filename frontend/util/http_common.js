import Vue from 'vue'
import axios from 'axios'
import store from '@/store/modules/Header.js'

export default new Vue({
  computed: {
    token () {
      return store.state.token
    },
    axios () {
      return axios.create({
        baseURL: 'http://j3a111.p.ssafy.io:8000',
        headers: {
          Authorization: this.token ? this.token : '',
          'Content-type': 'application/json'
        }
      })
    },
    formAxios () {
      return axios.create({
        baseURL: 'http://j3a111.p.ssafy.io:8000',
        headers: {
          Authorization: this.token ? this.token : '',
          'Content-Type': 'multipart/form-data'
        }
      })
    }
  }
})
