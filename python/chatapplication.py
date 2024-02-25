import socket
import threading

# Function to handle receiving messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(message)
        except:
            print("An error occurred while receiving messages.")
            break

# Function to handle sending messages
def send_messages(client_socket, username):
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client_socket.send(f"{username}: {message}".encode("utf-8"))

def main():
    # Set up the socket
    server = "127.0.0.1"
    port = 55555
    username = input("Enter your username: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server, port))

    # Send the username to the server
    client_socket.send(username.encode("utf-8"))

    # Start threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket, username))
    send_thread.start()

    print("Type your message below. Type 'exit' to leave the chat room.")

if __name__ == "__main__":
    main()
