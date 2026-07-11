

import streamlit.components.v1 as components
import json
from verser_splitter import verses_split





import os
import streamlit.components.v1 as components





import pandas as pd

df=pd.read_csv("data/The Quran Dataset.csv")
all_surah_ayas=df.groupby("surah_no")

quran_surahs = {
    1: "الفاتحة", 2: "البقرة", 3: "آل عمران", 4: "النساء", 5: "المائدة",
    6: "الأنعام", 7: "الأعراف", 8: "الأنفال", 9: "التوبة", 10: "يونس",
    11: "هود", 12: "يوسف", 13: "الرعد", 14: "إبراهـيم", 15: "الحجر",
    16: "النحل", 17: "الإسراء", 18: "الكهف", 19: "مريم", 20: "طه",
    21: "الأنبياء", 22: "الحج", 23: "المؤمنون", 24: "النور", 25: "الفرقان",
    26: "الشعراء", 27: "النمل", 28: "القصص", 29: "العنكبوت", 30: "الروم",
    31: "لقمان", 32: "السجدة", 33: "الأحزاب", 34: "سبأ", 35: "فاطر",
    36: "يس", 37: "الصافات", 38: "ص", 39: "الزمر", 40: "غافر",
    41: "فصلت", 42: "الشورى", 43: "الزخرف", 44: "الدخان", 45: "الجاثية",
    46: "الأحقاف", 47: "محمد", 48: "الفتح", 49: "الحجرات", 50: "ق",
    51: "الذاريات", 52: "الطور", 53: "النجم", 54: "القمر", 55: "الرحمن",
    56: "الواقعة", 57: "الحديد", 58: "المجادلة", 59: "الحشر", 60: "الممتحنة",
    61: "الصف", 62: "الجمعة", 63: "المنافقون", 64: "التغابن", 65: "الطلاق",
    66: "التحريم", 67: "الملك", 68: "القلم", 69: "الحاقة", 70: "المعارج",
    71: "نوح", 72: "الجن", 73: "المزمل", 74: "المدثر", 75: "القيامة",
    76: "الإنسان", 77: "المرسلات", 78: "النبأ", 79: "النازعات", 80: "عبس",
    81: "التكوير", 82: "الإنفطار", 83: "المطففين", 84: "الانشقاق", 85: "البروج",
    86: "الطارق", 87: "الأعلى", 88: "الغاشية", 89: "الفجر", 90: "البلد",
    91: "الشمس", 92: "الليل", 93: "الضحى", 94: "الشرح", 95: "التين",
    96: "العلق", 97: "القدر", 98: "البينة", 99: "الزلزلة", 100: "العاديات",
    101: "القارعة", 102: "التكاثر", 103: "العصر", 104: "الهمزة", 105: "الفيل",
    106: "قريش", 107: "الماعون", 108: "الكوثر", 109: "الكافرون", 110: "النصر",
    111: "المسد", 112: "الإخلاص", 113: "الفلق", 114: "الناس"
}

quran_surahs2={}
for k,v in quran_surahs.items():
  quran_surahs2[v]=k

def get_surah_ayahs_len(s_name):
    s_num=quran_surahs2[s_name]
    surah_ayas=all_surah_ayas.get_group(s_num)
    all_ayahs_arr=surah_ayas['ayah_ar'].values
    all_ayahs_arr[0]=all_ayahs_arr[0].replace("بسم الله الرحمن الرحيم","")
    all_ayahs_arr[0]=all_ayahs_arr[0].replace("بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ","")
    return len(all_ayahs_arr)




def wavesurfer_app(verses,verses_text,paths,surah_name):

    verses_json = json.dumps(verses)
    text_json = json.dumps(verses_text)
    path_json = json.dumps(paths)
    
    html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<script src="https://unpkg.com/wavesurfer.js"></script>

<script src="https://unpkg.com/wavesurfer.js@7/dist/plugins/regions.min.js"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/lamejs/1.2.0/lame.min.js"></script>

