# log_analyzer.py
import pandas as pd


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
