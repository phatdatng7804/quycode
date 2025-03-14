class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def __init__(self):
        pass

    # Hàm tạo ma trận Playfair từ khóa
    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")  # Thay thế chữ 'J' bằng 'I' để chuẩn hóa
        key = key.upper()  # Chuyển đổi tất cả ký tự thành chữ in hoa
        key_set = set(key)  # Sử dụng tập hợp để loại bỏ các ký tự trùng lặp
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Bảng chữ cái không có 'J'
        remaining_letters = [letter for letter in alphabet if letter not in key_set]  # Các chữ cái còn lại sau khi trừ đi từ khóa
        matrix = list(key)  # Khởi tạo danh sách ma trận với từ khóa

        # Thêm các ký tự còn lại vào ma trận
        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:  # Ma trận Playfair có 25 ô (5x5)
                break

        # Chia danh sách thành ma trận 5x5
        playfair_matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    # Hàm tìm vị trí của một chữ cái trong ma trận Playfair
    def find_letter_coords(self, letter, matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col  # Trả về tọa độ của chữ cái

    # Hàm mã hóa văn bản bằng Playfair
    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I")  # Chuẩn hóa văn bản đầu vào
        plain_text = plain_text.upper()  # Chuyển thành chữ in hoa
        encrypted_text = ""

        for i in range(0, len(plain_text), 2):  # Xử lý từng cặp ký tự
            pair = plain_text[i:i + 2]
            if len(pair) == 1:  # Nếu chỉ còn một ký tự, thêm 'X' vào cuối
                pair += "X"

            # Lấy tọa độ của từng ký tự trong cặp
            row1, col1 = self.find_letter_coords(pair[0], matrix)
            row2, col2 = self.find_letter_coords(pair[1], matrix)

            # Quy tắc mã hóa Playfair
            if row1 == row2:  # Cùng hàng -> Lấy ký tự bên phải
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột -> Lấy ký tự bên dưới
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:  # Khác hàng, khác cột -> Đổi chéo góc
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    # Hàm giải mã văn bản mã hóa bằng Playfair
    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()  # Chuyển thành chữ in hoa
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):  # Xử lý từng cặp ký tự
            pair = cipher_text[i:i + 2]
            row1, col1 = self.find_letter_coords(pair[0], matrix)
            row2, col2 = self.find_letter_coords(pair[1], matrix)

            # Quy tắc giải mã Playfair
            if row1 == row2:  # Cùng hàng -> Lấy ký tự bên trái
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột -> Lấy ký tự bên trên
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:  # Khác hàng, khác cột -> Đổi chéo góc
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        # Loại bỏ ký tự chèn thêm (ví dụ: 'X') để có bản rõ gốc
        banro = ""
        for i in range(0, len(decrypted_text) - 2, 2):
            if decrypted_text[i] == decrypted_text[i + 2]:  # Nếu hai ký tự giống nhau, bỏ ký tự ở giữa
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + decrypted_text[i + 1]

        # Xử lý ký tự cuối cùng nếu nó là 'X' thì loại bỏ
        if decrypted_text[-1] == "X":
            banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-2] + decrypted_text[-1]

        return banro  # Trả về bản rõ sau khi loại bỏ ký tự chèn
