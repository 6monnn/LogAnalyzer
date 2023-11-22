# main.py

import argparse
from log_parser import LogParser
from log_analyzer import LogAnalyzer
from log_manager import LogManager
from log_reader import LogReader
from log_filter import LogFilter

if __name__ == "__main__":
    log_line_pattern = r'(\w+ +\d+ \d+:\d+:\d+) (\S+) (\S+): (.+)'

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Parse and filter logs.')
    parser.add_argument('--log_file', default='/var/log/syslog', help='Path to the log file')
    parser.add_argument('--severity', nargs='+', default=[], help='Specify severity levels to display')
    parser.add_argument('--process', default='', help='Specify process name to filter logs')
    args = parser.parse_args()

    log_file_path = args.log_file
    severity_levels = args.severity
    process_name = args.process

    log_parser = LogParser(log_line_pattern)
    log_analyzer = LogAnalyzer()
    log_manager = LogManager()
    log_reader = LogReader()
    log_filter = LogFilter()

    parsed_logs = log_reader.read_log_file(log_file_path, log_parser)

    # Apply log filtering rules based on specified severity levels and process name
    if severity_levels or process_name:
        filtered_logs = log_filter.filter_logs(parsed_logs, severity_levels, process_name)
        log_manager.display_logs(filtered_logs)
    else:
        log_manager.display_logs(parsed_logs)
