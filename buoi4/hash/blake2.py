import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)  # Khởi tạo đối tượng hash Blake2b với kích thước băm 64 byte
    blake2_hash.update(message)  # Cập nhật dữ liệu vào đối tượng hash
    return blake2_hash.digest()  # Trả về giá trị băm dưới dạng bytes

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')  # Nhận chuỗi đầu vào và mã hóa thành bytes
    hashed_text = blake2(text)  # Tính toán hash của chuỗi đầu vào

    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))  # In ra chuỗi văn bản đã nhập
    print("BLAKE2 Hash:", hashed_text.hex())  # In ra giá trị hash dưới dạng hex

if __name__ == "__main__":
    main()