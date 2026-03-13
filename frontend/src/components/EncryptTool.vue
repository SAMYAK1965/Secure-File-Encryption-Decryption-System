<template>

<div class="card p-4 shadow">

<div class="dropzone mb-3"
     @dragover.prevent
     @drop.prevent="handleDrop">

<h5>Drag Folder Here</h5>

<input
type="file"
webkitdirectory
multiple
class="form-control mt-3"
@change="handleSelect"
/>

</div>


<div v-if="selected.length">

<h5>Files in Folder</h5>

<ul class="list-group mb-3">

<li
v-for="(file,index) in selected"
:key="index"
class="list-group-item">

{{ file.webkitRelativePath || file.name }}

</li>

</ul>

</div>


<button
class="btn btn-primary mb-3"
@click="uploadFolder">

Encrypt Folder

</button>


<button
v-if="downloadReady"
class="btn btn-success"
@click="downloadZip">

Download Encrypted Folder

</button>

</div>

</template>


<script>

import axios from "axios"

export default{

data(){

return{

selected:[],
zipBlob:null,
downloadReady:false

}

},

methods:{


handleDrop(e){

this.selected = Array.from(e.dataTransfer.files)

},


handleSelect(e){

this.selected = Array.from(e.target.files)

},


async uploadFolder(){

const formData = new FormData()

for(let i=0;i<this.selected.length;i++){

formData.append("files",this.selected[i])

}

const res = await axios.post(
"http://localhost:5000/encrypt-folder",
formData,
{ responseType:"blob" }
)

this.zipBlob = res.data
this.downloadReady = true

},


downloadZip(){

const url = window.URL.createObjectURL(
new Blob([this.zipBlob])
)

const link = document.createElement("a")

link.href = url
link.download = "encrypted_folder.zip"

document.body.appendChild(link)

link.click()

link.remove()

}

}

}

</script>


<style>

.dropzone{

border:2px dashed #0d6efd;
padding:40px;
text-align:center;
border-radius:10px;
background:#f8f9fa;

}

</style>