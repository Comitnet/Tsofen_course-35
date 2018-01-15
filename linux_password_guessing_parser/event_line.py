from enum import Enum

class Attempt_Type(Enum):
    FAILED_PASSWORD = 1
    ACCEPTED_PASSWORD = 2

class event_line:

  def __init__(self, event_time, machine_ip_address, attempt_type):
    self.event_time = event_time
    self.machine_ip_address = machine_ip_address
    if attempt_type == "Failed password":
      self.attempt_type = Attempt_Type.FAILED_PASSWORD
    elif attempt_type == "Accepted password":
      self.attempt_type = Attempt_Type.ACCEPTED_PASSWORD
    