import os
import torch.onnx 
import torchaudio
import nemo
import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp
import librosa
from omegaconf import OmegaConf
print(nemo.__version__)

conformer_transducer = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained(model_name="stt_en_conformer_transducer_medium")
conformer_transducer.save_to('Website/models/conformer_transducer.nemo')

punc_bert = nemo_nlp.models.PunctuationCapitalizationModel.from_pretrained(model_name="punctuation_en_distilbert")
punc_bert.save_to('Website/models/punc_bert.nemo')