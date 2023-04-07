import os
import torch.onnx 
import torchaudio
import nemo
import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp
import librosa
from omegaconf import OmegaConf
from nemo.collections.tts.models import FastPitchModel
from nemo.collections.tts.models import HifiGanModel
print(nemo.__version__)

conformer_transducer = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained(model_name="stt_en_conformer_transducer_medium")
conformer_transducer.save_to('Website/models/conformer_transducer.nemo')

punc_bert = nemo_nlp.models.PunctuationCapitalizationModel.from_pretrained(model_name="punctuation_en_distilbert")
punc_bert.save_to('Website/models/punc_bert.nemo')

spec_generator = FastPitchModel.from_pretrained("nvidia/tts_en_fastpitch")
spec_generator.save_to('Website/models/fastpitch.nemo')

hifigan = HifiGanModel.from_pretrained(model_name="nvidia/tts_hifigan")
hifigan.save_to('Website/models/hifigan.nemo')