import logging

class LogManager:
    """
    LogManager is responsible for configuring the logging settings and displaying logs.
    It uses Python's built-in logging module to manage log output.
    """
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def display_logs(self, logs):
        """
        Displays the given logs with formatting.

        Each log entry is expected to be a dictionary containing keys like timestamp, device,
        process, message, and optional severity. The logs are displayed in a formatted manner
        for easy reading.

        :param logs: A list of log dictionaries to be displayed.
        """
        if not logs:
            logging.info("No logs to display.")
            return

        logging.info("Displaying logs:")
        logging.info("-" * 80)

        for log in logs:
            logging.info("Timestamp: {}".format(log['timestamp']))
            logging.info("Device: {}".format(log['device']))
            logging.info("Process: {}".format(log['process']))
            logging.info("Message: {}".format(log['message']))
            logging.info(f"Severity: {log.get('severity', 'N/A')}")  
            logging.info("-" * 80)
