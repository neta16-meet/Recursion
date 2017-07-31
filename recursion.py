def factorial(n):
    '''
    The factorial of a number is the result of multiplying a sequence of descending
    natural numbers down to 1.
    Example:
    5! = 1 x 2 x 3 x 4 x 5 = 120

    Write a recursive function that takes a number n and returns the factorial
    of that number.
    '''

def pow(num, p):
    '''
    Write a recursive function that takes a number num and a number p,
    and returns the result of num to the power of p (num ** p).
    
    Example:
    pow(5, 3) = 125
    '''

def fib(n):
    '''
    The fibonacci series is a series of numbers, starting with 0 and 1, where each number's 
    value is the sum of the two previous numbers in the series:
    0, 1, 1, 2, 3, 5, 8, 13, 21.....

    Write a recursive function that takes a number n, representing an index
    in the fibonacci series, and returns the value of the number in
    the series with the specific index.
    '''

def hanoiTowers(discNum, fromPole, withPole, toPole):
    '''
    The game "Towers of Hanoi" uses three poles. A number of discs
    is stacked in decreasing order from the bottom to the top of one
    pole, i.e. the largest disc at the bottom and the smallest one on top.

    The aim of the game is to move the tower of discs from one pole to another pole. 

    The following rules have to be obeyed:
    1. Only one disc may be moved at a time.
    2. Only the most upper disc from one of the poles can be moved in a move
    3. It can be put on another pole, if this pole is empty or if the most upper
       disc of this pole is larger than the one which is moved.

    Write a recursive function that recieves an attribute discNum, and prints the series
    of moves required to move the discs from one pole to another, using three
    poles: one which has the discs at the beginning- fromPole, one which is used
    mainly to assist- withPole, and one which the discs should be moved to- toPole.

    Animation of this process can be seen here: http://towersofhanoi.info/Animate.aspx
    '''

def reverse(q):
    '''
    Write a *recursive* function that takes a queue q and reverses the order 
    of the values in the same queue, without using any other data structures.

    Example:
    q ----> 1 -> 2 -> 3 -> 4
    after function:
    q ----> 4 -> 3 -> 2 -> 1
    '''
