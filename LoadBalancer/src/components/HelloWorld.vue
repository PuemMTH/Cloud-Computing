<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      <!-- จะบอกประมาณว่า project นี้ สร้างโดย ใครบ้าง -->
      This project was created with
      <a href="https://vitejs.dev/" target="_blank" rel="noopener" v-pre>
        ธนภัทร เอี่ยมอาจ
      </a>
      and
      <a href="https://v3.vuejs.org/" target="_blank" rel="noopener" v-pre>
        พัชรพล เลารุจิราลัย
      </a>
    </h3>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
