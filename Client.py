# client.py
# A simple client to connect to the secure caching service.

import socket

HOST = '127.0.0.1'
PORT = 65432

def main():
    """
    Connects to the server and sends a sample message.
    """
    print("Initializing client...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            
            # TODO: Phase 2 - Implement the client-side secure handshake and encryption.
            
            # TODO: Implement client logic to send SET, GET, DELETE commands.
            
            message_to_send = b'Hello, secure world!'
            print(f"Sending sample message: {message_to_send.decode()}")
            s.sendall(message_to_send)
            
            data = s.recv(1024)
            print(f"Received echo from server: {data.decode()}")

        except ConnectionRefusedError:
            print(f"Connection failed. Is the server running on {HOST}:{PORT}?")


if __name__ == "__main__":
    main()
