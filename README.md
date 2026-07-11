# 📖 Quranic Verse Division Tool

an AI-powered application that automatically divides Quran recitation audio into individual verse segments. The tool uses audio processing and alignment techniques to detect verse timestamps, extract separate audio clips, and provide an interactive editor for refining the segments. It helps users create accurate, organized Quran verse audio files efficiently.

## ✨ Features

* 🎧 Download Quran recitation audio from YouTube
* 📖 Select Surah and Ayah range
* 🧠 Automatic verse-to-audio alignment
* ✂️ Split recitation into individual Ayah audio files
* 🔊 Preview generated audio segments
* 🎚️ Edit audio regions before saving
* 📦 Export verses as a ZIP file
* 📝 Display Quran verses with generated audio

## 🖼️ Application Workflow

1. Enter a Quran recitation Audio file
2. Select the Surah name
3. Choose starting and ending Ayah numbers
4. Run the processing pipeline
5. Review and edit generated audio segments
6. Download the final audio zip file

## 🛠️ Technologies Used

* Python
* Streamlit
* Librosa
* Pandas
* NumPy
* Audio processing libraries
* Speech alignment techniques
* WaveSurfer.js (audio editing interface)

## 📂 Project Structure

```
Quran-Verse-Division-Tool/
│
├── app.py                 # Streamlit application
├── verser_splitter.py     # Main verse splitting pipeline
├── downloader.py          # Audio downloading utilities
├── aligner.py             # Audio-text alignment
├── quran.py               # Quran data handling
├── builder.py             # Audio segment generation
│
├── data/
│   └── The Quran Dataset.csv
│
├── requirements.txt       # Python dependencies
│
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Quran-Verse-Division-Tool.git

cd Quran-Verse-Division-Tool
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 📦 Output

The application generates:

* Individual Ayah audio files
* Edited audio segments
* ZIP archive containing processed verses

## 🚀 Deployment

The application can be deployed using:

* Hugging Face Spaces
* Streamlit Community Cloud
* Docker
* Other cloud platforms

## 📌 Future Improvements

* Improve alignment accuracy
* Support more audio sources
* Add cloud storage support
* Make the surah detect automatically
* Automatic detection of the surah boundaries in the file
* Support for multiple surahs

## 👨‍💻 Author

Mohmed Salah (Mo salah)

---

⭐ If you find this project useful, consider giving it a star on GitHub.
