# encoding=utf-8
from pm4py.objects.log.importer.xes import factory as log_factory


def get_set_from_log(elp):
    """
    Extracts all event names from the event log (uses pm4py)
    :param elp: path to the event log
    :return: Set of all event names
    """
    # Get the event log as a data structure from the log importer from pm4py
    event_log = log_factory.apply(elp)
    event_names = []
    for trace in event_log:
        for event in trace:
            event_name = event["concept:name"]
            if event_name not in event_names:
                event_names.append(event_name)
    return event_names
