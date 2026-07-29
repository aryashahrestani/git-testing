import os
import http.server
import socketserver
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView

# Define the port number for the HTTP server
PORT = 8000  # Change the port number if needed

# Define the HTTP server handler class
class FileServer(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=os.getcwd(), **kwargs):
        super().__init__(*args, directory=directory, **kwargs)

# Define the popup for selecting a directory
class FileChooserPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create a FileChooserListView widget for selecting directories
        self.file_chooser = FileChooserListView(path=os.getcwd(), dirselect=True)
        # Bind the on_submit event to the select_directory method
        self.file_chooser.bind(on_submit=self.select_directory)
        # Set the content of the popup to the file chooser widget
        self.content = self.file_chooser

    # Method called when a directory is selected
    def select_directory(self, instance, selection, touch):
        # If no directory is selected, dismiss the popup
        if not selection:
            self.dismiss()
            return
        
        # Get the selected path
        selected_path = selection[0]
        # Check if the selected path is a directory
        if os.path.isdir(selected_path):
            # If it is a directory, dismiss the popup and start the server with the selected directory
            self.dismiss()
            start_server(selected_path)
        else:
            # If it is not a directory, display an error popup
            error_popup = Popup(title="Error", content=Label(text="Please select a directory."), size_hint=(None, None), size=(300, 150))
            error_popup.open()

# Define the main application class
class MainApp(App):
    # Method called when the application is built
    def build(self):
        # Create a vertical box layout
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        # Create a button for selecting a directory
        select_button = Button(text="Select Directory", size_hint=(1, None), height=50)
        # Bind the on_press event of the button to the show_file_chooser method
        select_button.bind(on_press=self.show_file_chooser)
        # Add the button to the layout
        layout.add_widget(select_button)
        # Return the layout
        return layout

    # Method called when the "Select Directory" button is pressed
    def show_file_chooser(self, instance):
        # Create and open the file chooser popup
        file_chooser_popup = FileChooserPopup(title="Select Directory")
        file_chooser_popup.open()

# Method for starting the HTTP server
def start_server(directory):
    # Change the current working directory to the selected directory
    os.chdir(directory)
    # Start the HTTP server
    with socketserver.TCPServer(("", PORT), FileServer) as httpd:
        print(f"Server started on port {PORT} serving files from {directory}")
        try:
            # Serve requests indefinitely
            httpd.serve_forever()
        except KeyboardInterrupt:
            # Handle keyboard interrupt (Ctrl+C)
            print("\nServer stopped.")
            httpd.server_close()

# Entry point of the program
if __name__ == "__main__":
    # Run the main application
    MainApp().run()
