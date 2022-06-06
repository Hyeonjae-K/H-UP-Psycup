<template>
  <div class="container">
    <!-- header -->
    <div align="center">
      <b-card no-body class="overflow-hidden mb-5" style="max-width: 540px;">
        <b-row no-gutters>
          <b-col md="6">
            <b-card-img :src="'http://127.0.0.1:8000' + items.thumbnail" alt="Image" class="rounded-0"></b-card-img>
          </b-col>
          <b-col md="6">
            <b-card-body :title="items.name">
              <b-card-text>
                {{ items.description }}
              </b-card-text>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>
    </div>
    <!-- section -->
    <div v-for="(item, index) in items.contents" :key="index">
      <!-- Question -->
      <!-- 질문에 이미지 있는 경우 -->
      <b-card v-if="item.image" :img-src="'http://127.0.0.1:8000' + item.image" img-left class="mb-3">
        <b-card-text>
          {{ index+1 }}.{{ item.question }}
        </b-card-text>
      </b-card>
      <!-- 질문에 이미지 없는 경우 -->
      <b-card v-else class="mb-3">
        <b-card-text>
          {{ index+1 }}.{{ item.question }}
        </b-card-text>
      </b-card>
      <!-- Answer -->
      <b-row>
        <b-col v-for="(answer, idx) in item.answers" :key="idx">
          <img class="col-12" :src="'127.0.0.1:8000' + answer.image" v-if="answer.image">
          <input type="radio" :id="`a${idx}${index}`"
            :name="`${index}${item.question}`"
            :value="answer.score"
            @click="checkState(`a${idx}${index}`, index)"
          />
          <label :for="`a${idx}${index}`">{{ answer.answer }}</label>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
import { fetchDetail } from '../api/index'

export default {
  data() {
    return {
      items: ''
    }
  },
  methods: {
    async fetchData(id) {
      const { data } = await fetchDetail(id);
      this.items = data;
      console.log(this.items);
    }
  },  
  created() {
    this.fetchData(this.$route.params.id);
  }
}
</script>