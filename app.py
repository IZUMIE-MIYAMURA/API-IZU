import os
import random
from flask import Flask, jsonify, url_for

app = Flask(__name__)

IMAGE_FOLDER = os.path.join(os.getcwd(), 'HENTAI')

@app.route('/neko', methods=['GET'])
def random_image():
    try:
        # Debug statement
        print(f"IMAGE_FOLDER: {IMAGE_FOLDER}")

        # Ensure the directory exists
        if not os.path.isdir(IMAGE_FOLDER):
            return jsonify(error="Image folder does not exist"), 404

        # List all files in the directory
        files = os.listdir(IMAGE_FOLDER)

        # Filter to include only image files (simple check, can be extended)
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))]

        if not image_files:
            return jsonify(error="No images found in folder"), 404

        # Select a random image file
        random_image_file = random.choice(image_files)

        # Construct the URL for the selected image
        # Assuming images are served from /static/hentai
        image_url = url_for('static', filename=os.path.join('hentai', random_image_file), _external=True)

        # Return the JSON response with the image URL
        return jsonify(url=image_url), 200
    except Exception as e:
        # Log the error and return a 500 response
        print(f"Error occurred: {e}")
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
