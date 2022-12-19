from flask import Flask, render_template
from main import img
import os

app = Flask(__name__)

picImage = os.path.join('static')

app.config['UPLOAD_FOLDER'] = picImage


@app.route('/person_detection', methods=['GET', 'POST'])
def person_detection():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'ludzie_2.jpg')
    return render_template("index.html", user_image=pic1)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
