# log_parser.py

import re

class LogParser:
    def __init__(self, log_line_pattern):
        self.log_line_pattern = log_line_pattern

    def parse_log_line(self, line):
        match = re.match(self.log_line_pattern, line)
        if match:
            return {
                'timestamp': match.group(1),
                'device': match.group(2),
                'process': match.group(3),
                'message': match.group(4),
                'severity': self.extract_severity(match.group(4))
            }
        else:
            return None

    @staticmethod
    def extract_severity(message):
        # Implement logic to extract severity from the log message
        # For example, let's assume the severity is in square brackets, like "[CRITICAL]"
        match = re.search(r'\[([A-Z]+)\]', message)
        return match.group(1) if match else None
