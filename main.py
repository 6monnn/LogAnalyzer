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
    parser.add_argument('--show_critical', action='store_true', help='Display only critical logs')
    args = parser.parse_args()

    log_file_path = args.log_file
    show_critical_logs = args.show_critical

    log_parser = LogParser(log_line_pattern)
    log_analyzer = LogAnalyzer()
    log_manager = LogManager()
    log_reader = LogReader()
    log_filter = LogFilter()

    parsed_logs = log_reader.read_log_file(log_file_path, log_parser)

    log_manager.display_logs(parsed_logs[:5])

    # Apply security-critical log filtering rule if --show_critical argument is provided
    if show_critical_logs:
        security_critical_logs = log_filter.filter_security_critical_logs(parsed_logs)
        log_manager.display_logs(security_critical_logs)
    else:
        log_manager.display_logs(parsed_logs)
