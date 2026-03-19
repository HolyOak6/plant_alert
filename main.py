import requests
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()
email_sender = os.getenv("EMAIL_USER") or os.environ["EMAIL_USER"]
email_password = os.getenv("EMAIL_PASS") or os.environ["EMAIL_PASS"]
api_key = os.getenv("API_KEY") or os.environ["API_KEY"]
email_receiver = email_sender  # send to yourself
url = "https://api.openweathermap.org/data/3.0/onecall"

def send_alert():
    msg = EmailMessage()
    msg["Subject"] = "Plant Alert 🌱"
    msg["From"] = email_sender
    msg["To"] = email_receiver
    msg.set_content("Temps are dropping to dangerous levels. Bring your plants in.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(msg)

params = {
    "lat": os.getenv("LATITUDE") or os.environ["LATITUDE"],
    "lon": os.getenv("LONGITUDE") or os.environ["LONGITUDE"],
    "appid": api_key,
    "units": "imperial"
}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    data = None

if data:
    print("data received")
    hourly_data = data["hourly"]
    cold_hours = 0
    current_time = data["current"]["dt"]
    next_24_hours = current_time + (24*60*60)

    for hour in hourly_data:
        if current_time <= hour["dt"] <= next_24_hours:
            if hour["temp"] <= 35:
                cold_hours += 1
                if cold_hours >= 2:
                    send_alert()
                    break
            else:
                cold_hours = 0

else:
    print("Skipping processing due to API failure")
