from flask import Flask, request, jsonify, send_from_directory
from generate_email import ColdEmailGenerator
import os

obj = ColdEmailGenerator(github_token=os.getenv("GITHUB_TOKEN"))

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/generate-email', methods=['POST'])
def generate_email():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    try:
        email_content = obj.generate_cold_email(url)
        return jsonify({'email': email_content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)