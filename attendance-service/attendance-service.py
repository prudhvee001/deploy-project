from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/attendance')
def attendance():
    return jsonify({"date": "2025-04-25", "status": "Present"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002)
