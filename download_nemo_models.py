import nemo.collections.asr as nemo_asr
from nemo.collections.nlp.models import PunctuationCapitalizationLexicalAudioModel

# to get the list of pre-trained models
print(PunctuationCapitalizationLexicalAudioModel.list_available_models())
