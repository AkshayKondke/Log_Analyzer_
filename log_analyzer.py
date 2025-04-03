import re
from collections import defaultdict
import time
from datetime import datetime

# Optional: Install colorama for colored output (`pip install colorama`)
try:
    from colorama import init, Fore, Style
    init()  # Initialize colorama for Windows compatibility
    COLOR_AVAILABLE = True
except ImportError:
    COLOR_AVAILABLE = False

# Configuration
THRESHOLD = 10  # Number of failed attempts to trigger an alert
TIME_WINDOW = 60  # Time window in seconds to check attempts (1 minute)

# Dictionary to track attempts: {IP: [(timestamp, log_line), ...]}
attempts = defaultdict(list)

def parse_log_line(line):
    """Extract IP and timestamp from a log line using regex."""
    # Example log format: "2025-04-03 10:00:00 192.168.1.1 LOGIN_FAILED"
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\d+\.\d+\.\d+\.\d+) (LOGIN_FAILED)"
    match = re.search(pattern, line)
    if match:
        timestamp_str, ip, status = match.groups()
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return ip, timestamp
    return None, None

def check_brute_force(ip, timestamp, log_line):
    """Check if the IP has exceeded the threshold for failed attempts."""
    attempts[ip].append((timestamp, log_line))
    current_time = timestamp
    recent_attempts = [
        t for t in attempts[ip]
        if (current_time - t[0]).total_seconds() <= TIME_WINDOW
    ]
    attempts[ip] = recent_attempts

    if len(recent_attempts) >= THRESHOLD:
        alert(ip, recent_attempts)
        attempts[ip].clear()

def alert(ip, attempt_list):
    """Send a clear, optimized alert about a potential brute force attack."""
    # Summary line
    summary = f"Possible brute force attack from IP: {ip} ({len(attempt_list)} attempts in {TIME_WINDOW}s)"
    
    # Colorized output if colorama is available
    if COLOR_AVAILABLE:
        print(f"{Fore.RED}╔════════════════════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.RED}║ ALERT: {summary:<42} ║{Style.RESET_ALL}")
        print(f"{Fore.RED}╚════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    else:
        print("╔════════════════════════════════════════════════════╗")
        print(f"║ ALERT: {summary:<42} ║")
        print("╚════════════════════════════════════════════════════╝")

    # Detailed log entries
    print("Details of failed attempts:")
    for timestamp, log_line in attempt_list:
        print(f"  {timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {log_line.strip()}")

def analyze_log_file(file_path):
    """Read and analyze the log file line by line."""
    print(f"Starting log analysis on {file_path}...")
    try:
        with open(file_path, 'r') as file:
            for line in file:
                ip, timestamp = parse_log_line(line)
                if ip and timestamp:
                    check_brute_force(ip, timestamp, line)
                time.sleep(0.1)  # Simulate real-time (remove in live use)
        print("Log analysis completed.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    log_file = "sample_log.txt"
    analyze_log_file(log_file)