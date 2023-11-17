import re


def parse_log_line(line):
    pattern = r'(\w+ +\d+ \d+:\d+:\d+) (\S+) (\S+): (.+)'
    match = re.match(pattern, line)

    if match:
        return {
            'timestamp': match.group(1),
            'device': match.group(2),
            'process': match.group(3),
            'message': match.group(4)
        }
    else:
        return None

def filter_logs_by_process(logs, process_name):
    return [log for log in logs if process_name in log['process']]

def read_and_parse_log_file(file_path):
    parsed_logs = []
    with open(file_path, 'r') as file:
        for line in file:
            parsed_line = parse_log_line(line.strip())
            if parsed_line:
                parsed_logs.append(parsed_line)
    return parsed_logs

def display_parsed_logs(parsed_logs):
    for log in parsed_logs:
        print(f"Timestamp: {log['timestamp']}, Device: {log['device']}, Process: {log['process']}, Message: {log['message']}")

if __name__ == "__main__":
    log_file_path = '/var/log/syslog'
    process_to_filter = 'wpa_supplicant'

    parsed_logs = read_and_parse_log_file(log_file_path)

    print("Displaying first 5 parsed logs for verification:")
    display_parsed_logs(parsed_logs[:5])

    filtered_logs = filter_logs_by_process(parsed_logs, process_to_filter)
    print("\nDisplaying filtered logs:")
    display_parsed_logs(filtered_logs)
