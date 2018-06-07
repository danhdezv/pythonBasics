

heigth = int( input("N: ") )
 
while  ( str (heigth).isnumeric()  ):
    while heigth > 0:
        print("*"*heigth )
        heigth -= 1
    heigth = int( input("Nw: ")   )

