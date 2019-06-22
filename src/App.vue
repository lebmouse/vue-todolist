<template>
  <div id="app">
    <Header></Header>
    <InputBar></InputBar>
    <List></List>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import InputBar from "./components/InputBar.vue";
import List from "./components/List.vue";

export default {
  name: "app",
  components: {
    Header,
    InputBar,
    List
  },
  created() {
    this.$store.dispatch("asynSetList");
  },
  mounted() {
    this.$store.watch(
      () => this.$store.getters.getList,
      todos => localStorage.setItem("todoList", JSON.stringify(todos))
    );
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
