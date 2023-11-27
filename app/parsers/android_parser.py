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
    if 'login failed' in log_entry.get('message', '').lower():
        return {
            'timestamp': log_entry['timestamp'],
            'user': log_entry.get('user', 'Unknown'),
            'status': 'Failed',
            'source': 'Android',
            'message': log_entry['message']
        }
    return None
