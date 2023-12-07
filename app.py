from flask import Flask, render_template, request
import qrcode
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/makeQr', methods=['GET', 'POST'])
def make():
    data = request.form.to_dict()
    data_to_convert = data['data']
    qr = qrcode.make(data_to_convert)
    qr.save('static/image.jpg')
    return render_template('index.html')
app.run(host="0.0.0.0",debug=True)