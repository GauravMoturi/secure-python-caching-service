# server.py
# The main server logic for the High-Performance & Secure Caching Service.

import socket
import threading

# In-memory key-value store
cache = {}
# Lock for thread-safe access to the cache
cache_lock = threading.Lock()

HOST = '127.0.0.1'
PORT = 6379

def handle_client(conn, addr):
    """Handles a single client connection."""
    print(f"[NEW CONNECTION] {addr} connected.")
    
    try:
        # TODO: Phase 3 - Implement secure handshake with client.
        
        while True:
            data = conn.recv(1024).decode('utf-8').strip()
            if not data:
                break
            
            # TODO: Phase 3 - Decrypt incoming data after handshake.
            
            parts = data.split()
            command = parts[0].upper()
            response = ""

            # Phase 2: Use cache_lock to make write operations thread-safe
            if command in ["SET", "DELETE"]:
                with cache_lock:
                    if command == "SET" and len(parts) >= 3:
                        key = parts[1]
                        value = " ".join(parts[2:])
                        cache[key] = value
                        response = "OK"
                    elif command == "DELETE" and len(parts) == 2:
                        key = parts[1]
                        if key in cache:
                            del cache[key]
                            response = "1"
                        else:
                            response = "0"
            # Read operations don't strictly need a lock in this simple case but would in a more complex system.
            elif command == "GET" and len(parts) == 2:
                key = parts[1]
                response = cache.get(key, "(nil)")
            elif command == "PING":
                response = "PONG"
            else:
                response = "ERROR: Unknown command or incorrect arguments."

            # TODO: Phase 3 - Encrypt outgoing response.
            conn.sendall(f"{response}\n".encode('utf-8'))

    finally:
        print(f"[DISCONNECTED] {addr} disconnected.")
        conn.close()

def main():
    """Initializes and runs the cache server."""
    print("[STARTING] Server is starting...")
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    
    while True:
        conn, addr = server_socket.accept()
        # Phase 2: Create a new thread for each client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
