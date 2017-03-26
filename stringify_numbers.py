digits = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
          6: "six", 7: "seven", 8: "eight", 9: "nine"}

exceptions = {10: "ten", 11: "eleven", 12: "twelve", 14: "fourteen",
              2: "twen", 3: "thir", 4: "for", 5: "fif", 8: "eigh"}


def print_number():
    """Print out the strings of integers from 1 to 99"""

    for num in range(1, 10):
        print digits[num]

    for num in range(10, 20):
        if num in exceptions:
            print exceptions[num]
        elif num % 10 in exceptions:
            print exceptions[num % 10] + "teen"
        else:
            print digits[num % 10] + "teen"

    for num in range(20, 100):
        if num/10 in exceptions:
            tens = exceptions[num/10]
        else:
            tens = digits[num/10]

        ones = digits[num % 10]
        print tens + "ty" + ones


print_number()
