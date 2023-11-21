# log_manager.py

import logging

class LogManager:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def display_logs(self, logs):
        for log in logs:
            logging.info(f"Timestamp: {log['timestamp']}, Device: {log['device']}, Process: {log['process']}, Message: {log['message']}")
