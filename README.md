# 🔐 Brute Force Detection Script

## 📌 Overview
This Python script analyzes log files to detect potential brute force attacks by monitoring repeated failed login attempts from the same IP address within a specified time window. If an IP exceeds the threshold of failed attempts, an alert is triggered.

## ✨ Features
- 📜 Parses log files to extract IP addresses and timestamps of failed login attempts.
- 📊 Tracks failed attempts per IP within a defined time window.
- 🚨 Alerts when an IP exceeds the failed attempt threshold.
- 🎨 Color-coded alerts using `colorama` for better visibility (optional).
- 🛠️ Handles file reading errors gracefully.

## 📦 Requirements
- 🐍 Python 3.x
- 🎨 `colorama` (optional, for colored alerts)

To install `colorama`, run:
```bash
pip install colorama
```

## ⚙️ Configuration
The script includes two main configurable parameters:
- `THRESHOLD` (default: `10`): Number of failed attempts within the time window to trigger an alert.
- `TIME_WINDOW` (default: `60` seconds): Time window in seconds to track failed attempts.

You can modify these values in the script:
```python
THRESHOLD = 10  # Number of failed attempts to trigger an alert
TIME_WINDOW = 60  # Time window in seconds to check attempts (1 minute)
```

## 📝 Log Format
The script expects log lines in the following format:
```
YYYY-MM-DD HH:MM:SS <IP_ADDRESS> LOGIN_FAILED
```
Example:
```
2025-04-03 10:00:00 192.168.1.1 LOGIN_FAILED
```

## 🔍 How It Works
1. 📖 Reads the log file line by line.
2. 🔎 Extracts the timestamp and IP address from each log entry.
3. 📊 Tracks failed login attempts within the defined `TIME_WINDOW`.
4. 🚨 If an IP exceeds `THRESHOLD` attempts within the time window, an alert is displayed.
5. 🖥️ Displays the details of the failed attempts.

## ▶️ Usage
Run the script by executing:
```bash
python brute_force_detector.py
```
By default, it analyzes `sample_log.txt`. To specify a different log file, modify the script:
```python
log_file = "your_log_file.txt"
analyze_log_file(log_file)
```

## 🎯 Example Output
```
╔════════════════════════════════════════════════════╗
║ 🚨 ALERT: Possible brute force attack from IP: 192.168.1.1 (10 attempts in 60s) ║
╚════════════════════════════════════════════════════╝
Details of failed attempts:
  🕒 2025-04-03 10:00:00 - 192.168.1.1 LOGIN_FAILED
  🕒 2025-04-03 10:00:05 - 192.168.1.1 LOGIN_FAILED
  ...
```

## ⚠️ Error Handling
- ❌ If the log file is missing, an error message is displayed.
- 🛠️ If an unexpected issue occurs, the script reports the error.

## 📜 License
This script is open-source and available for modification and use under the MIT License.

## 👤 Author
Akshay Kondke
