class LogFilter:
    """
    LogFilter is a utility class that provides functionalities for filtering log entries.
    It offers methods to filter logs based on specified criteria such as severity levels 
    and process names.
    """
    @staticmethod
    def filter_logs(logs, severity_levels, process_name):
        """
        Filters a list of log entries based on severity levels and process name.

        :param logs: A list of log entries, where each entry is a dictionary.
        :param severity_levels: A list of severity levels to include in the filter.
                                If empty or None, all severity levels are included.
        :param process_name: The name of the process to filter the logs by.
                             If empty or None, logs from all processes are included.
        :return: A list of filtered log entries that match the specified criteria.
        """
        filtered_logs = [log for log in logs
                         if (not severity_levels or log.get('severity') in severity_levels)
                         and (not process_name or process_name.lower() in log.get('process', '').lower())]
        return filtered_logs
