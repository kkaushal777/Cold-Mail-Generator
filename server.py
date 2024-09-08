from flask import Flask, request, jsonify, send_from_directory
from backend import generate_cold_email

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
        email_content = generate_cold_email(url)
        return jsonify({'email': email_content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)