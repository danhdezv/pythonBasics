# Listas

""" 
  El usuario tendra que introducir valores numericos, los cuales se almacenarán para después sacar el promedio 
  y mostrarlo cuando el valor introducido NO sea numerico

  input > 5
  input > 6
  input > 7
  input > 8
  input > 's'
  output > 'promedio: 6.5'

"""
myList = []
while True:
  num = input('')
  if num.isnumeric():
     myList.append(int(num))
  else:
    break
prom = sum(myList) / len(myList)
print(f'Promedio: {prom}')