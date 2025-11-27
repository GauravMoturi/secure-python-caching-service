# server.py
# The main server logic for the secure caching service.

import socket

HOST = '127.0.0.1'
PORT = 65432

def main():
    """
    Initializes and runs the cache server.
    """
    print("Initializing Secure Cache Server...")
    
    # In-memory cache (dictionary) to store key-value pairs
    cache = {}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")

        # TODO: Phase 1 - Accept client connection and handle basic commands.
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            
            # TODO: Phase 2 - Implement the secure handshake and encryption/decryption layer.
            
            # TODO: Phase 3 - Re-architect to handle multiple clients concurrently using threading.
            
            # This is a placeholder loop to show a connection is established.
            while True:
                data = conn.recv(1024)
                if not data:
                    print(f"Connection with {addr} closed.")
                    break
                # For now, just echo back the data to the client.
                conn.sendall(data)

if __name__ == "__main__":
    main()
