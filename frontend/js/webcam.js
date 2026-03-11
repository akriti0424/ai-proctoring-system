const video = document.getElementById("video")

navigator.mediaDevices.getUserMedia({video:true})
.then(stream=>{
video.srcObject = stream
})

const canvas = document.createElement("canvas")
const ctx = canvas.getContext("2d")

setInterval(()=>{

canvas.width = video.videoWidth
canvas.height = video.videoHeight

ctx.drawImage(video,0,0)

let frame = canvas.toDataURL("image/jpeg")

fetch("/api/frame",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({image:frame})
})

},500)