from flask import Flask, jsonify
import random

app = Flask(__name__)


image_urls = [
    'https://example.com/image1.jpg',
    'https://example.com/image2.jpg',
    'https://example.com/image3.jpg',
    

 
@app.route('/random-image')
def get_random_image():
    random_image_url = random.choice(image_urls)
    return jsonify({'imageUrl': random_image_url})

if __name__ == '__main__':
    app.run(debug=True)
