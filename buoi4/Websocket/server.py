import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()  # Tạo tập hợp các client kết nối

    def open(self):
        WebSocketServer.clients.add(self)  # Thêm client vào danh sách khi kết nối

    def on_close(self):
        WebSocketServer.clients.remove(self)  # Loại bỏ client khi đóng kết nối

    @classmethod
    def send_message(cls, message: str):
        print(f"Sending message ({message}) to {len(cls.clients)} client(s).")
        for client in cls.clients:
            client.write_message(message)  # Gửi tin nhắn cho tất cả các client

class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list  # Danh sách từ

    def sample(self):
        return random.choice(self.word_list)  # Chọn một từ ngẫu nhiên từ danh sách

def main():
    app = tornado.web.Application(
        [
            (r"/websocket/", WebSocketServer),  # Định nghĩa URL endpoint cho WebSocket
        ],
        websocket_ping_interval=10,
        websocket_ping_timeout=30,
    )
    app.listen(8888)  # Lắng nghe cổng 8888

    io_loop = tornado.ioloop.IOLoop.current()  # Khởi tạo vòng lặp I/O

    word_selector = RandomWordSelector(['apple', 'banana', 'orange', 'grape', 'melon'])  # Danh sách các từ

    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()),  # Gửi từ ngẫu nhiên
        3000  # Gửi mỗi 3 giây
    )

    periodic_callback.start()  # Bắt đầu gửi tin nhắn định kỳ

    io_loop.start()  # Bắt đầu vòng lặp I/O

if __name__ == "__main__":
    main()  # Gọi hàm main khi chạy chương trình
