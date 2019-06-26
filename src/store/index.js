import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API = 'http://127.0.0.1:8000/api/'

export default new Vuex.Store({
  state: {
    list: [],
  },
  getters: {
    getList(state) {
      return state.list;
    }
  },
  actions: {
    asynSetList({
      commit
    }) {
      // let list = JSON.parse(localStorage.getItem("todoList") || "[]");
      axios.get(API + 'todos/')
        .then(
          (response) => {
            console.log(response)
            commit('setList', response.data)
          }
        ).catch(
          (err) => {
            console.log(err);
          }
        )
    },
    asyncPushList({
      commit,
      dispatch
    }, payload) {
      axios.post(API + 'todos/', payload)
        .then(res => {
          console.log(res)
          // commit('pushList', res.data)
          dispatch("asynSetList");
        })
        .catch(err => console.log(err))
    },
    asyncSpliceItem({
      commit,
      dispatch
    }, payload) {
      axios.delete(`${API}todos/${payload}/`)
        .then((res) => {
          console.log(res)
          dispatch("asynSetList");
        })
        .catch(err => console.log(err))
    }
  },
  mutations: {
    setList(state, payload) {
      state.list = payload
    }
  }
})