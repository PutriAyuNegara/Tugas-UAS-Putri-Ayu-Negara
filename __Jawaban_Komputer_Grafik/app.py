# pip install flask
# pip install Pillow
from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No image uploaded!', 400

    image = request.files['image']
    image_path = f"static/{image.filename}"
    image.save(image_path)

    return render_template('settings.html', image_path=image_path)

@app.route('/settings', methods=['POST'])
def settings():
    size = int(request.form['size'])
    position = request.form['position']
    image_path = request.form['image_path']

    img = Image.open(image_path)

    # Resize image
    img.thumbnail((size, size))

    # Calculate crop dimensions
    width, height = img.size
    left = 0
    top = 0
    right = width
    bottom = height

    if position == 'top_left':
        right = size
        bottom = size
    elif position == 'top_center':
        left = (width - size) // 2
        right = left + size
        bottom = size
    elif position == 'top_right':
        left = width - size
        right = width
        bottom = size
    elif position == 'center_left':
        top = (height - size) // 2
        right = size
        bottom = top + size
    elif position == 'center':
        left = (width - size) // 2
        top = (height - size) // 2
        right = left + size
        bottom = top + size
    elif position == 'center_right':
        left = width - size
        top = (height - size) // 2
        right = width
        bottom = top + size
    elif position == 'bottom_left':
        top = height - size
        right = size
        bottom = height
    elif position == 'bottom_center':
        left = (width - size) // 2
        top = height - size
        right = left + size
        bottom = height
    elif position == 'bottom_right':
        left = width - size
        top = height - size
        right = width
        bottom = height

    # Crop image
    img = img.crop((left, top, right, bottom))

    modified_image_path = f"static/modified_{image_path.split('/')[-1]}"
    img.save(modified_image_path)

    return render_template('result.html', image_path=modified_image_path)

if __name__ == '__main__':
    app.run(debug=True)
