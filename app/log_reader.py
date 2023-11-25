import logging

class LogReader:
    @staticmethod
    def read_log_file(file_path, log_parser):
        parsed_logs = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    parsed_line = log_parser.parse_log_line(line.strip())
                    if parsed_line:
                        parsed_logs.append(parsed_line)
        except FileNotFoundError as e:
            logging.error(f"File not found: {file_path}")
            raise LogReaderError(f"File not found: {file_path}") from e
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise LogReaderError(f"An error occurred: {e}") from e
        return parsed_logs

class LogReaderError(Exception):
    pass
