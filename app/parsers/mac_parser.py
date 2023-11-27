import re

def parse_macos_log_line(log_line):
    """
    Parses a single line of macOS log output.
    Returns a dictionary with extracted fields.
    """
    log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}) (\w+): \[(.*?)\] \[(.*?)\] (.*)'
    match = re.match(log_pattern, log_line)

    if match:
        return {
            "timestamp": match.group(1),
            "log_level": match.group(2),
            "subsystem": match.group(3),
            "process": match.group(4),
            "message": match.group(5)
        }
    else:
        return None

def macos_failed_login(log_entry):
    """
    Detects a failed login attempt in a macOS log entry.

    Args:
    log_entry (dict): A dictionary representing a log entry from macOS.

    Returns:
    dict: A dictionary containing details of the failed login attempt, or None if no failed login is detected.

    Example:
    >>> log_entry = {
        'timestamp': '2023-04-01 12:34:56',
        'message': 'User authentication failed',
        'user': 'johndoe'
    }
    >>> macos_failed_login(log_entry)
    {'timestamp': '2023-04-01 12:34:56', 'user': 'johndoe', 'status': 'Failed', 'source': 'macOS', 'message': 'User authentication failed'}
    """
    if 'authentication failed' in log_entry.get('message', '').lower():
        return {
            'timestamp': log_entry['timestamp'],
            'user': log_entry.get('user', 'Unknown'),
            'status': 'Failed',
            'source': 'macOS',
            'message': log_entry['message']
        }
    return None
