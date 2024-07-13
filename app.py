from flask import Flask, send_file, jsonify
import os
import random

app = Flask(__name__)

# Folder containing images
IMAGE_FOLDER = 'neko'

@app.route('/random-image', methods=['GET'])
def random_image():
    # Get list of all files in the image folder
    images = os.listdir(IMAGE_FOLDER)
    
    # Filter out non-image files if necessary
    images = [img for img in images if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Choose a random image
    if images:
        selected_image = random.choice(images)
        image_path = os.path.join(IMAGE_FOLDER, selected_image)
        
        # Return the image file
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return jsonify({"error": "No images found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
