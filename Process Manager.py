import tkinter as tk
import psutil

class ProcessManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Manager")

        # Create frame to display process list
        self.process_frame = tk.Frame(root)
        self.process_frame.pack(pady=10)

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.process_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create listbox to display processes
        self.process_listbox = tk.Listbox(self.process_frame, width=100, height=20, yscrollcommand=self.scrollbar.set)
        self.process_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.config(command=self.process_listbox.yview)

        # Refresh button
        self.refresh_button = tk.Button(root, text="Refresh Processes", command=self.refresh_processes)
        self.refresh_button.pack(pady=5)

        # Kill button
        self.kill_button = tk.Button(root, text="Kill Process", command=self.kill_process)
        self.kill_button.pack(pady=5)

    def refresh_processes(self):
        # Clear the listbox
        self.process_listbox.delete(0, tk.END)

        # Get the list of running processes
        running_processes = psutil.process_iter()

        # Add processes to the listbox
        for process in running_processes:
            try:
                process_info = process.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
                self.process_listbox.insert(tk.END, f"{process_info['pid']} - {process_info['name']} - CPU%: {process_info['cpu_percent']:.2f} - MEM%: {process_info['memory_percent']:.2f}")
            except psutil.NoSuchProcess:
                # Skip processes that are no longer running
                pass

    def kill_process(self):
        # Get the selected process from the listbox
        selected_index = self.process_listbox.curselection()
        if selected_index:
            process_info = self.process_listbox.get(selected_index).split(" - ")[0]
            pid = int(process_info)
            # Kill the process
            try:
                process = psutil.Process(pid)
                process.terminate()
                self.refresh_processes()  # Refresh process list after killing
                tk.messagebox.showinfo("Success", f"Process with PID {pid} has been terminated.")
            except psutil.NoSuchProcess:
                tk.messagebox.showerror("Error", "Process is no longer running.")
        else:
            tk.messagebox.showwarning("Warning", "Please select a process to kill.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProcessManagerGUI(root)
    app.refresh_processes()  # Refresh processes initially
    root.mainloop()
