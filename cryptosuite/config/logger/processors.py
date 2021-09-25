from datetime import datetime


def add_timestamp(_, __, event_dict):
    event_dict["timestamp"] = datetime.now()
    return event_dict

