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