# 🔇 SonicScope – Real-Time Audio Signal Visualizer & Editor

An interactive Python GUI app to record, analyze, and manipulate audio signals in real-time. Visualize signals in the **time and frequency domains**, apply **transformations**, and explore signal behavior using **FFT and waveform plots**.

## 🚀 Features

* 🔴 **Record** stereo audio (5 seconds) from your microphone
* ▶️ **Play** both input and output signals
* 📈 **Visualize** signals in:

  * Time domain
  * Frequency domain via FFT
* 📤 **Upload** and analyze external WAV files
* ⚙️ **Transform** your signal with:

  * Amplitude **scaling**
  * Time-domain **shifting**
* 🎛️ **Interactive Filter Menu** (under development):

  * High-Pass, Low-Pass, Band-Pass, Band-Stop
  * FIR and IIR filter designs
* 🧠 **Modular architecture** with centralized config and better separation of logic
* 🛠️ Built using **NiceGUI**, **NumPy**, **SciPy**, **Plotly**, and **PyDub**

## 🖼️ Demo

![Demo of the app in action](assets/demo.gif)

## 🐍 Python Version

Tested with **Python 3.10+**

## 📦 Requirements

* Python 3.10 or higher
* Install the dependencies listed in `requirements.txt`

## ▶️ Running the App

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rh8991/signal-processing-roadmap.git
   cd signal-processing-roadmap/SonicScope
   ```

2. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:

   ```bash
   python gui.py
   ```

4. **Open in your browser**:

   Visit [http://localhost:8080](http://localhost:8080) to use the web-based interface.

## 🌐 Static Web Demo

A lightweight front-end version is available in the `web` directory. Open `web/index.html` in a modern browser to record audio, visualize time and frequency domains, and play back recordings without running the Python server.

## 📂 File Structure

```bash
SonicScope/
├── assets/                # Audio files (input/output WAV)
│   ├── input.wav
│   └── output.wav
├── web/                   # Standalone web client
│   ├── index.html
│   └── app.js
├── config.py              # Central config and shared plots
├── gui.py                 # NiceGUI front-end layout
├── signal_tools.py        # Recording, playback, upload, plotting
├── signal_processing.py   # FFT, scaling, time-shifting, filters
├── requirements.txt       # Dependencies
└── README.md              # This file
```

## 📚 Lessons Learned

While building this project, I discovered key differences in how stereo audio is handled in NumPy arrays and SciPy WAV readers. Flattening stereo channels using `np.fromstring()` led to **incorrect playback speed** and signal length. The fix involved **selecting one audio channel (`data[:, 0]`)** and ensuring memory contiguity using `np.ascontiguousarray()`.

🧠 Want to understand this better? Read more in the [SciPy WAV documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html)

## 🔍 FFT & Domain Plots

The **FFT** feature computes the frequency spectrum of your signal and overlays it in the Frequency Domain tab. Plots are interactive and powered by **Plotly**, giving real-time signal feedback for deeper analysis.

## 🤝 Contributing

Contributions, ideas, and feedback are welcome!

* Feel free to fork the repo and submit a pull request
* Open an issue to suggest features or report bugs
* Star ⭐ the repo if you find it useful!

GitHub: [https://github.com/rh8991/signal-processing-roadmap](https://github.com/rh8991/signal-processing-roadmap)

## 📄 License

This project is licensed under the MIT License.
