const recordBtn = document.getElementById('record');
const stopBtn = document.getElementById('stop');
const playBtn = document.getElementById('play');
const player = document.getElementById('player');
const waveformCanvas = document.getElementById('waveform');
const freqCanvas = document.getElementById('frequency');
const waveCtx = waveformCanvas.getContext('2d');
const freqCtx = freqCanvas.getContext('2d');

let mediaRecorder;
let audioChunks = [];
let analyser;
let dataArray;
let freqArray;
let animationId;
let audioCtx;
let source;

function draw() {
    waveCtx.clearRect(0, 0, waveformCanvas.width, waveformCanvas.height);
    freqCtx.clearRect(0, 0, freqCanvas.width, freqCanvas.height);

    analyser.getByteTimeDomainData(dataArray);
    analyser.getByteFrequencyData(freqArray);

    waveCtx.beginPath();
    for (let i = 0; i < dataArray.length; i++) {
        const x = (i / dataArray.length) * waveformCanvas.width;
        const y = (dataArray[i] / 255.0) * waveformCanvas.height;
        if (i === 0) waveCtx.moveTo(x, y);
        else waveCtx.lineTo(x, y);
    }
    waveCtx.stroke();

    const barWidth = freqCanvas.width / freqArray.length;
    for (let i = 0; i < freqArray.length; i++) {
        const barHeight = freqArray[i] / 255.0 * freqCanvas.height;
        freqCtx.fillRect(i * barWidth, freqCanvas.height - barHeight, barWidth, barHeight);
    }

    animationId = requestAnimationFrame(draw);
}

recordBtn.onclick = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    audioCtx = new AudioContext();
    source = audioCtx.createMediaStreamSource(stream);
    analyser = audioCtx.createAnalyser();
    source.connect(analyser);
    analyser.fftSize = 2048;
    const bufferLength = analyser.frequencyBinCount;
    dataArray = new Uint8Array(bufferLength);
    freqArray = new Uint8Array(bufferLength);

    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.ondataavailable = e => audioChunks.push(e.data);
    mediaRecorder.onstop = () => {
        const blob = new Blob(audioChunks, { type: 'audio/webm' });
        audioChunks = [];
        player.src = URL.createObjectURL(blob);
        playBtn.disabled = false;
    };
    mediaRecorder.start();
    draw();
    recordBtn.disabled = true;
    stopBtn.disabled = false;
};

stopBtn.onclick = () => {
    mediaRecorder.stop();
    cancelAnimationFrame(animationId);
    audioCtx && audioCtx.close();
    recordBtn.disabled = false;
    stopBtn.disabled = true;
};

playBtn.onclick = () => {
    player.play();
};
