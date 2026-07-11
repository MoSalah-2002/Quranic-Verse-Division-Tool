# 📖 Quranic Verse Division Tool

A Streamlit-based application that automatically divides Quran recitation audio into individual verse (Ayah) audio segments using speech alignment techniques.

The tool helps users extract accurate audio clips for specific Quran verses, edit segments, and export the results for further use.

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

1. Enter a Quran recitation YouTube link
2. Select the Surah name
3. Choose starting and ending Ayah numbers
4. Run the processing pipeline
5. Review and edit generated audio segments
6. Download the final audio package

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

* Add more reciters
* Improve alignment accuracy
* Support more audio sources
* Add cloud storage support
* Improve mobile compatibility

## 👨‍💻 Author

Mohmed Salah

---

⭐ If you find this project useful, consider giving it a star on GitHub.
