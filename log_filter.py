# log_filter.py

class LogFilter:
    @staticmethod
    def filter_logs(logs, severity_levels, process_name):
        print(f"Filtering logs by severity: {severity_levels}, process: {process_name}")
        filtered_logs = [log for log in logs
                         if (not severity_levels or log.get('severity') in severity_levels)
                         and (not process_name or process_name.lower() in log.get('process', '').lower())]
        return filtered_logs
