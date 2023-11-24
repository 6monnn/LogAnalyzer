# log_manager.py

import logging

class LogManager:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def display_logs(self, logs):
        if not logs:
            logging.info("No logs to display.")
            return

        logging.info("Displaying logs:")
        logging.info("-" * 80)  # Separator line

        for log in logs:
            # Replace f-strings with format method
            logging.info("Timestamp: {}".format(log['timestamp']))
            logging.info("Device: {}".format(log['device']))
            logging.info("Process: {}".format(log['process']))
            logging.info("Message: {}".format(log['message']))
            logging.info(f"Severity: {log.get('severity', 'N/A')}")  
            logging.info("-" * 80)  # Separator line
