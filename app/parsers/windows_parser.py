import Evtx.Evtx as evtx
import Evtx.Views as e_views

def parse_windows_event_log(file_path):
    """
    Parses a Windows Event Log file (.evtx) and yields individual event records.
    """
    with evtx.Evtx(file_path) as log:
        for record in log.records():
            yield e_views.xml_records(record.xml())
