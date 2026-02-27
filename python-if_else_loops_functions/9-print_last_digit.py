#!/usr/bin/python3
def print_last_digit(number):
    """Prints the last digit of a number and returns it"""
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last

# Example usage
if __name__ == "__main__":
    r1 = print_last_digit(98)    
    r2 = print_last_digit(0)     
    r3 = print_last_digit(-1024) 
    print(r3)                    