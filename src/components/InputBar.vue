<template>
  <section class="input">
    <input type="text" v-model="value" @keyup.enter="addItem">
    <button @click="addItem">제출</button>
  </section>
</template>

<script>
export default {
  data() {
    return {
      value: ""
    };
  },
  methods: {
    addItem() {
      if (this.value) {
        // this.$store.commit("pushList", this.value);
        let obj = {body : this.value}
        this.$store.dispatch("asyncPushList", obj);
        this.value = "";
      }
    }
  }
};
</script>

<style>
</style>
