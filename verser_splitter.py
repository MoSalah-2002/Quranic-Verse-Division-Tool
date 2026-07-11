# from downloader import download_audio
from quran import get_surah_with_out_search
from aligner import run_alignment
import librosa
import re
from bulider import extract_clean_words,build_final_ayahs,build_final_paths,save_ayah_audio_segments,audio_to_base64
import numpy as np
import os
import torch

def verses_split(audio_file,surah_name:str,ayah_start:int,ayah_end:int,addtion_part:float):
    
    # audio_path = download_audio(link)

    test_sampel,sr=librosa.load(audio_file,sr=16000)
    
    s_num,s_name,all_ayahs_arr=get_surah_with_out_search(surah_name)

    txt_res =" ".join(all_ayahs_arr[(ayah_start-1):(ayah_end)])
    txt_res = re.sub(r'[\u06D6-\u06ED]', '', txt_res)
    txt_res = re.sub(r"\s+", " ", txt_res)

    
    word_timestamps = run_alignment(
    audio=test_sampel,
    txt_res=txt_res)
    
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
    ayat_len=ayat_len,
    addtion_part=addtion_part)
    aya_id=np.arange(ayah_start,ayah_end+1)
    
    final_final_arr = build_final_paths(
    aya_id=aya_id,
    final_arr=final_arr,
    s_num=s_num)

    output_dir = save_ayah_audio_segments(
        final_final_res=final_final_arr,
        audio_signal=test_sampel,
        sample_rate=16000,
        output_dir=f"output/سورة {s_name}"
    )
    all_verses=[i for i,t in final_arr]
    files = sorted(os.listdir(output_dir))
    base64_audios=[audio_to_base64(os.path.join(f"output/سورة {s_name}",f)) for f in files]
    final_all_verses={"verses":[]}
    for v,p,f_name in zip(all_verses,base64_audios,files):
        final_all_verses['verses'].append({"text":v,"audio_base64":p,"path_name":f_name})

    return final_all_verses