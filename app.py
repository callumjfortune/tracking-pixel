import io
from flask import Flask, render_template, send_file
import base64

app = Flask(__name__)

pixel_content = base64.b64decode(
    b'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7'
)

@app.route('/square.png')
def tracking_pixel():

    print("Tracking pixel requested!")

    return send_file(
        io.BytesIO(pixel_content),
        mimetype='image/png',
        max_age=0
    )

@app.route('/content')
def squareHTML():

    print("Tracking pixel html requested!")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
