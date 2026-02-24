navigator.mediaDevices.getUserMedia({video: true })
   .then(stream => {
     document.getElementById("video").srcObject = stream;
   })
   .catch(err => console.error("Camera error", err));

   document.addEventListener("visibilitychange", () =>{
    if(document.hidden){
        console.log("Tab switched - possible violation")
    }
   });