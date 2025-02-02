def isPrime(n):
    '''
    Checks for a prime number.<br>
    Input - `n`, any integer <br>
    Output - boolean value
    '''
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1


    if c==0 and n!=1:
        return 1
    else:
        return 0

###############################

def sum(a,b):
    '''
    Adds to numbers
    input: a, b - two numbers
    output: returns sum
    '''
    c=a+b
    return c

###############################

def difference(a,b):
   '''
   subtracts two numbers
   input: a, b - two numbers
   output: returns difference
   '''
   c=a-b
   return c

###############################

def Fibonacci_Series(n):
    # base case
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (Fibonacci_Series(n-2) + Fibonacci_Series(n-1))

###############################

def MultiplyTwoNumbers(a,b):
    """
    multiplying two numbers
    input: a,b - two numbers
    output: returns multiplication
    """
    c = a*b
    return c

###############################

def MultiplyList(myList):
    """
    multiplying the numbers in list
    input: list
    output: returns the multiplication
            of numbers in given list
    """
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

################################




