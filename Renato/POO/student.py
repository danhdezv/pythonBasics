class Student(object):
  def __init__(self, name, score):
    self.name = name
    self.score = score
    print(f'Hello {name}')
  def print_details(self):
    print(f'name: {self.name}')
    print(f'score: {self.score}')

student1 = Student('Fulano', [99, 55, 100])
student2 = Student('Perengano', [30, 65, 100])

student1.print_details()
student2.print_details()
