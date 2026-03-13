<template>
  <div class="container mt-5">

    <h1 class="text-center">🔐 Folder Encryption Tool</h1>

    <EncryptTool />

  </div>
</template>

<script>
import EncryptTool from "./components/EncryptTool.vue"

export default {
  components: {
    EncryptTool
  }
}
</script>