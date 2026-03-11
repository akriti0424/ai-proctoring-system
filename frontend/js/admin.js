const socket = new WebSocket("ws://127.0.0.1:8000/ws/admin")

const img = document.getElementById("live")

socket.onmessage = function(event){

img.src = event.data

}