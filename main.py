# main.py

import argparse
from log_parser import LogParser
from log_analyzer import LogAnalyzer
from log_manager import LogManager
from log_reader import LogReader

if __name__ == "__main__":
    log_line_pattern = r'(\w+ +\d+ \d+:\d+:\d+) (\S+) (\S+): (.+)'

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Parse and filter logs.')
    parser.add_argument('--log_file', default='/var/log/syslog', help='Path to the log file')
    parser.add_argument('--process_name', default='wpa_supplicant', help='Process name to filter logs')
    args = parser.parse_args()

    log_file_path = args.log_file
    process_to_filter = args.process_name

    log_parser = LogParser(log_line_pattern)
    log_analyzer = LogAnalyzer()
    log_manager = LogManager()
    log_reader = LogReader()

    parsed_logs = log_reader.read_log_file(log_file_path, log_parser)

    log_manager.display_logs(parsed_logs[:5])

    filtered_logs = log_analyzer.filter_logs_by_process(parsed_logs, process_to_filter)
    log_manager.display_logs(filtered_logs)
