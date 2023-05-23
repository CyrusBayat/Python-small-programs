

def prime_checker(number):
    check = True
    for i in range(2,number):
        if number % i ==0:
            check=False
    if check == True:
        print(f"{number} Is a prime number")
    else:
        print(f"{number} Not a prime number")
        


num = int(input("Check this number: "))

prime_checker(number = num)