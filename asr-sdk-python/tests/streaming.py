from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from ailabs_asr.streaming import StreamingClient
import os
os.environ["PA_ALSA_PLUGHW"] = "0"
os.environ["PA_ALSA_IGNORE"] = "1"  # 這行額外加上 #禁用 PyAudio 的音訊裝置偵測


def on_processing_sentence(message):
  print(f'hello: {message["asr_sentence"]}')

def on_final_sentence(message):
  print(f'world: {message["asr_sentence"]}')

# check input device index
# p = pyaudio.PyAudio()
# info = p.get_host_api_info_by_index(0)
# numdevices = info.get('deviceCount')

# for i in range(0, numdevices):
#   if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
#     print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

asr_client = StreamingClient('api-key-applied-from-devconsole')
asr_client.start_streaming_wav(
  pipeline='asr-zh-en-std',
  # verbose=True,
  file='voice.wav')