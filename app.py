import os
import random
from flask import Flask, send_file, jsonify

app = Flask(__name__)

IMAGE_FOLDER = os.path.join(os.getcwd(), 'neko')

@app.route('/neko', methods=['GET'])
def random_image():
    try:
        # Debug statement
        print(f"IMAGE_FOLDER: {IMAGE_FOLDER}")
        # Ensure the directory exists
        if not os.path.isdir(IMAGE_FOLDER):
            return jsonify(error="Image folder does not exist"), 404

        images = os.listdir(IMAGE_FOLDER)
        if not images:
            return jsonify(error="No images found"), 404
        
        random_image = random.choice(images)
        image_path = os.path.join(IMAGE_FOLDER, random_image)

        # Debug statement
        print(f"Serving image: {image_path}")
        return send_file(image_path, mimetype='image/jpeg')
    except Exception as e:
        # Debug statement
        print(f"Error: {e}")
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
