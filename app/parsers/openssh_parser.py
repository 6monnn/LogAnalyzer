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
