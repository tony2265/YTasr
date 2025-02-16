import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

from flask import Flask, request, jsonify
from ailabs_asr.streaming import StreamingClient

# 初始化 Flask
app = Flask(__name__)

# 初始化 ASR 客戶端
asr_client = StreamingClient(
    key='74ffd750e35599f025915e9c1d865aa21d2c6ee8'
)

# 定義一個路由來接收音檔並進行辨識
@app.route('/recognize', methods=['POST'])
def recognize():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    # 接收上傳的音檔
    audio_file = request.files['file']

    # 開始語音辨識
    result = []
    def on_processing_sentence(message):
        result.append({"partial": message["asr_sentence"]})

    def on_final_sentence(message):
        result.append({"final": message["asr_sentence"]})

    asr_client.start_streaming_wav(
        pipeline='asr-zh-tw-std',
        file=audio_file,
        on_processing_sentence=on_processing_sentence,
        on_final_sentence=on_final_sentence
    )

    # 回傳辨識結果，包裹成物件格式
    return jsonify({"results": result})

# 啟動 Flask 伺服器
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=False, host='0.0.0.0', port=port)