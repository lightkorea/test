# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data.get('message', 'No message provided')
    
    # 메시지를 콘솔에 출력
    print(f"Received message: {message}")

    return jsonify({"status": "Message received", "message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
