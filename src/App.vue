<template>
  <div id="app">
    <header>Todo List</header>
    <section class="input">
      <!-- 1. v-model -->
      <!-- 2. v-on -->
      <input type="text" name id v-model="value" @keyup.enter="addItem">
      <button @click="addItem">제출</button>
    </section>
    <section>
      <ol>
        <!-- 3. v-for, v-bind:key -->
        <li v-for="(item,index) in list" :key="index">{{item}}</li>
      </ol>
    </section>
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      // 4. Vue data
      value: "",
      list: []
    };
  },
  // 5. methods
  methods: {
    addItem() {
      this.list.push(this.value);
    }
  }
};
</script>

<style>
</style>
