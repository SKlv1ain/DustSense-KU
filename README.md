# DustSense KU - Real-time Air Quality Monitoring System

DustSense KU is a web-based air quality monitoring and health advisory system that collects and analyzes environmental data including PM2.5, PM10, humidity, temperature, and wind speed. The data is sourced from physical sensors (KidBright board) and an external weather API (Open-Meteo). The system provides a live dashboard, historical data analysis, health recommendations, and a RESTful API.

---

## 🌍 Project Overview

Air pollution, especially dust particles (PM2.5 and PM10), can severely impact respiratory health. This project collects and analyzes real-time environmental data to:
- Predict air quality
- Assess its potential health effects
- Recommend outdoor safety precautions

---

## 🔌 Sensor Hardware

- **PMS7003** – Dust sensor (PM2.5, PM10)
- **KY-015** – Humidity sensor
- **Temperature sensor** – Integrated on KidBright board

---

## 🌐 External API

- **Wind Speed Data**: Fetched from [Open-Meteo API](https://open-meteo.com)

---

## 🧠 Features

- Live AQI and environmental conditions
- Risk-level-based Health Advisory with animation icons
- Historical Data Visualization using Chart.js
- Statistics page with data insights
- Theme toggle (Dark/Light mode)
- RESTful API for external use:
  - `/api/latest/` – Get latest environmental data
  - `/api/health-advisory/` – Get current air quality risk level
  - `/api/recommendation/` – Get health-based recommendations

---

## 🖥️ Getting Started

Follow these steps to set up and run the DustSense KU project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/DustSense-KU.git
cd DustSense-KU
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # MacOS/Linux
.venv\Scripts\activate     # Windows
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)

If using custom API keys or database settings, create a `.env` file and set the necessary variables.

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to access the dashboard.

---

## 📂 Project Structure
```plaintext
DustSense-KU/
├── air/                  
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       ├── home.html
│       ├── statistics.html
├── DustSenseKU/       
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── settings.py
│   ├── urls.py
├── static/               
├── db.sqlite3            
└── manage.py
```

---
## 🙌 Contributions

Contributions are welcome! Feel free to fork the repository, submit pull requests, or raise issues to help improve the system.

## 📜 License

This project is licensed under the MIT License.
