<template>
  <div class="container mt-5">

    <h1 class="text-center">🔐 Folder Encryption Tool</h1>

    <EncryptTool />

    <DecryptTool />

  </div>
</template>

<script>
import EncryptTool from "./components/EncryptTool.vue"
import DecryptTool from "./components/DecryptTool.vue"

export default {
  components: {
    EncryptTool,
    DecryptTool
  }
}
</script>