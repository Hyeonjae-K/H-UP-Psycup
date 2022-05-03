<template>
  <div class="container mt-4" >
    <ul>
      <test-card 
      v-for="item in items" 
      :key="item.id"
      :item="item"
      ></test-card>
    </ul>
  </div>
</template>

<script>
import { fetchTestList } from '../api/index'
import TestCard from '../components/TestCard.vue'

export default {
  components: {
    TestCard,
  },
  data() {
    return {
      items:'',
    }
  },
  methods: {
    async fetchData() {
      const { data } = await fetchTestList();
      this.items = data;
      console.log(this.items);
    },
  },
  created() {
    this.fetchData();
  },
}
</script>