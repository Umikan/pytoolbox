const transcribe_clip = (blob) => {
    const server = document.querySelector("#server").value;
    const result = document.querySelector("#result");
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", `${server}apps/transcribe/clip/`, true);
    var data = new FormData();
    data.append('data', blob, 'audio_blob');
    xhttp.send(data);
    alert("クリップの文字起こしを行っています。");
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const data = JSON.parse(this.responseText);
            result.value = data['result'];
         }
    };
}

const recording = (stream) => {
    const record = document.querySelector("#record");
    const mic = document.querySelector("#mic");
    const player = document.querySelector('#player');
    const mediaRecorder = new MediaRecorder(stream);

    let mimeType = '';
    let chunks = [];

    mediaRecorder.ondataavailable = function (e) {
        mimeType = e.data.type;
        chunks.push(e.data);
    };
    mediaRecorder.onstop = function () {
        const blob = new Blob(chunks, {'type': mimeType});
        chunks = [];
        player.src = window.URL.createObjectURL(blob);
        transcribe_clip(blob);
    };

    record.onclick = () => {
        if (mic.style.color != 'red'){
            mediaRecorder.start();
            record.style.borderColor =  'red';
            mic.style.color = 'red';
        } else {
            mediaRecorder.stop();
            record.style.borderColor =  'black';
            mic.style.color = 'black';
        }
    };
}


if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    console.log("getUserMedia supported.");
    navigator.mediaDevices
      .getUserMedia({
          audio: true,
        }
      )
      .then(recording)
      .catch((err) => {
        console.error(`The following getUserMedia error occurred: ${err}`);
      });
} else {
    console.log("getUserMedia not supported on your browser!");
}


