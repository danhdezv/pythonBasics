class Antenna(object):
    color = ''
    longitude = ''

class Hair(object):
    color = ''
    texture = ''

class Eye(object):
    shape = ''
    color = ''
    size = ''

class Parent(object):
    color = ''
    size = ''
    aspect = ''
    antennas = Antenna()
    eyes = Eye()
    hair = Hair()

    def floatAction(self):
      print('I\'m floating!')


class OtherParent(object):
    color = ''
    size = ''
    aspect = ''
    antennas = Antenna()
    eyes = Eye()
    hair = Hair()

    def flyAction(self):
      print('I\'m flying!')

class NewObj(Parent, OtherParent):
    pass

myNewObj = NewObj()
myNewObj.floatAction()
myNewObj.flyAction()