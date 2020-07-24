from time import sleep

class MockManager: 
  def update_light(self, color, mode):
    print(color)
    print("displaying mode %s" % mode)
    sleep(1)