<style>

body{{
    font-family:Arial;
}}

.wave{{
    margin-bottom:30px;
}}

button{{
    margin:5px;
}}

</style>



<style>

@import url('https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Amiri:ital,wght@0,400;0,700;1,400;1,700&display=swap');


.verse-title {{
    font-family: 'Amiri Quran', serif;
    font-size: 24px;
    direction: rtl;
    text-align: center;
    line-height: 2.2;
}}


</style>

</head>

<body>

<div id="container"></div>

<hr>

<button onclick="saveAll()">

💾 الحفظ و تنزيل الملف المضغوط

</button>

<script>

const verses = {verses_json};

const verseTitles = {text_json};

const verse_paths = {path_json};

const allRegions = {{}};

const waves = [];

const container =
document.getElementById("container");



verses.forEach((v,index)=>{{

    const verseId = index + 1;
    const verseName = verseTitles[index];

    const div = document.createElement("div");

    div.className="wave";

    div.innerHTML=`

        <h3 class="verse-title"> ${{verseName}}</h3>

        <div id="wave_${{verseId}}"></div>

        <button id="play_${{verseId}}">
        ▶ / ⏸
        </button>

        <p>

         البداية :

        <span id="start_${{verseId}}">

        0

        </span>

        &nbsp;&nbsp;

         النهاية :

        <span id="end_${{verseId}}">

        0

        </span>

        </p>

    `;

    container.appendChild(div);



    const regions =
    WaveSurfer.Regions.create();



    const ws =
    WaveSurfer.create({{

        container:"#wave_"+verseId,

        height:120,

        waveColor:"#999",

        progressColor:"#444",

        url:
        "data:audio/mp3;base64,"+
        v.audio_base64,

        plugins:[regions]

    }});



    waves.push(ws);



    ws.on("ready",()=>{{



        const region =
        regions.addRegion({{

            start:0,

            end:ws.getDuration(),

            drag:true,

            resize:true

        }});



        function update(){{

            document.getElementById(

                "start_"+verseId

            ).innerHTML=

            region.start.toFixed(3);



            document.getElementById(

                "end_"+verseId

            ).innerHTML=

            region.end.toFixed(3);



            allRegions[verseId]={{

                start:region.start,

                end:region.end,

                audio:v.audio_base64

            }};

        }}



        update();



        region.on(

            "update-end",

            update

        );



        document.getElementById(

            "play_"+verseId

        ).onclick=()=>{{

            ws.playPause();

        }};



    }});



}});


function audioBufferToWav(buffer){{

    const numOfChan = buffer.numberOfChannels;

    const length =
        buffer.length * numOfChan * 2 + 44;


    const bufferArray =
        new ArrayBuffer(length);


    const view =
        new DataView(bufferArray);


    let offset = 0;


    function writeString(str){{

        for(let i=0;i<str.length;i++){{

            view.setUint8(
                offset++,
                str.charCodeAt(i)
            );

        }}

    }}


    writeString("RIFF");

    view.setUint32(
        offset,
        36 + buffer.length*numOfChan*2,
        true
    );

    offset +=4;


    writeString("WAVE");

    writeString("fmt ");


    view.setUint32(
        offset,
        16,
        true
    );

    offset +=4;


    view.setUint16(
        offset,
        1,
        true
    );

    offset +=2;


    view.setUint16(
        offset,
        numOfChan,
        true
    );

    offset +=2;


    view.setUint32(
        offset,
        buffer.sampleRate,
        true
    );

    offset +=4;


    view.setUint32(
        offset,
        buffer.sampleRate*numOfChan*2,
        true
    );

    offset +=4;


    view.setUint16(
        offset,
        numOfChan*2,
        true
    );

    offset +=2;


    view.setUint16(
        offset,
        16,
        true
    );

    offset +=2;


    writeString("data");


    view.setUint32(
        offset,
        buffer.length*numOfChan*2,
        true
    );

    offset +=4;



    const channels=[];

    for(
        let i=0;
        i<numOfChan;
        i++
    )
        channels.push(
            buffer.getChannelData(i)
        );


    let pos=44;


    for(
        let i=0;
        i<buffer.length;
        i++
    ){{

        for(
            let ch=0;
            ch<numOfChan;
            ch++
        ){{

            let sample =
            Math.max(
                -1,
                Math.min(
                    1,
                    channels[ch][i]
                )
            );


            view.setInt16(
                pos,
                sample<0 ?
                sample*0x8000 :
                sample*0x7FFF,
                true
            );

            pos +=2;

        }}
    }}


    return new Blob(
        [view],
        {{
            type:"audio/wav"
        }}
    );

}}


