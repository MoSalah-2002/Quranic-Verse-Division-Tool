
import re
import numpy as np
from quran import get_surah_with_out_search
from aligner import run_alignment
import os
import soundfile as sf
import base64

def extract_clean_words(word_timestamps):
    res_txt = []
    times_stamps = []

    for r in word_timestamps:
        start = r["start"]
        end = r["end"]
        text = r["text"]

        # remove Arabic tashkeel (diacritics)
        text_without_tashkeel = re.sub(r'[\u06D6-\u06ED]', '', text)

        if text_without_tashkeel != "":
            res_txt.append(text_without_tashkeel)
            times_stamps.append((start, end))

    return res_txt, times_stamps


def build_final_ayahs(res_txt, times_stamps, ayat_len2, ayat_len,addtion_part=0.2):
    final_arr = []
    c1 = 0
    c2 = 0

    for i in range(len(ayat_len2)):

        ayah_arr = res_txt[ayat_len2[c1]:ayat_len[c2]]

        if ayah_arr:
            ayah_time_arr = times_stamps[ayat_len2[c1]:ayat_len[c2]]

            # # start time
            # if c1 > 0 and final_arr:
            #     start_ayah = final_arr[-1][1][-1]
            # else:
            #     start_ayah = ayah_time_arr[0][0]
            
            start_ayah = ayah_time_arr[0][0]

            # end time
            end_ayah = ayah_time_arr[-1][1] + addtion_part

            ayah_time = (start_ayah, end_ayah)

            final_arr.append((
                " ".join(ayah_arr).strip(),
                ayah_time
            ))

        c1 += 1
        if i != len(ayat_len2) - 2:
            c2 += 1

    return final_arr



def build_final_paths(aya_id, final_arr, s_num):
    final_final_arr = []

    for t_idx,idx in  enumerate(aya_id):
        final_path = str(s_num).zfill(3) + str(idx).zfill(3)

        # safer access (idx is 1-based in your code)
        time = final_arr[t_idx][1]

        final_final_arr.append((final_path, time))

    return final_final_arr


def local_verses_split(audio_path,surah_name,ayah_start,ayah_end):

    s_num,s_name,all_ayahs_arr=get_surah_with_out_search(surah_name)
    txt_res =" ".join(all_ayahs_arr[(ayah_start-1):(ayah_end)])
    txt_res = re.sub(r'[\u06D6-\u06ED]', '', txt_res)
    txt_res = re.sub(r"\s+", " ", txt_res)


    word_timestamps = run_alignment(
    audio_path=audio_path
    ,txt_res=txt_res)

    res_txt, times_stamps = extract_clean_words(word_timestamps)

    ayat_len=[]
    for ayah in all_ayahs_arr[(ayah_start-1):ayah_end]:
        ayah = re.sub(r'[\u06D6-\u06ED]', '', ayah)
        ayah = re.sub(r"\s+", " ", ayah)
        ayat_len.append(len(ayah.split()))
    ayat_len=np.array(ayat_len).cumsum()
    ayat_len2=ayat_len.copy()
    ayat_len2 = np.insert(ayat_len2, 0, 0)

    final_arr = build_final_ayahs(
    res_txt=res_txt,
    times_stamps=times_stamps,
    ayat_len2=ayat_len2,
    ayat_len=ayat_len)
    aya_id=np.arange(ayah_start,ayah_end+1)

    # final_final_arr = build_final_paths(
    # aya_id=aya_id,
    # final_arr=final_arr,
    # s_num=s_num)

    return{"الايات":final_arr}

def save_ayah_audio_segments(final_final_res, audio_signal, sample_rate=16000, output_dir="./output"):
    os.makedirs(output_dir, exist_ok=True)
    for item in final_final_res:
        path = item[0]
        start_time, end_time = item[1]

        start_sig = int(start_time * sample_rate)
        end_sig = int(end_time * sample_rate)

        signal = audio_signal[start_sig:end_sig]

        output_path = os.path.join(output_dir, f"{path}.wav")

        sf.write(output_path, signal, sample_rate)

    return output_dir

def audio_to_base64(file_path: str) -> str:
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
        return base64.b64encode(audio_bytes).decode("utf-8")
