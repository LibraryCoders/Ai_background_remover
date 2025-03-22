from flask import Flask, request, render_template
from rembg import remove
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    output_image = None
    if request.method == 'POST':
        file = request.files['image']
        if file:
            input_image = Image.open(file.stream)
            output_image = remove(input_image)
            img_byte_arr = io.BytesIO()
            output_image.save(img_byte_arr, format='PNG', quality=100)

            img_byte_arr.seek(0)
            output_image = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')

    return render_template('upload.html', output_image=output_image)

if __name__ == '__main__':
    app.run(debug=True)