async function saveAll(){{

    const zip = new JSZip();

    for (const [id, data] of Object.entries(allRegions)){{

        const title = verse_paths[id-1];

        const audioBlob = await fetch(
            "data:audio/mp3;base64," + data.audio
        ).then(r => r.blob());


        const arrayBuffer =
            await audioBlob.arrayBuffer();


        const audioContext =
            new AudioContext();


        const audioBuffer =
            await audioContext.decodeAudioData(arrayBuffer);



        const startSample =
            Math.floor(
                data.start * audioBuffer.sampleRate
            );


        const endSample =
            Math.floor(
                data.end * audioBuffer.sampleRate
            );


        const length =
            endSample - startSample;



        const offline =
            new OfflineAudioContext(
                audioBuffer.numberOfChannels,
                length,
                audioBuffer.sampleRate
            );


        const source =
            offline.createBufferSource();


        const newBuffer =
            offline.createBuffer(
                audioBuffer.numberOfChannels,
                length,
                audioBuffer.sampleRate
            );


        for(
            let ch=0;
            ch<audioBuffer.numberOfChannels;
            ch++
        ){{

            newBuffer
            .copyToChannel(
                audioBuffer
                .getChannelData(ch)
                .slice(startSample,endSample),
                ch
            );

        }}


        source.buffer = newBuffer;

        source.connect(
            offline.destination
        );

        source.start();


        const rendered =
            await offline.startRendering();



        // convert WAV

        const wav =
            audioBufferToWav(rendered);



        zip.file(
            title + ".wav",
            wav
        );

    }}


    const content =
        await zip.generateAsync({{
            type:"blob"
        }});


    const link =
        document.createElement("a");


    link.href =
        URL.createObjectURL(content);


    link.download =
        "{surah_name}.zip";


    link.click();


    alert("تم إنشاء الملف المضغوط بنجاح");

}}
</script>

</body>

</html>

"""

    return html


import streamlit as st
import requests
import base64
import io
import zipfile
from pydub import AudioSegment



st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Amiri:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">

<style>

html, body, [class*="css"] {
    font-family: 'Amiri', sans-serif;
}
/* Checkbox text */
[data-testid="stCheckbox"] p {
    font-family: "Amiri";
    font-size: 16px;
    direction: rtl;
}

</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
input[type="number"] {
    pointer-events: none;
}
</style>
""", unsafe_allow_html=True)



import json



st.set_page_config(page_title="📖 اداة تقسيم ايات القران الكريم 📖", layout="centered")

# st.title("📖 اداة تقسيم ايات القران الكريم 📖")
st.markdown("""
<h2 style="
    font-family:'Amiri', serif;
    direction:rtl;
    text-align:center;
    color:#C9A227;
">
📖 اداة تقسيم ايات القران الكريم 📖
</h2>
""", unsafe_allow_html=True)

# -----------------------
# Inputs
# -----------------------


# link = st.text_input("فضلا ضع رابط التلاوة")
audio_file = st.file_uploader(
    "فضلا قم برفع ملف التلاوة",
    type=["mp3", "wav", "ogg", "flac", "m4a", "aac"],
    accept_multiple_files=False
)

