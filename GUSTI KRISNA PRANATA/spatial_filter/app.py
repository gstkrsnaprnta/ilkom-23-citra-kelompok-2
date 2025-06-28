from flask import Flask, render_template, request, send_file
from PIL import Image
import numpy as np
import io
from werkzeug.utils import secure_filename
from your_filter_file import sharpen_image  

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            img = Image.open(file.stream).convert('RGB')
            img_np = np.array(img)
            enhanced = sharpen_image(img_np)
            output_img = Image.fromarray(enhanced)

            buf = io.BytesIO()
            output_img.save(buf, format='PNG')
            buf.seek(0)
            return send_file(buf, mimetype='image/png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
