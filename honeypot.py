import socket
import threading
import datetime
import json
import os
import time
import sys

class Honeypot:
    def __init__(self, log_dir):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.log_file = os.path.join(log_dir, f"honeypot_{datetime.datetime.now().strftime('%Y%m%d')}.json")
        print(f"Log file will be created at: {self.log_file}")

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
        service_banners = {
            21: "220 FTP server ready\r\n",
            22: "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1\r\n",
            80: "HTTP/1.1 200 OK\r\nServer: Apache/2.4.41 (Ubuntu)\r\n\r\n",
            443: "HTTP/1.1 200 OK\r\nServer: Apache/2.4.41 (Ubuntu)\r\n\r\n"
        }

        try:
            # Send appropriate banner for the service
            if port in service_banners:
                client_socket.send(service_banners[port].encode())

            # Receive data from attacker
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                self.log_activity(port, remote_ip, data)
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
        # Initialize Honeypot with the directory where logs will be stored
        # Example: Honeypot('/var/log/honeypot_logs') or Honeypot('C:/honeypot_logs')
        honeypot = Honeypot('/honeypot_logs')

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
    Honeypot.main()