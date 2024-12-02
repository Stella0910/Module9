def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, result):
            if result % i != 0:
                return f'Простое\n{result}\n'
            else:
                return f'Составное\n{result}\n'
    return wrapper


@is_prime
def sum_three(first, second, third):
    sum_of_three = first + second + third
    return sum_of_three


result = sum_three(2, 3, 6)
print(result)

result = sum_three(2, 3, 1)
print(result)