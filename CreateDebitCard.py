# Simple Python API using Flask
from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/CreateDebitCard', methods=['GET'])
def create_debit_card():
    response = {
        'card_number': '1234-5678-9876-5432',
        'status': 'active',
        'timestamp': datetime.datetime.now().isoformat()
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
