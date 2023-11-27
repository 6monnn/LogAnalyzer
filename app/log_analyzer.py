# log_analyzer.py
import pandas as pd
from collections import defaultdict
from datetime import datetime, timedelta



class LogAnalyzer:
    @staticmethod
    def filter_logs_by_process(logs, process_name):
        return [log for log in logs if process_name in log['process']]


    def detect_spikes(log_df, threshold):
        """
        Detects spikes in log activity.

        Parameters:
        - log_df (DataFrame): DataFrame containing log data.
        - threshold (int): The threshold for flagging a spike.

        Returns:
        - spikes (DataFrame): DataFrame containing information about detected spikes.
        """
        # Assuming log_df has a 'timestamp' column
        log_df['timestamp'] = pd.to_datetime(log_df['timestamp'])
        log_df.set_index('timestamp', inplace=True)

        # Resample log data to hourly (or another appropriate frequency)
        frequency = log_df.resample('H').count()

        # Detect spikes
        mean = frequency.mean()[0]
        std_dev = frequency.std()[0]
        spikes = frequency[frequency > mean + threshold * std_dev]

        return spikes


class FailedLoginDetector:
    def __init__(self, threshold_count=5, threshold_time=10):
        """
        threshold_count: Number of failed attempts to trigger an alert.
        threshold_time: Time window in minutes for failed attempt count.
        """
        self.threshold_count = threshold_count
        self.threshold_time = threshold_time
        self.attempt_records = defaultdict(list)

    def process_log_entry(self, log_entry):
        """
        Process a single log entry.
        log_entry should be a dictionary with at least 'timestamp', 'user', and 'status' keys.
        """
        if self._is_failed_attempt(log_entry):
            self._record_attempt(log_entry['user'], log_entry['timestamp'])

            if self._is_repeated_attempt(log_entry['user']):
                print(f"Alert: Repeated failed login attempts for user {log_entry['user']}")

    def _is_failed_attempt(self, log_entry):
        """
        Determines if a log entry is a failed login attempt.
        This function needs to be customized based on the actual log format.
        """

        if 'status' in log_entry and log_entry['status'] == 'Failed':
            return True

        if 'message' in log_entry and 'Failed password for' in log_entry['message']:
            return True

        return False


    def _record_attempt(self, user, timestamp):
        # Remove old attempts outside the threshold time window
        cutoff_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S') - timedelta(minutes=self.threshold_time)
        self.attempt_records[user] = [t for t in self.attempt_records[user] if t > cutoff_time]
        
        # Record the new attempt
        self.attempt_records[user].append(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S'))

    def _is_repeated_attempt(self, user):
        # Check if the number of attempts exceeds the threshold
        return len(self.attempt_records[user]) >= self.threshold_count
