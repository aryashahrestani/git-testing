import psutil
import tkinter as tk

class SystemHealthChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("System Health Checker")

        # Create labels to display system health information
        self.cpu_label = tk.Label(root, text="CPU Usage: ")
        self.cpu_label.pack()

        self.memory_label = tk.Label(root, text="Memory Usage: ")
        self.memory_label.pack()

        self.ram_label = tk.Label(root, text="RAM Configuration: ")
        self.ram_label.pack()

        self.disk_labels = []
        self.network_label = tk.Label(root, text="Network Usage: ")
        self.network_label.pack()

        # Update system health information every second
        self.update_info()

    def update_info(self):
        # Get system health information
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        ram_info = psutil.virtual_memory()
        disks = psutil.disk_partitions(all=True)
        network_speed = (psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv) / 1024

        # Update labels with new system health information
        self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        self.memory_label.config(text=f"Memory Usage: {memory_usage}%")
        self.ram_label.config(text=f"RAM Configuration: {ram_info.total / (1024**3):.2f} GB")

        for i, disk in enumerate(disks):
            try:
                disk_usage = psutil.disk_usage(disk.mountpoint)
                disk_read_speed = psutil.disk_io_counters(perdisk=True).get(disk.device, psutil.disk_io_counters()).read_bytes / (1024 * 1024)
                disk_write_speed = psutil.disk_io_counters(perdisk=True).get(disk.device, psutil.disk_io_counters()).write_bytes / (1024 * 1024)
                disk_label_text = f"Disk {i + 1} Usage: Free: {disk_usage.free / (1024**3):.2f} GB | Read Speed: {disk_read_speed:.2f} MB/s | Write Speed: {disk_write_speed:.2f} MB/s"
                
                # Create new label for disk usage if not already created
                if len(self.disk_labels) <= i:
                    new_disk_label = tk.Label(self.root, text=disk_label_text)
                    new_disk_label.pack()
                    self.disk_labels.append(new_disk_label)
                else:
                    # Update existing label for disk usage
                    self.disk_labels[i].config(text=disk_label_text)
            except Exception as e:
                print(f"Error processing disk {i + 1}: {e}")

        # Remove extra disk labels if any
        if len(disks) < len(self.disk_labels):
            for j in range(len(disks), len(self.disk_labels)):
                self.disk_labels[j].destroy()
            self.disk_labels = self.disk_labels[:len(disks)]

        self.network_label.config(text=f"Network Usage: {network_speed:.2f} KB/s")

        # Schedule the next update after 1 second
        self.root.after(1000, self.update_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemHealthChecker(root)
    root.mainloop()
