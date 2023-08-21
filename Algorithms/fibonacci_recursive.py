def fibonacci_rec(number):
    if number < 2:
        return number
    else:
        return fibonacci_rec(number-1)+ fibonacci_rec(number-2)
        print(fibonacci_rec(number-1)+fibonacci(number-2))
print(fibonacci_rec(8))
