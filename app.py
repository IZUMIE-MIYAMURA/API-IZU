import os
import json
import random
from flask import Flask, jsonify

app = Flask(__name__)

# Path to the JSON file containing image URLs
JSON_FILE_PATH = os.path.join(os.getcwd(), 'HENTAI', 'neko.json')

@app.route('/neko', methods=['GET'])
def random_image():
    try:
        # Ensure the JSON file exists
        if not os.path.isfile(JSON_FILE_PATH):
            return jsonify(error="JSON file does not exist"), 404

        # Read the JSON file
        with open(JSON_FILE_PATH, 'r') as file:
            image_urls = json.load(file)

        # Ensure the JSON file is not empty
        if not image_urls:
            return jsonify(error="No images found in JSON file"), 404

        # Select a random image URL
        random_image_url = random.choice(image_urls)

        # Return the JSON response with the image URL
        return jsonify(url=random_image_url), 200
    except Exception as e:
        # Log the error and return a 500 response
        print(f"Error occurred: {e}")
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
