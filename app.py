from flask import Flask, request, jsonify, Response, json
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        prediction = model.predict(np.array([data['features']]))
        result = {
            'message': f'Predicted score for the input data is {prediction[0]:.2f}.'
        }
        print("Response to client:", result)
        return Response(json.dumps(result), mimetype='application/json')
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
