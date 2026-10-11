import socket
port = 5050
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

server_socket_address = (host_ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)

server.listen()
print("Server is listening")

port = 5050
buffer = 16
format = "utf-8"
disconnected = "End"


while True:
    conn, addr = server.accept()
    print("Connected to", addr)
    connected = True


    while connected:
        message_length = conn.recv(buffer).decode(format)
        print("Length of the message is", message_length)


        if message_length:
            message_length = int(message_length)
            msg = conn.recv(message_length).decode(format)
            if msg == disconnected:
                conn.send("Goodbye. It was nice to serve you.".encode(format))
                print("Terminating connection with", addr)
                connected = False
            else:
                hours = float(msg)
                if hours <= 40:
                    salary = hours * 200
                else:
                    salary = 8000 + (hours - 40) * 300
                conn.send(f"Your salary is Tk {salary:.2f}".encode(format))
    conn.close()