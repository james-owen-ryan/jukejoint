class ActionSelector(object):
  def __init__(self, id, scale, precondition=lambda person: True):
    self.id = id
    self.scale = scale # (threshold, current position, threshold)
    self.precondition = precondition

class Departure(ActionSelector):
  def __init__(self, scale, precondition=lambda person: True):
    super(Departure, self).__init__('DEPARTURE', scale)
    self.precondition = precondition
    self.signals = (('leave', 1))
    #TODO: symbol weights as a function of where the scale is currently at

  def __str__(self):
    # 'x is thinking about'
    return 'leaving town for a new job'