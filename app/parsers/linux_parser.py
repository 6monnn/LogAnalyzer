import re
from datetime import datetime

def parse_linux_log_line(log_line):
    """
    Parses a single line of a Linux log file.
    Returns a dictionary with extracted fields.
    """
    log_pattern = r'(\w+  \d+ \d+:\d+:\d+) (\w+) (\w+): (.*)'
    match = re.match(log_pattern, log_line)

    if match:
        timestamp_str = match.group(1)
        timestamp = datetime.strptime(timestamp_str, '%b %d %H:%M:%S')
        return {
            "timestamp": timestamp,
            "hostname": match.group(2),
            "process": match.group(3),
            "message": match.group(4)
        }
    else:
        return None

def linux_failed_login(log_entry):
    """
    Identifies failed login attempts from a Linux log entry.
    Typical log entries for failed logins include phrases like "Failed password for".
    """
    if 'Failed password for' in log_entry.get('message', ''):
        # Extract the username and IP address from the log message if available
        parts = log_entry['message'].split()
        user_index = parts.index('for') + 1
        user = parts[user_index] if user_index < len(parts) else 'Unknown'
        ip_index = parts.index('from') + 1
        ip = parts[ip_index] if ip_index < len(parts) else 'Unknown IP'

        return {
            'timestamp': log_entry['timestamp'],
            'user': user,
            'status': 'Failed',
            'source': 'Linux',
            'message': f"Failed login for {user} from {ip}"
        }
    return None
