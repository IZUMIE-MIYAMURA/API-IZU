import os
import json
import random
from flask import Flask, jsonify

app = Flask(__name__)

# Path to the JSON file containing image URLs
NEKO_IMAGE = os.path.join(os.getcwd(), 'HENTAI', 'neko.json')
CUM_IMAGE = os.path.join(os.getcwd(), 'HENTAI', 'cum.json')
LOGO_IMAGE = os.path.join(os.getcwd(),'HENTAI',"logo.json')
@app.route('/neko', methods=['GET'])
def random_neko_image():
    try:
        # Ensure the JSON file exists
        if not os.path.isfile(NEKO_IMAGE):
            return jsonify(error="JSON file does not exist"), 404

        # Read the JSON file
        with open(NEKO_IMAGE, 'r') as file:
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

@app.route('/cum', methods=['GET'])
def random_cum_image():
    try:
        # Ensure the JSON file exists
        if not os.path.isfile(CUM_IMAGE):
            return jsonify(error="JSON file does not exist"), 404

        # Read the JSON file
        with open(CUM_IMAGE, 'r') as file:
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

@app.route('/logo', methods=['GET'])
def random_logo_image():
    try:
        # Ensure the JSON file exists
        if not os.path.isfile(LOGO_IMAGE):
            return jsonify(error="JSON file does not exist"), 404

        # Read the JSON file
        with open(LOGO_IMAGE, 'r') as file:
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
