from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for spatial data
spatial_data = {
    "points": [],
    "lines": [],
    "polygons": [],
}

@app.route('/api/spatial-data', methods=['GET'])
def get_spatial_data():
    return jsonify(spatial_data)

@app.route('/api/spatial-data', methods=['POST'])
def add_spatial_feature():
    data = request.get_json()

    if data and "layer" in data and "feature" in data:
        layer = data["layer"]
        feature = data["feature"]

        spatial_data[layer].append(feature)

        return jsonify({"message": "Spatial feature added successfully."}), 201

    return jsonify({"message": "Invalid request body."}), 400

@app.route('/api/spatial-data/<layer>/<feature_id>', methods=['DELETE'])
def delete_spatial_feature(layer, feature_id):
    if layer in spatial_data and feature_id:
        for i, feature in enumerate(spatial_data[layer]):
            if feature.get("id") == feature_id:
                del spatial_data[layer][i]
                return jsonify({"message": "Spatial feature deleted successfully."})

    return jsonify({"message": "Spatial feature not found."}), 404

# Root-level GET route to serve HTML
@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
