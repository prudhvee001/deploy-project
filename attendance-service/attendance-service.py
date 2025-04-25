from flask import Flask, jsonify
from werkzeug.urls import url_quote  # Ensure the correct version of Werkzeug is installed

app = Flask(__name__)

@app.route('/attendance', methods=['GET'])
def get_attendance():
    return jsonify({"attendance": "success"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
