def main():
    fizzbuzz(2, 144)

def fizzbuzz(start: int, end: int):
    """
    Prints out all numbers in range start to end while appending 'fizz' to
    perfect squares, 'buzz' to prime numbers, and 'fizzbuzz' to numbers that 
    are both perfect squares and prime numbers.
    """
    for num in range(start, end + 1):
        perfect_square = is_perfect_square(num)
        prime = is_prime(num)
        
        if perfect_square and prime:
            print(f'{num} fizzbuzz')
        elif perfect_square:
            print(f'{num} fizz')
        elif prime:
            print(f'{num} buzz')
        else:
            print(num)
    

def is_perfect_square(num: int) -> bool:
    """
    Determine whether num is a perfect square or not
    """
    pass


def is_prime(num: int) -> bool:
    """
    Determine whether num is a prime number or not
    """
    pass


if __name__ == '__main__': 
    main()