import os
import random
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

IMAGE_FOLDER = os.path.join(os.getcwd(), 'HENTAI')

@app.route('/neko', methods=['GET'])
def serve_random_neko_image():
    try:
        random_image = random.choice(neko)
        return send_from_directory(IMAGE_DIRECTORY_NEKO, random_image)
    except IndexError:
        return "No images found in 'neko' directory", 404
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
