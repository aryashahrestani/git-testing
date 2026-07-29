import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from kivy.metrics import dp  # dp for converting from density-independent pixels to pixels

class DiskUsageAnalyzer(App):
    def calculate_disk_usage(self, directory):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(directory):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
            for d in dirnames:
                dp = os.path.join(dirpath, d)
                total_size += os.stat(dp).st_size
                self.directory_sizes[dp] = self.convert_bytes(os.stat(dp).st_size, "MB")
        return total_size

    def get_directory_size(self, directory):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(directory):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
            for d in dirnames:
                dp = os.path.join(dirpath, d)
                total_size += os.stat(dp).st_size
        return total_size

    def convert_bytes(self, size, unit=None):
        if unit == "KB":
            return size / 1024
        elif unit == "MB":
            return size / (1024 * 1024)
        elif unit == "GB":
            return size / (1024 * 1024 * 1024)
        else:
            return size

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))  # Create a vertical BoxLayout with spacing and padding

        self.directory_sizes = {}  # Dictionary to store directory sizes

        self.directory_input = TextInput(hint_text="Selected directory will appear here", multiline=False, readonly=True)  # TextInput for displaying selected directory
        layout.add_widget(self.directory_input)  # Add TextInput widget to layout

        self.file_chooser = FileChooserListView()  # FileChooserListView for selecting directory
        self.file_chooser.bind(selection=self.on_file_selected)  # Bind selection event to on_file_selected method
        layout.add_widget(self.file_chooser)  # Add FileChooserListView widget to layout



        self.result_label = Label(text="", size_hint_y=None, height=dp(200), valign='top', text_size=(None, None))  # Label for displaying analysis result
        layout.add_widget(self.result_label)  # Add Label widget to layout

        return layout  # Return the layout as the root widget of the application

    def on_file_selected(self, instance, selection):
        if selection:
            self.directory_input.text = selection[0]  # Update TextInput with selected directory path

    def analyze(self, instance):
        directory = self.directory_input.text
        if os.path.exists(directory):
            total_size = self.calculate_disk_usage(directory)
            result_text = f"Total disk usage of '{directory}' is: {self.convert_bytes(total_size, 'MB'):.2f} MB\n"
            for dirpath, size in self.directory_sizes.items():
                result_text += f"{dirpath}: {size:.2f} MB\n"
            self.result_label.text = result_text  # Update Label with analysis result
        else:
            self.result_label.text = "Directory does not exist."

if __name__ == "__main__":
    DiskUsageAnalyzer().run()  # Run the Kivy application
