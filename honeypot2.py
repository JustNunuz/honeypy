import os
import datetime
import json
import socket
import threading
import time
import sys
from pathlib import Path

class Honeypot:
    def __init__(self, log_dir):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.log_file = os.path.join(log_dir, f"honeypot_{datetime.datetime.now().strftime('%Y%m%d')}.json")

    def log_activity(self, port, remote_ip, data):
        """Log suspicious activity with timestamp and details"""
        activity = {
            "timestamp": datetime.datetime.now().isoformat(),
            "remote_ip": remote_ip,
            "port": port,
            "data": data.decode('utf-8', errors='ignore')
        }

        with open(self.log_file, 'a') as f:
            json.dump(activity, f)
            f.write('\n')

    def handle_connection(self, client_socket, remote_ip, port):
        """Handle individual connections and emulate services"""
        try:
            # Add your connection handling code here
            data = client_socket.recv(1024)
            self.log_activity(port, remote_ip, data)
            client_socket.sendall(b"Service response")
        except socket.error as e:
            print(f"Error handling connection: {e}")
        finally:
            client_socket.close()

    def start_listener(self, port):
        """Start listening on the specified port"""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen(5)
        print(f"Listening on port {port}")

        while True:
            try:
                client_socket, addr = server_socket.accept()
                remote_ip = addr[0]
                print(f"Connection from {remote_ip}")

                # Handle the connection in a new thread
                threading.Thread(target=self.handle_connection, args=(client_socket, remote_ip, port)).start()
            except socket.error as e:
                print(f"Error accepting connection: {e}")

def main():
    honeypot = Honeypot('/honeypot_logs') #log file directory

    # Start listeners for each port in separate threads
    for port in [21, 22, 80, 443]:
        listener_thread = threading.Thread(
            target=honeypot.start_listener,
            args=(port,)
        )
        listener_thread.daemon = True
        listener_thread.start()

    try:
        # Keep main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Shutting down honeypot...")
        sys.exit(0)

if __name__ == "__main__":
    main()