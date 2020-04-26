class State:
  def __init__(self):
    self.on = True
    self.status = 'idle'

  def set_status(self, status):
    self.status = status

  def get_status(self):
    return self.status