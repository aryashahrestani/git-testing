import tkinter as tk
from tkinter import messagebox
import socket
from threading import Thread

class PortScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Port Scanner")
        
        # Host input
        self.host_label = tk.Label(root, text="Enter Host IP:")
        self.host_label.grid(row=0, column=0, padx=10, pady=5)
        self.host_entry = tk.Entry(root, width=30)
        self.host_entry.grid(row=0, column=1, padx=10, pady=5)

        # Port range input
        self.port_range_label = tk.Label(root, text="Enter Port Range (start-end):")
        self.port_range_label.grid(row=1, column=0, padx=10, pady=5)
        self.port_range_entry = tk.Entry(root, width=30)
        self.port_range_entry.grid(row=1, column=1, padx=10, pady=5)

        # Scan button
        self.scan_button = tk.Button(root, text="Scan", command=self.start_scan)
        self.scan_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Output text area
        self.output_text = tk.Text(root, height=20, width=50)
        self.output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def start_scan(self):
        # Get host and port range from user input
        host = self.host_entry.get()
        port_range = self.port_range_entry.get()

        # Validate host and port range inputs
        if not host:
            messagebox.showerror("Error", "Please enter a valid host IP.")
            return
        try:
            start_port, end_port = map(int, port_range.split('-'))
            if not (1 <= start_port <= end_port <= 65535):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid port range in the format 'start-end' (e.g., 1-1000).")
            return

        # Clear output text area
        self.output_text.delete("1.0", tk.END)

        # Start scanning ports in a separate thread
        scan_thread = Thread(target=self.scan_ports, args=(host, start_port, end_port))
        scan_thread.start()

    def scan_ports(self, host, start_port, end_port):
        # Scan ports and update output text area
        self.output_text.insert(tk.END, f"Scanning ports {start_port}-{end_port} on host {host}...\n")
        for port in range(start_port, end_port + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.5)
                    result = sock.connect_ex((host, port))
                    if result == 0:
                        self.output_text.insert(tk.END, f"Port {port} is open\n")
            except Exception as e:
                print(f"Error scanning port {port}: {e}")

def main():
    root = tk.Tk()
    app = PortScannerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
