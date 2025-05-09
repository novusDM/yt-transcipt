# app.py
from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

app = Flask(__name__)

@app.route('/get-transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        text_transcript = formatter.format_transcript(transcript)
        return jsonify({'transcript': text_transcript})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
