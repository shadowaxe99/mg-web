from flask import Flask, render_template, request, jsonify
from api.routes import api_blueprint
from workers.voice_synthesis_worker import voiceSynthesisWorker
from workers.chatbot_worker import chatbotWorker
import os
import json

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/api')

# Load configuration from file
with open('config/config.json') as config_file:
    config = json.load(config_file)

# Set up the database connection here if needed
# db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conversation')
def conversation():
    return render_template('conversation.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/monetization')
def monetization():
    return render_template('monetization.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    response = chatbotWorker(message, config['INFLUENCER_NAME'])
    return jsonify(response)

@app.route('/synthesize_voice', methods=['POST'])
def synthesize_voice():
    text = request.form['text']
    audio_content = voiceSynthesisWorker(text, config['INFLUENCER_NAME'])
    return jsonify({'audio_content': audio_content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))