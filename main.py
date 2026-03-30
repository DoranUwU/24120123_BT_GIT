
def print_hi(name):

    print(f'Hello {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    print_hi('Github')

