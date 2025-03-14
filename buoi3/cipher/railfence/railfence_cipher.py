class RailFenceCipher:
    def __init__(self):
        pass

    # Hàm mã hóa theo thuật toán Rail Fence
    def rail_fence_encrypt(self, plain_text, num_rails):
        # Tạo danh sách các hàng (rails) để chứa các ký tự
        rails = [[] for _ in range(num_rails)]
        rail_index = 0  # Vị trí hiện tại trong hàng
        direction = 1  # 1: di chuyển xuống, -1: di chuyển lên

        # Duyệt từng ký tự trong văn bản
        for char in plain_text:
            rails[rail_index].append(char)  # Thêm ký tự vào hàng hiện tại

            # Điều chỉnh hướng đi
            if rail_index == 0:
                direction = 1  # Nếu ở trên cùng, đi xuống
            elif rail_index == num_rails - 1:
                direction = -1  # Nếu ở dưới cùng, đi lên
            rail_index += direction  # Chuyển đến hàng tiếp theo

        # Nối tất cả các ký tự theo thứ tự để tạo bản mã hóa
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    # Hàm giải mã theo thuật toán Rail Fence
    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Tạo danh sách chứa độ dài của từng hàng (rail)
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        # Xác định số ký tự thuộc về mỗi hàng trong chuỗi mã hóa
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1  # Tăng số lượng ký tự của hàng hiện tại

            # Điều chỉnh hướng đi
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Tách chuỗi mã hóa thành từng hàng theo số lượng ký tự đã tính
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])  # Lấy phần của chuỗi theo độ dài tương ứng
            start += length
        
        plain_text = ""  # Biến chứa kết quả giải mã
        rail_index = 0
        direction = 1

        # Duyệt lại để lấy ký tự đúng vị trí theo thứ tự đọc ban đầu
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index][0]  # Lấy ký tự đầu tiên của hàng hiện tại
            rails[rail_index] = rails[rail_index][1:]  # Loại bỏ ký tự vừa lấy

            # Điều chỉnh hướng đi
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction  # Chuyển đến hàng tiếp theo
        
        return plain_text  # Trả về bản rõ sau khi giải mã
