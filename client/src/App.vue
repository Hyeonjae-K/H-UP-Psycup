<template>
  <div id="app">
    <TestNavbar />
    <div>
      <RouterView />
    </div>
  </div>
</template>

<script>
import TestNavbar from './components/TestNavbar.vue'

export default {
  name: 'App',
  components: {
    TestNavbar,
  }
}
</script>
