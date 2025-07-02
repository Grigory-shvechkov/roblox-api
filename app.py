from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "✅ Roblox API is running!", 200

@app.route('/roblox-data', methods=['POST'])
def roblox_data():
    data = request.get_json()
    print("✅ Received from Roblox:", data)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Render uses port 10000
