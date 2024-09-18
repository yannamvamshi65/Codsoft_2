try:
    operand1=int(input("enter 1st number:\n"))
    operand2=int(input("enter 2nd number:\n"))
    choice=int(input("Select the operation to perform:(Enter the choice number)\n1.+\n2.-\n3.*\n4./\n5.%\n"))
    match choice:
        case 1:
            print(operand1+operand2)
        case 2 :
            print(operand1 - operand2)
        case 3:
            print(operand1 * operand2)
        case 4:
            print(operand1 / operand2)
        case 5:
            print(operand1 % operand2)
except Exception as e:
    print("\"Please Enter only \'INTEGER\' values\"\n",e)

