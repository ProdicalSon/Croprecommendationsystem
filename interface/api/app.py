from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    # Example data from the user
    data = request.json
    location = data.get("location")
    soil_ph = data.get("soil_ph")
    preference = data.get("preference")
    
    # Mock recommendation logic
    recommendations = [
        {"crop": "Wheat", "suitability": 90},
        {"crop": "Rice", "suitability": 85},
    ]
    
    return jsonify({"location": location, "recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
