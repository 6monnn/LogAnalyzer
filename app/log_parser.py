# log_parser.py

import re

class LogParser:
    """
    LogParser is a class designed to parse log lines based on a specified pattern.
    It can extract key information from each log line and categorize it into structured data.
    """
    def __init__(self, log_line_pattern):
        self.log_line_pattern = log_line_pattern

    def parse_log_line(self, line):
        """
        Parses a single log line using the defined pattern and extracts key information.

        :param line: A string representing a single line from a log file.
        :return: A dictionary with parsed log data (timestamp, device, process, message, severity)
                 or None if the line does not match the pattern.
        """
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
        """
        Extracts the severity level from a log message.

        :param message: The log message string.
        :return: The extracted severity as a string, or None if not found.
        """
        match = re.search(r'\[([A-Za-z]+)\]', message)
        return match.group(1).upper() if match else None
    
    def detect_failed_logins(log_df, max_attempts):
        """
        Detects repeated failed login attempts.

        Parameters:
        - log_df (DataFrame): DataFrame containing log data.
        - max_attempts (int): The maximum number of allowed consecutive failed attempts.

        Returns:
        - failed_attempts (DataFrame): DataFrame containing information about failed login attempts.
        """
        failed_logins = log_df[log_df['status'] == 'failed']

        failed_attempts = failed_logins.groupby('username')['status'].rolling(window=max_attempts).count()

        failed_attempts = failed_attempts[failed_attempts >= max_attempts].reset_index()

        return failed_attempts

