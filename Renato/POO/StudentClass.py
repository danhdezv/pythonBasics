class Student:
  def __init__(self, name, score):
    self.name = name
    self.score = score
    print(f'Hello {name}')
  def print_details(self):
    print(f'name: {self.name}')
    print(f'score: {self.score}')
