import Evtx.Evtx as evtx
import Evtx.Views as e_views

def parse_windows_event_log(file_path):
    """
    Parses a Windows Event Log file (.evtx) and yields individual event records.
    """
    with evtx.Evtx(file_path) as log:
        for record in log.records():
            yield e_views.xml_records(record.xml())

def windows_event_failed_login(log_entry):
    """
    Detects a failed login attempt in a Windows Event log entry, specifically for event ID 4625.

    Args:
    log_entry (dict): A dictionary representing a log entry from Windows Event Logs.

    Returns:
    dict: A dictionary containing details of the failed login attempt, or None if no failed login is detected.

    Example:
    >>> log_entry = {
        'timestamp': '2023-04-01 12:34:56',
        'event_id': 4625,
        'user': 'johndoe'
    }
    >>> windows_event_failed_login(log_entry)
    {'timestamp': '2023-04-01 12:34:56', 'user': 'johndoe', 'status': 'Failed', 'source': 'WindowsEvent', 'message': 'Failed login for johndoe'}
    """
    if log_entry.get('event_id') == 4625:
        return {
            'timestamp': log_entry['timestamp'],
            'user': log_entry.get('user', 'Unknown'),
            'status': 'Failed',
            'source': 'WindowsEvent',
            'message': f"Failed login for {log_entry.get('user', 'Unknown')}"
        }
    return None
