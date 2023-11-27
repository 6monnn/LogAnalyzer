import re

def parse_apache_log_line(log_line):
    """
    Parses a single line of Apache log in Combined Log Format.
    Returns a dictionary with extracted fields.
    """
    log_pattern = r'(\d+\.\d+\.\d+\.\d+) - (.*?) \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"'
    match = re.match(log_pattern, log_line)
    
    if match:
        return {
            "ip": match.group(1),
            "identity": match.group(2),
            "timestamp": match.group(3),
            "request": match.group(4),
            "status": int(match.group(5)),
            "size": int(match.group(6)),
            "referer": match.group(7),
            "user_agent": match.group(8)
        }
    else:
        return None
    
def apache_failed_login(log_entry):
    """
    Detects a failed login attempt in an Android log entry.

    Args:
    log_entry (dict): A dictionary representing a log entry from Android.

    Returns:
    dict: A dictionary containing details of the failed login attempt, or None if no failed login is detected.

    Example:
    >>> log_entry = {
        'timestamp': '2023-04-01 12:34:56',
        'message': 'User login failed',
        'user': 'johndoe'
    }
    >>> android_failed_login(log_entry)
    {'timestamp': '2023-04-01 12:34:56', 'user': 'johndoe', 'status': 'Failed', 'source': 'Android', 'message': 'User login failed'}
    """
    if log_entry.get('status') in [401, 403]:
        return {
            'timestamp': log_entry['timestamp'],
            'user': log_entry.get('user', 'Unknown'),
            'status': 'Failed',
            'source': 'Apache',
            'message': f"Failed login for {log_entry.get('user', 'Unknown')} from {log_entry['ip']}"
        }
    return None
