from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    location = data.get('location')
    soil_ph = data.get('soil_ph')
    preference = data.get('preference')

    # Mock crop recommendation logic
    recommended_crops = []
    if soil_ph < 6:
        recommended_crops = ['Rice', 'Potato']
    elif 6 <= soil_ph <= 7:
        recommended_crops = ['Wheat', 'Soybeans']
    else:
        recommended_crops = ['Alfalfa', 'Sunflower']

    return jsonify({'recommended_crops': recommended_crops})

if __name__ == '__main__':
    app.run(debug=True)
