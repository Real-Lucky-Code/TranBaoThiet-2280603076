import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txt_plaintext.toPlainText(),
            "key": self.ui.txt_key.toPlainText()  
        }
        try:
            response = requests.post(url, json=payload)
            print(f"Response status code: {response.status_code}")  # In HTTP code
            print(f"Response content: {response.text}")  # In nội dung phản hồi

            if response.status_code == 200:
                data = response.json()
                encrypted_message = data.get('encrypted_message', '')
                self.ui.txt_ciphertext.setText(encrypted_message)
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encryption Successful")
                msg.exec_()
            else:
                print(f"API returned an error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")


        
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_ciphertext.toPlainText(),
            "key": self.ui.txt_key.toPlainText()  # Sửa text() thành toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            print(f"Response status code: {response.status_code}")  # Debug thông tin HTTP
            print(f"Response content: {response.text}")  # In dữ liệu JSON

            if response.status_code == 200:  # Sửa lại điều kiện
                data = response.json()
                decrypted_message = data.get("decrypted_message", "")
                self.ui.txt_plaintext.setText(decrypted_message)
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decryption Successful")
                msg.exec_()
            else:
                print(f"API returned an error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
            