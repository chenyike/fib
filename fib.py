#author - Yike Chen

def F(n):
    '''Function for generating fib sequence'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1)+F(n-2)

def is_prime_number(x):
    '''Check if the number is prime or not'''
    if x == 2:
        return True
    elif x > 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
            else:
                return True
    else:
        return False

def outPut(i):
    '''Do the outPut'''
    if F(i)%3 == 0:
        return "Buzz"
    elif F(i)%5 == 0:
        return "Fizz"
    elif is_prime_number(F(i)):
        return "FizzBuzz"
    else:
        return F(i)

def main():
    '''main function handling output'''
    number = raw_input("How many Fib number do we want? ")
    n = int(number)
    for i in range(0,n):
        print outPut(i)


if __name__ == '__main__':
    main()
