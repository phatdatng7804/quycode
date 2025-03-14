class TranspositionCipher:
    def __init__(self):
        pass

    # Hàm mã hóa theo thuật toán hoán vị (Transposition Cipher)
    def encrypt(self, text, key):
        encrypted_text = ''
        
        # Duyệt qua từng cột từ 0 đến key-1
        for col in range(key):
            pointer = col  # Vị trí ký tự hiện tại trong chuỗi đầu vào
            
            # Thêm ký tự theo khoảng cách `key`
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key  # Nhảy sang ký tự tiếp theo trong cùng một cột
        
        return encrypted_text  # Trả về chuỗi đã mã hóa

    # Hàm giải mã theo thuật toán hoán vị (Transposition Cipher)
    def decrypt(self, text, key):
        # Tạo danh sách rỗng với số lượng phần tử bằng `key`
        decrypted_text = [''] * key
        row, col = 0, 0  # Bắt đầu từ hàng 0, cột 0
        
        # Duyệt từng ký tự trong chuỗi mã hóa
        for symbol in text:
            decrypted_text[col] += symbol  # Thêm ký tự vào cột tương ứng
            col += 1  # Chuyển sang cột tiếp theo
            
            # Nếu đạt tới số cột hoặc đến gần cuối hàng, chuyển xuống hàng tiếp theo
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1
        
        return ''.join(decrypted_text)  # Ghép các phần tử lại để trả về văn bản gốc
