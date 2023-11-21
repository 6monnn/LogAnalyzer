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
            logging.info(f"Timestamp: {log['timestamp']}")
            logging.info(f"Device: {log['device']}")
            logging.info(f"Process: {log['process']}")
            logging.info(f"Message: {log['message']}")
            logging.info("-" * 80)  # Separator line