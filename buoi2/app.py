from flask import Flask, render_template, request
from cipher.ceasar import CeasarCipher  # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ceasar/encrypt', methods=['POST'])
def ceasar():
    return render_template('ceasar.html')

@app.route("/encrypt", methods=['POST'])
def encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['InputKeyPlain'])  # Đảm bảo key là số nguyên
    ceasar = CeasarCipher()
    encrypted_text = ceasar.encrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['InputKeyCipher'])
    ceasar = CeasarCipher()
    decrypted_text = ceasar.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
