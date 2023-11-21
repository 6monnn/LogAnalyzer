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
                'message': match.group(4)
            }
        else:
            return None
