import re

def parse_openssh_log_line(log_line):
    """
    Parses a single line of OpenSSH log.
    Returns a dictionary with extracted fields, or None if the line doesn't match.
    """
    ssh_pattern = r'(\w+ \d+ \d+:\d+:\d+) \w+ sshd\[\d+\]: (Failed|Accepted) password for (\w+) from (\d+\.\d+\.\d+\.\d+) port \d+ ssh2'
    match = re.match(ssh_pattern, log_line)

    if match:
        return {
            "timestamp": match.group(1),
            "auth_result": match.group(2),
            "username": match.group(3),
            "ip_address": match.group(4)
        }
    else:
        return None

def openssh_failed_login(log_entry):
    """
    Detects a failed login attempt in an OpenSSH log entry.

    Args:
    log_entry (dict): A dictionary representing a log entry from OpenSSH.

    Returns:
    dict: A dictionary containing details of the failed login attempt, or None if no failed login is detected.

    Example:
    >>> log_entry = {
        'timestamp': '2023-04-01 12:34:56',
        'message': 'Failed password for invalid user johndoe from 192.168.1.1 port 22 ssh2',
        'user': 'johndoe'
    }
    >>> openssh_failed_login(log_entry)
    {'timestamp': '2023-04-01 12:34:56', 'user': 'johndoe', 'status': 'Failed', 'source': 'OpenSSH', 'message': 'Failed password for invalid user johndoe from 192.168.1.1 port 22 ssh2'}
    """
    if 'Failed password for' in log_entry.get('message', ''):
        return {
            'timestamp': log_entry['timestamp'],
            'user': log_entry.get('user', 'Unknown'),
            'status': 'Failed',
            'source': 'OpenSSH',
            'message': log_entry['message']
        }
    return None
