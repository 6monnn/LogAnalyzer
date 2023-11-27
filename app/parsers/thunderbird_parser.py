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
    if 'login failure' in log_entry.get('message', '').lower():
        return {
            'timestamp': log_entry['timestamp'],
            'user': log_entry.get('user', 'Unknown'),
            'status': 'Failed',
            'source': 'Thunderbird',
            'message': log_entry['message']
        }
    return None
