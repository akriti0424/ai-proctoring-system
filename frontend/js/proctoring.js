const socket = new WebSocket("ws://127.0.0.1:8000/ws/proctor")

const video = document.getElementById("video")

const canvas = document.createElement("canvas")
const ctx = canvas.getContext("2d")

setInterval(()=>{

canvas.width = video.videoWidth
canvas.height = video.videoHeight

ctx.drawImage(video,0,0)

const frame = canvas.toDataURL("image/jpeg")

socket.send(frame)

console.log("Frame sent")

},2000)