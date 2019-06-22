import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

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
      let list = JSON.parse(localStorage.getItem("todoList") || "[]");
      console.log('asynSetList' + list)
      commit('setList', list)
    }
  },
  mutations: {
    setList(state, payload) {
      state.list = payload
    },
    pushList(state, payload) {
      state.list.push(payload);
    },
    spliceItem(state, payload) {
      state.list.splice(payload, 1);
    }
  }
})