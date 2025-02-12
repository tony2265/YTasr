from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from ailabs_asr.streaming import StreamingClient



def on_processing_sentence(message):
  print(f'hello: {message["asr_sentence"]}')

def on_final_sentence(message):
  print(f'world: {message["asr_sentence"]}')


asr_client = StreamingClient('api-key-applied-from-devconsole')
asr_client.start_streaming_wav(
  pipeline='asr-zh-en-std',
  # verbose=True,
  file='voice.wav')