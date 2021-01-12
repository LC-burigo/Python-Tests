from time import time

fibonacci_cache = dict()


def fibonacci_memo(input_value):
    if input_value in fibonacci_cache:
        return fibonacci_cache[input_value]
    if input_value == 1:
        value = 1
    elif input_value == 2:
        value = 1
    elif input_value > 2:
        value = fibonacci_memo(input_value - 1) + fibonacci_memo(input_value - 2)
    fibonacci_cache[input_value] = value
    return fibonacci_cache[input_value]


for i in range(1, 101):
    print("fib({}) = ".format(i), fibonacci_memo(i))


def fibonacci(n):
    t1 = 0
    t2 = 1
    cont = 3
    while cont <= n:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        cont += 1
    return t2


print(fibonacci(1))


def GridTraveler(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1
    return GridTraveler(m - 1, n) + GridTraveler(m, n - 1)


start = time()
print(GridTraveler(1, 1))
end = time()
print(end - start)

GridTraveler_cache = {}


def GridTraveler_new(m, n):
    key = '{},{}'.format(m,n)
    if key in GridTraveler_cache:
        return GridTraveler_cache[key]
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1
    value = GridTraveler_new(m - 1, n) + GridTraveler_new(m, n - 1)
    GridTraveler_cache[key] = value
    return value


start = time()
print(GridTraveler_new(15, 15))
end = time()
print(end - start)