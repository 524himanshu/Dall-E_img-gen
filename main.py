import os
from flask import Flask, jsonify, render_template
import openai

# Fetch the OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generateimages/<prompt>')
def generate(prompt):
    try:
        # Call the OpenAI Image API with the provided prompt
        response = openai.Image.create(
            prompt=prompt,
            n=5,  # Number of images to generate
            size="256x256"
        )
        
        # Extract the image URLs from the response
        image_urls = [data['url'] for data in response['data']]
        
        # Return the image URLs as JSON
        return jsonify(image_urls=image_urls)
    except Exception as e:
        # Return an error message if the API call fails
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    # Start the Flask app on host 0.0.0.0 and port 81
    app.run(host='0.0.0.0', port=81)
