class ActionSelector(object):
  def __init__(self, id, scale, precondition=lambda person: True):
    self.id = id
    self.scale = scale # (threshold, current position, threshold)
    self.precondition = precondition

class QuitJob(ActionSelector):
  def __init__(self, scale, precondition=lambda person: person.occupation):
    super(QuitJob, self).__init__('QUIT JOB', scale)
    self.precondition = precondition
    self.signals = (('work', 2), ('job', 2), ('quit', 2))
    #TODO: symbol weights as a function of where the scale is currently at

  def __str__(self):
    # 'x is thinking about'
    return 'quitting their job'