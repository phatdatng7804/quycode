from flask import Flask, request, jsonify
from cipher.rsa.rsa_utils import RSACipher

app = Flask(__name__)

# Khởi tạo đối tượng RSA Cipher
rsa_cipher = RSACipher()

# ✅ API tạo khóa RSA
@app.route("/api/rsa/generate_keys", methods=["GET"])
def rsa_generate_keys():
    test= rsa_cipher.generate_keys()
    print(test)
    return jsonify({"message": "Keys generated successfully"})

# ✅ API mã hóa RSA
@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.json
    message = data["message"]
    key_type = data["key_type"]

    private_key, public_key = rsa_cipher.load_keys()
    if key_type == "public":
        key = public_key
    elif key_type == "private":
        key = private_key
    else:
        return jsonify({"error": "Invalid key type"})

    encrypted_message = rsa_cipher.encrypt(message, key)
    encrypted_hex = encrypted_message.hex()
    return jsonify({"encrypted_message": encrypted_hex})

# ✅ API giải mã RSA
@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.json
    ciphertext_hex = data["ciphertext"]
    key_type = data["key_type"]

    private_key, public_key = rsa_cipher.load_keys()
    if key_type == "public":
        key = public_key
    elif key_type == "private":
        key = private_key
    else:
        return jsonify({"error": "Invalid key type"})

    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted_message = rsa_cipher.decrypt(ciphertext, key)
    return jsonify({"decrypted_message": decrypted_message})

# ✅ API ký RSA
@app.route("/api/rsa/sign", methods=["POST"])
def rsa_sign_message():
    data = request.json
    message = data["message"]
    private_key, _ = rsa_cipher.load_keys()

    signature = rsa_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({"signature": signature_hex})

# ✅ API xác minh chữ ký RSA
@app.route("/api/rsa/verify", methods=["POST"])
def rsa_verify_signature():
    data = request.json
    message = data["message"]
    signature_hex = data["signature"]

    public_key, _ = rsa_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = rsa_cipher.verify(message, signature, public_key)

    return jsonify({"is_verified": is_verified})

# ✅ Chạy ứng dụng Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
