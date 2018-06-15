class Subject:
  def __init__(self, name, score):
    self.name = name
    self.score = score

class Student:
  def __init__(self, name, subjects):
    self.name = name
    self.subjects = []
    print(f'Hello {name}')
    for key, value in subjects.items():
        self.subjects.append(Subject(key, value))
  
  def print_details(self):
    print(f'name: {self.name}')
    for subject in self.subjects:
      print(f'{subject.name}: {subject.score}')

  def getAverage(self):
    pass
    #return sum(self.score) / len(self.score)
