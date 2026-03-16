<template>

<div class="card p-4 shadow mt-4">

<h4 class="mb-3">🔓 Decrypt Folder</h4>

<div class="mb-3">

<label class="form-label">Upload Encrypted ZIP</label>

<input
type="file"
accept=".zip"
class="form-control"
@change="handleSelect"
/>

</div>


<button
class="btn btn-warning mb-3"
@click="uploadZip"
:disabled="!selectedFile"
>

Decrypt Folder

</button>


<button
v-if="downloadReady"
class="btn btn-success"
@click="downloadZip"
>

Download Decrypted Folder

</button>

</div>

</template>



<script>

import axios from "axios"

export default {

data() {

return {

selectedFile: null,
zipBlob: null,
downloadReady: false

}

},

methods: {

handleSelect(e) {

this.selectedFile = e.target.files[0] || null
this.downloadReady = false

},

async uploadZip() {

if (!this.selectedFile) {

alert("Please select an encrypted ZIP file first")
return

}

const formData = new FormData()
formData.append("file", this.selectedFile)

try {

const res = await axios.post(

"https://secure-file-encryption-decryption-system.onrender.com/decrypt-folder",

formData,

{
responseType: "blob",
headers: {
"Content-Type": "multipart/form-data"
}
}

)

this.zipBlob = res.data
this.downloadReady = true

} catch (error) {

console.error(error)
alert("Decryption failed. Please check backend server.")

}

},

downloadZip() {

const url = window.URL.createObjectURL(

new Blob([this.zipBlob])

)

const link = document.createElement("a")

link.href = url
link.download = "decrypted_folder.zip"

document.body.appendChild(link)

link.click()

link.remove()

}

}

}

</script>
