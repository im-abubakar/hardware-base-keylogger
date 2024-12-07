import serial
import time
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Setup the serial connection
arduino_port = 'COM10'  # Replace with the correct COM port for your Arduino
baud_rate = 9600
try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    logging.info("Serial connection established.")
except serial.SerialException as e:
    logging.error(f"Error opening serial connection: {e}")
    exit(1)

# Replace with your Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1314598947494301766/9e3u1FROKR8Uxfol8WgghR9w6HU7P1Ngkx6hKhPx1_2mynJSMGAcls5yVgIbZgazs1Jw"


def send_to_discord(data):
    payload = {"content": data}
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        logging.info("Data sent to Discord successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending data to Discord: {e}")

# Main loop
try:
    while True:
        if ser.in_waiting > 0:
            try:
                data = ser.readline().decode('utf-8').strip()
                if data:
                    logging.info(f"Received data from Arduino: {data}")
                    send_to_discord(data)
            except UnicodeDecodeError:
                logging.warning("Error decoding serial data. Skipping invalid data.")

        time.sleep(1)

except KeyboardInterrupt:
    logging.info("Program terminated by user.")
finally:
    if ser.is_open:
        ser.close()
        logging.info("Serial connection closed.")
