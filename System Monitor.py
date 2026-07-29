import psutil
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class SystemMonitor:
    def __init__(self, root):
        # Initialize the Tkinter root window
        self.root = root
        self.root.title("System Monitor")

        # Create subplots for CPU, memory, disk, and network usage
        self.cpu_fig, self.cpu_ax = plt.subplots(figsize=(4, 2))
        self.cpu_plot, = self.cpu_ax.plot([], [], 'r-')
        self.cpu_ax.set_title('CPU Usage (%)')
        self.cpu_ax.set_xlim(0, 50)
        self.cpu_ax.set_ylim(0, 100)
        self.cpu_ax.grid(True)

        self.memory_fig, self.memory_ax = plt.subplots(figsize=(4, 2))
        self.memory_plot, = self.memory_ax.plot([], [], 'g-')
        self.memory_ax.set_title('Memory Usage (%)')
        self.memory_ax.set_xlim(0, 50)
        self.memory_ax.set_ylim(0, 100)
        self.memory_ax.grid(True)

        self.disk_fig, self.disk_ax = plt.subplots(figsize=(4, 2))
        self.disk_plot, = self.disk_ax.plot([], [], 'b-')
        self.disk_ax.set_title('Disk Usage (%)')
        self.disk_ax.set_xlim(0, 50)
        self.disk_ax.set_ylim(0, 100)
        self.disk_ax.grid(True)

        self.network_fig, self.network_ax = plt.subplots(figsize=(4, 2))
        self.network_plot, = self.network_ax.plot([], [], 'm-')
        self.network_ax.set_title('Network Usage (KB)')
        self.network_ax.set_xlim(0, 50)
        self.network_ax.set_ylim(0, 1024)
        self.network_ax.grid(True)

        # Create FigureCanvasTkAgg for each subplot and pack them into the root window
        self.canvas1 = FigureCanvasTkAgg(self.cpu_fig, master=root)
        self.canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas2 = FigureCanvasTkAgg(self.memory_fig, master=root)
        self.canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas3 = FigureCanvasTkAgg(self.disk_fig, master=root)
        self.canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas4 = FigureCanvasTkAgg(self.network_fig, master=root)
        self.canvas4.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create FuncAnimation to update plots every second
        self.anim = FuncAnimation(self.cpu_fig, self.update_info, interval=1000)

    def update_info(self, frame):
        # Get system information
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        network_usage = (psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv) / 1024

        # Update plots with new data
        self.update_plot(self.cpu_ax, self.cpu_plot, cpu_usage)
        self.update_plot(self.memory_ax, self.memory_plot, memory_usage)
        self.update_plot(self.disk_ax, self.disk_plot, disk_usage)
        self.update_plot(self.network_ax, self.network_plot, network_usage)

    def update_plot(self, ax, plot, value):
        # Update plot data
        plot.set_data(range(len(plot.get_xdata()) + 1), list(plot.get_ydata()) + [value])
        ax.relim()
        ax.autoscale_view(True,True,True)
        ax.figure.canvas.draw()

        # Hide previous text annotations
        for txt in ax.texts:
            txt.set_visible(False)

        # Add new text annotation for usage percentage
        ax.text(0.95, 0.95, f'{value:.1f}%', verticalalignment='top', horizontalalignment='right', transform=ax.transAxes)

if __name__ == "__main__":
    # Create Tkinter root window and SystemMonitor instance
    root = tk.Tk()
    app = SystemMonitor(root)
    root.mainloop()
