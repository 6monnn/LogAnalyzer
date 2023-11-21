# log_filter.py

class LogFilter:
    @staticmethod
    def filter_security_critical_logs(logs):
        # Add your filtering rules here based on log severity
        # For example, let's consider logs with severity 'CRITICAL'
        return [log for log in logs if log.get('severity') == 'CRITICAL']
