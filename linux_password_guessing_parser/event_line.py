from enum import Enum

class Attempt_Type(Enum):
    FAILED_LOGIN      = 1
    FAILED_PASSWORD   = 2
    ACCEPTED_PASSWORD = 3

class Event_Type(Enum):
    FAIL_WRONG_USER   = 1
    FAIL_RIGHT_USER   = 2
    SUCCESSFUL_ACCESS = 3

class Event_Line:

  def __init__(self, event_time, machine_ip_address, attempt_type):
    self.event_time         = event_time
    self.machine_ip_address = machine_ip_address
    self.attempt_type = attempt_type
    



class Event_Report:
  def __init__(self, start_line, end_line, event_type):
    self.start_line = start_line
    self.end_line   = end_line
    self.event_type = event_type

  def setEventType(self, event_type):
    self.event_type = event_type