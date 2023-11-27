import re

def parse_thunderbird_log_line(log_line):
    """
    Parses a single line of Thunderbird log.
    Returns a dictionary with extracted fields, or None if the line doesn't match a known pattern.
    """
    log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3})\s+(.*?):\s+(.*)'
    match = re.match(log_pattern, log_line)

    if match:
        return {
            "timestamp": match.group(1),
            "module": match.group(2),
            "message": match.group(3)
        }
    else:
        return None

def thunderbird_failed_login(log_entry):
    """
    Detects a failed login attempt in a Thunderbird log entry.

    Args:
    log_entry (dict): A dictionary representing a log entry from Thunderbird.

    Returns:
    dict: A dictionary containing details of the failed login attempt, or None if no failed login is detected.

    Example:
    >>> log_entry = {
        'timestamp': '2023-04-01 12:34:56',
        'message': 'Login failure: user johndoe',
        'user': 'johndoe'
    }
    >>> thunderbird_failed_login(log_entry)
    {'timestamp': '2023-04-01 12:34:56', 'user': 'johndoe', 'status': 'Failed', 'source': 'Thunderbird', 'message': 'Login failure: user johndoe'}
    """
    if 'login failure' in log_entry.get('message', '').lower():
        return {
            'timestamp': log_entry['timestamp'],
            'user': log_entry.get('user', 'Unknown'),
            'status': 'Failed',
            'source': 'Thunderbird',
            'message': log_entry['message']
        }
    return None
