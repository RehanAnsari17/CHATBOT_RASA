
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/seat_availability', methods=['GET'])
def seat_availability():
    departure = request.args.get('from')
    destination = request.args.get('to')
    travel_date = request.args.get('date')
    class_type = request.args.get('class')
    train_number = request.args.get('train_number')

    mock_data = {
        'seats_available': 50
    }

    return jsonify(mock_data)

if __name__ == '__main__':
    app.run(port=5001)