text = """
ℹ️ <b>يرجى التأكد من النقاط التالية قبل رفع ملف التلاوة</b><br><br>

📖 تأكد أن الملف المرفوع هو <b>تلاوة للقرآن الكريم</b><br><br>

🕌 تأكد أن <b>السورة المقروءة</b> في الملف الصوتي هي <b>السورة المختارة بالأسفل</b><br><br>

🔢 تأكد أن التلاوة <b>تبدأ من رقم الآية</b> الذي أدخلته في خانة 
<b>"التلاوة تبدأ من"</b>، وتنتهي عند <b>رقم الآية</b> الذي أدخلته في خانة 
<b>"التلاوة تنتهي عند"</b>.<br><br>

🕌 تأكد أن التلاوة تحتوي على <b>سورة واحدة فقط</b>،
وهي السورة التي قمت باختيارها في خانة <b>"السورة"</b> بالأسفل<br><br>

🚫 تأكد أن التلاوة <b>ليست من صلاة التراويح</b><br>

⚠️ إذا كانت كذلك، فيرجى قص <b>التكبير، وسورة الفاتحة، والركوع، والسجود</b> يدويًا، ثم رفع الملف بعد ذلك<br><br>

📄 تأكد أن التلاوة <b>لا تبدأ بسورة الفاتحة ثم السورة المختارة</b>،
حيث يُسمح برفع <b>سورة واحدة فقط</b>
"""

st.markdown(f"""
<div style="
    background-color:#F5F5DC;
    border-right:6px solid #C9A227;
    padding:28px;
    width:765px;
    border-radius:15px;
    font-family:'Amiri', 'Noto Naskh Arabic', serif;
    font-size:16px;
    margin-bottom:15;
    line-height:1;
    direction:rtl;
    text-align:right;
    padding-right: 8px;
    margin-left:0px;
">
{text}
</div>
""", unsafe_allow_html=True)

surah_name = st.selectbox("إختر السورة", list(quran_surahs.values()))

surah_len=get_surah_ayahs_len(surah_name)



ayah_start = st.number_input("التلاوة تبدأ من الاية", min_value=1, value=1,max_value=surah_len-1)
ayah_end = st.number_input("تنتهي التلاوة عند الاية", min_value=ayah_start+1, value=surah_len,max_value=surah_len)

is_tartil = st.checkbox("هل التلاوة ترتيل ؟" ,  value=True)

addtion_part=0
if is_tartil:
    addtion_part=0.5
else:
    addtion_part=1
# -----------------------
# Helper
# -----------------------
def play_audio_base64(b64_audio):
    audio_bytes = base64.b64decode(b64_audio)
    st.audio(audio_bytes, format="audio/mp3")

# -----------------------

import shutil

if st.button("تقسيم الايات "):

    if audio_file is None:
      st.warning("⚠️ قم برفع التلاوة اولا")
      st.stop()
    parent_folder = "output"

    for item in os.listdir(parent_folder):
        item_path = os.path.join(parent_folder, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)

    payload = {
        "audio_file": audio_file,
        "surah_name": surah_name,
        "ayah_start": int(ayah_start),
        "ayah_end": int(ayah_end),
        "addtion_part":float(addtion_part)
    }
    try:
      with st.spinner("تتم المعالجة..."):
          data = verses_split(**payload)
          verses = data["verses"]
          
          verse_texts = [v["text"] for v in verses]
          path_names = [p["path_name"] for p in verses]

          components.html(
              wavesurfer_app(verses,verse_texts,path_names,"سورة "+str(surah_name)),
              height=3000,
              scrolling=True)
        
          st.success(f"تمت المعالجة بنجاح ✅")
    except:
      st.error(f"❌ حدث خطأ ما تأكد من التعلميات بالأعلى و و قم بأعادة المحاولة")
