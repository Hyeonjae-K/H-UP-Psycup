<template>
  <div>
    <b-card
      :title="item.name"
      :img-src="'http://127.0.0.1:8000' + item.thumbnail"
      img-alt="Thumbnail"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
    >
      <b-card-text>
        {{ item.description }}
        <br />
        <small>{{ item.create_date }}</small>
      </b-card-text>

      <b-button :href="`/detail/${item.id}`" variant="outline-primary">테스트 시작</b-button>
    </b-card>
  </div>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
}
</script>