<template>
  <section>
    <ul>
      <li v-for="(item,index) in list" :key="index">
        <input
          class="item"
          ref="item"
          readonly
          type="text"
          @keyup.enter="modifyItem(index)"
          :value="item"
        >
        <!-- <button ref="modifyBtn" @click="modifyItem(index)">수정</button> -->
        <button @click="removeItem(index)">제거</button>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  data() {
    return {
      valueToModify: "",
      prevModifiedItem: null,
      presentModifiedItem: null
    };
  },
  computed: {
    list() {
      return this.$store.state.list;
    }
  },
  methods: {
    removeItem(index) {
      this.$store.commit("spliceItem", index);
    },
    modifyItem(index) {
      let prev = this.prevModifiedItem;
      // 다른 아이템을 원래되로 되돌리기.
      if (prev !== null) {
        let item = this.$refs["item"][prev];
        let modifyBtn = this.$refs["modifyBtn"][prev];
        item.setAttribute("readonly", "readonly");
        modifyBtn.innerText = "수정";
      }
      // 수정완료되어 다시 원래되로 되돌리기.
      // 아니면 수정하기 위해 만들기.
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
        item.focus();
        modifyBtn.innerText = "완료";
        this.presentModifiedItem = index;
        this.prevModifiedItem = index;
      }
    }
  }
};
</script>

<style>
</style>
