
import torch

from ctc_forced_aligner import (
    load_audio,
    load_alignment_model,
    generate_emissions,
    preprocess_text,
    get_alignments,
    get_spans,
    postprocess_results,
)

language = "iso" 
device = "cuda" 

alignment_model, alignment_tokenizer = load_alignment_model(
    device,
    dtype=torch.float16,
)

def run_alignment(
    audio,
    txt_res,
    alignment_model=alignment_model,
    alignment_tokenizer=alignment_tokenizer,
    language=language):
    # 1. Load audio
    # audio_waveform = load_audio(
    #     audio_path,
    #     alignment_model.dtype,
    #     alignment_model.device
    # )
    audio_waveform = torch.from_numpy(audio)

    audio_waveform = audio_waveform.to(
        device=alignment_model.device,
        dtype=alignment_model.dtype
    )

    # 2. Generate emissions
    emissions, stride = generate_emissions(
        alignment_model,
        audio_waveform
    )

    # 3. Preprocess text
    tokens_starred, text_starred = preprocess_text(
        txt_res,
        romanize=True,
        language=language,
    )

    # 4. Get alignments
    segments, scores, blank_token = get_alignments(
        emissions,
        tokens_starred,
        alignment_tokenizer,
    )

    # 5. Get spans
    spans = get_spans(
        tokens_starred,
        segments,
        blank_token
    )

    # 6. Post-process results
    word_timestamps = postprocess_results(
        text_starred,
        spans,
        stride,
        scores
    )

    return word_timestamps


