from datetime import datetime

def event_is_passed(event):
  return event.event_date.replace(tzinfo=None) < datetime.now().replace(tzinfo=None)