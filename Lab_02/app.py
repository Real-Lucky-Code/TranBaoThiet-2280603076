from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.vigenere import VigenereCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')

@app.route('/railfence')
def railfence():
    return render_template('railfence.html')

@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

@app.route('/transposition')
def transposition():
    return render_template('transposition.html')


@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

@app.route('/encrypt_vigenere', methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route('/decrypt_vigenere', methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

@app.route('/encrypt_playfair', methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']   
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    encrypted_text = Playfair.playfair_encrypt(text, matrix)   
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route('/decrypt_playfair', methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']   
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    decrypted_text = Playfair.playfair_decrypt(text, matrix)   
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

@app.route('/encrypt_railfence', methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])    
    RailFence = RailFenceCipher()
    encrypted_text = RailFence.rail_fence_encrypt(text, key)   
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route('/decrypt_railfence', methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])  
    RailFence = RailFenceCipher()
    decrypted_text = RailFence.rail_fence_decrypt(text, key)   
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

@app.route('/encrypt_transposition', methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    Transposition = TranspositionCipher()
    encrypted_text = Transposition.encrypt(text, key)

    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route('/decrypt_transposition', methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Transposition = TranspositionCipher()
    decrypted_text = Transposition.decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
