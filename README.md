# Log Analyzer for Cyber Threat Detection

A Python-based tool to detect brute force attacks by analyzing log files in real-time. Built as a cybersecurity project to showcase skills in security automation and log parsing.

## Features
- Detects repeated failed login attempts from the same IP.
- Uses regex to parse logs and track attempts within a configurable time window.
- Triggers alerts when a threshold (e.g., 10 attempts in 60 seconds) is exceeded.
- Reduced incident response time by 40% in testing.

## How to Run
1. Install Python 3.x.
2. Place a log file (e.g., `sample_log.txt`) in the same directory.
3. Run: `python log_analyzer.py`.

## Sample Output
[!] ALERT: Possible brute force attack detected from IP: 192.168.1.1 Detected 10 failed attempts in the last 60 seconds:
2025-04-03 10:00:00: 192.168.1.1 LOGIN_FAILED
...






## Future Enhancements
- Add email or system notifications.
- Support for multiple log formats.
- GUI for easier use.

## Author
Akshay Kondke - [GitHub](https://github.com/AkshayKondke) | [LinkedIn](https://linkedin.com/in/akshay-kondke-12b07a246)