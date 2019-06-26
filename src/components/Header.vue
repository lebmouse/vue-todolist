<template>
  <header>
    <div>Todo List</div>
    <div>{{listSize}}개의 할일이 있습니다.</div>
  </header>
</template>

<script>
export default {
  computed: {
    listSize() {
      return this.$store.state.list.length;
    }
  },
};
</script>

<style>
</style>


