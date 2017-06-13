def fizz_buzz(param):
    """The FizzBuzz Challenge"""

    # Return FizzBuzz if param is divisible by both 3 and 5
    if param % 3 == 0 and param % 5 == 0:
        return "FizzBuzz"
    # Return Fizz if param is divisible by both 3
    elif param % 3 == 0:
        return "Fizz"
    # Return Buzz if param is divisible by 5
    elif param % 5 == 0:
        return "Buzz"
    else:
    # Return param if param is not divisible by 3 or 5
        return param
