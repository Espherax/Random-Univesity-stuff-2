def Menu():
    """Menu function"""
    print ("""************
Calculator
************
Menu
1) Addition
2) Substraction
3) Multiplication
4) Division
5) Exit""")
def Calculator():
    """Mathematic operations"""
    Menu()
    opc = int(input("Select an option\n"))
    while (opc >0 and opc <5):
        x = int(input("Type your first number\n"))
        y = int(input("Type your second number\n"))
        if (opc==1):
            print ("The result is:", x+y)
            opc = int(input("Select an option\n"))
        elif(opc==2):
            print ("The result is:",x-y)
            opc = int(input("Select an option\n"))
        elif(opc==3):
            print ("The result is:",x*y)
            opc = int(input("Selecione Opcion\n"))
        elif(opc==4):
            try:
                print ("The result is:", float(x)/y)
                opc = int(input("Select an option\n"))
            except ZeroDivisionError:
                print ("You cannot divide by zero!")
                opc = int(input("Select an option\n"))


Calculator()
