from cipher.caesar import alphabet

class CaesarCipher:
    def __init__(self):
        # Khởi tạo CaesarCipher với bảng chữ cái đã cho
        self.alphabet = alphabet
    
    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)  # Độ dài bảng chữ cái
        text = text.upper()  # Chuyển tất cả ký tự sang chữ hoa
        encrypted_text = []

        for letter in text:
            letter_index = self.alphabet.index(letter)  # Lấy vị trí của ký tự trong bảng chữ cái
            output_index = (letter_index + key) % alphabet_len  # Dịch chuyển theo khóa
            output_letter = self.alphabet[output_index]  # Lấy ký tự sau khi dịch chuyển
            encrypted_text.append(output_letter)  # Thêm vào kết quả

        return "".join(encrypted_text)  # Trả về chuỗi đã mã hóa
    
    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)  # Độ dài bảng chữ cái
        text = text.upper()  # Chuyển tất cả ký tự sang chữ hoa
        decrypted_text = []

        for letter in text:
            letter_index = self.alphabet.index(letter)  # Lấy vị trí của ký tự trong bảng chữ cái
            output_index = (letter_index - key) % alphabet_len  # Dịch ngược lại theo khóa
            output_letter = self.alphabet[output_index]  # Lấy ký tự sau khi dịch ngược
            decrypted_text.append(output_letter)  # Thêm vào kết quả

        return "".join(decrypted_text)  # Trả về chuỗi đã giải mã
