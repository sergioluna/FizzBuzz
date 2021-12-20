import math

def main():
    fizzbuzz(2, 144)


def fizzbuzz(start: int, end: int):
    """
    Prints out all numbers from start to end while appending 'fizz' to
    perfect squares, 'buzz' to prime numbers, and 'fizzbuzz' to numbers that 
    are perfect squares where the square-root is a prime number.
    """
    for num in range(start, end + 1):
        perfect_square = is_perfect_square(num)
        prime = is_prime(num)
        
        if perfect_square and is_prime(math.isqrt(num)):
            print(f'{num} fizzbuzz')
        elif perfect_square:
            print(f'{num} fizz')
        elif prime:
            print(f'{num} buzz')
        else:
            print(num)
    

def is_perfect_square(num: int) -> bool:
    """
    Returns True if num is a perfect square, False otherwise
    """
    # math.isqrt() returns floor of exact square root of num
    return (math.isqrt(num) ** 2 == num) 


def is_prime(num: int) -> bool:
    """
    Returns True if num is prime, False otherwise
    """
    if num <= 1:
        return False
    else:
        # iterate through relevant factors to check if num is divisible
        for factor in range(2, math.isqrt(num) + 1):
            if num % factor == 0:
                return False
        return True


if __name__ == '__main__': 
    main()