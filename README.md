# 🌱 Plant Cold Alert System

## Overview
This project is an automated weather monitoring system that alerts me when temperatures are expected to drop to levels that could damage my plants.

It uses the OpenWeatherMap API to fetch hourly forecast data, analyzes upcoming temperature trends, and sends an email alert if sustained cold conditions are detected.

---

## Problem
Succulents and other plants can tolerate brief cold exposure, but sustained low temperatures (near freezing) can cause damage or death.

Manually checking the weather daily is inefficient and unreliable.

---

## Solution
This script:
- Pulls hourly weather forecast data
- Checks the next 24 hours
- Detects **2+ consecutive hours below 35°F**
- Sends an email alert if dangerous conditions are found

---

## Features
- 🌡️ Uses real-time weather API data
- ⏱️ Filters for the next 24 hours only
- ❄️ Detects sustained cold exposure (not just brief dips)
- 📧 Sends automated email alerts via Gmail SMTP
- 🔁 Runs automatically using GitHub Actions (daily schedule)
- 🔐 Uses environment variables for secure credential handling

---

## Tech Stack
- Python
- requests (API calls)
- smtplib (email sending)
- python-dotenv (local environment variables)
- GitHub Actions (automation)

---

## How It Works
1. Fetch weather data from OpenWeatherMap API
2. Extract hourly forecast data
3. Filter timestamps within the next 24 hours
4. Track consecutive hours below 35°F
5. Trigger alert if threshold is met

---

## Environment Variables

Create a `.env` file locally with:
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
API_KEY=your_openweather_api_key
LATITUDE=your_lat
LONGITUDE=your_lon


⚠️ `.env` is ignored via `.gitignore` and should never be committed.

For GitHub Actions, these values are stored as repository secrets.

---

## Automation

This project uses GitHub Actions to run daily on a schedule.

- Runs once per day
- No local machine required
- Fully cloud-based execution

---

## Future Improvements
- Add retry logic for API failures
- Improve alert logic (duration weighting, thresholds per plant type)
- Add SMS notifications (Twilio or similar)
- Support multiple locations
- Logging and monitoring

---

## Key Takeaways
This project demonstrates:
- API integration
- Data parsing and filtering
- Real-world conditional logic
- Automation and scheduling
- Secure handling of credentials

---

## Author
Michael
