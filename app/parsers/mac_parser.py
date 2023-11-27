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
