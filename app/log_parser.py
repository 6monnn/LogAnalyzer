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
        # Assuming log_df has 'status' and 'username' columns
        failed_logins = log_df[log_df['status'] == 'failed']

        # Group by username and count consecutive failed attempts
        failed_attempts = failed_logins.groupby('username')['status'].rolling(window=max_attempts).count()

        # Filter only those that meet or exceed max_attempts
        failed_attempts = failed_attempts[failed_attempts >= max_attempts].reset_index()

        return failed_attempts

