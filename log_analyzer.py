# log_analyzer.py

class LogAnalyzer:
    @staticmethod
    def filter_logs_by_process(logs, process_name):
        return [log for log in logs if process_name in log['process']]
