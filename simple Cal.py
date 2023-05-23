
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print (logo)

# Add
def add (n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1 , n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2



operations_dic = {
    "*": multiply,
    "+": add,
    "/": divide,
    "-": subtract,
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for i in operations_dic:
            print(i)



    flag = True

    while flag == True:
        operations_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number?: "))
        function= operations_dic[operations_symbol]
        result = function(num1,num2)

        print(f"{num1} {operations_symbol} {num2} = {result}")

        keep_doing = input("Type 'y' to calculating with 8, or type 'n' to restart: " ).lower()

        if keep_doing == "y":
            num1 = result
          
        elif keep_doing == "n":
            flag = False
            calculator()


calculator()