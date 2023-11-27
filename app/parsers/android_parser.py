import re

def parse_android_log_line(log_line):
    """
    Parses a single line of Android logcat output.
    Returns a dictionary with extracted fields.
    """
    log_pattern = r'(\w)/(\w+)\s*\(\s*(\d+)\):\s*(.*)'
    match = re.match(log_pattern, log_line)

    if match:
        return {
            "log_level": match.group(1),
            "tag": match.group(2),
            "pid": int(match.group(3)),
            "message": match.group(4)
        }
    else:
        return None

def android_failed_login(log_entry):
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
    if 'login failed' in log_entry.get('message', '').lower():
        return {
            'timestamp': log_entry['timestamp'],
            'user': log_entry.get('user', 'Unknown'),
            'status': 'Failed',
            'source': 'Android',
            'message': log_entry['message']
        }
    return None
