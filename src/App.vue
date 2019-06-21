<template>
  <div id="app">
    <header>Todo List</header>
    <section class="input">
      <input type="text" v-model="value" @keyup.enter="addItem">
      <button @click="addItem">제출</button>
    </section>
    <section>
      <ul>
        <li v-for="(item,index) in list" :key="index">
          <input class="item" ref="item" readonly type="text" :value="item">
          <button ref="modifyBtn" @click="modifyItem(index)">수정</button>
          <button @click="removeItem(index)">제거</button>
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
const STORAGE_KEY = "todoList";
var todoStorage = {
  fetch: function() {
    var todos = localStorage.getItem(STORAGE_KEY) || "[]";
    todos = JSON.parse(todos);
    return todos;
  },
  save: function(todos) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(todos));
  }
};

export default {
  name: "app",
  data() {
    return {
      value: "",
      valueToModify: "",
      prevModifiedItem: null,
      presentModifiedItem: null,
      list: todoStorage.fetch()
    };
  },
  watch: {
    list: function(todos) {
      console.log("리스트변경");
      todoStorage.save(todos);
    }
  },
  // 5. methods
  methods: {
    addItem() {
      if (this.value) {
        this.list.push(this.value);
        this.value = "";
      }
    },
    removeItem(index) {
      this.list.splice(index, 1);
    },
    modifyItem(index) {
      let prev = this.prevModifiedItem;
      if (prev !== null) {
        let item = this.$refs["item"][prev];
        let modifyBtn = this.$refs["modifyBtn"][prev];
        item.setAttribute("readonly", "readonly");
        modifyBtn.innerText = "수정";
      }
      if (this.prevModifiedItem === index) {
        let item = this.$refs["item"][index];
        let modifyBtn = this.$refs["modifyBtn"][index];
        item.setAttribute("readonly", "readonly");
        modifyBtn.innerText = "수정";
        this.list.splice(index, 1, item.value);
        console.log("수정완료");
        this.prevModifiedItem = null;
      } else {
        let item = this.$refs["item"][index];
        let modifyBtn = this.$refs["modifyBtn"][index];
        item.removeAttribute("readonly");
        modifyBtn.innerText = "완료";
        this.presentModifiedItem = index;
        this.prevModifiedItem = index;
      }
    }
  }
};
</script>

<style>
#app {
  width: 70%;
  min-height: 400px;
  text-align: center;
  background-color: beige;
  margin: auto;
}
ul {
  list-style: none;
}
li {
  width: 95%;
  background-color: rgba(255, 228, 196, 0.842);
  margin: 5px;
  display: flex;
}
.item {
  flex-grow: 1;
  text-align: center;
  border: none;
  background-color: none;
}
.item:focus {
  outline: none;
}
.item:read-only {
  background-color: blanchedalmond;
}
</style>
