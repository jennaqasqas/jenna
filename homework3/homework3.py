def say_goodbye(name):
    print("Goodbye, ", name)

def say_area(radius):
    area = 3.14 * (radius ^ 2)
    print(area)

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def get_min_max(temps):
    return (min(temps), max(temps))

def is_weekend(day):
    if day == "6" or day == "7":
        return True
    else:
        return False
    
def optimal_car(distance, fuel):
    fuel_efficiency = distance / fuel
    return fuel_efficiency

def encrypt(num):
    last_digit = num % 10
    remaining = num // 10
    multiplier = 10 ** len(str(remaining))

    return last_digit * multiplier + remaining

def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result


def minimum(set):
    minim = set[0]
    for i in set:
        if i < minim:
            minim = i
    return minim


def maximum(set):
    maxi = set[0]
    for i in set:
        if i > maxi:
            maxi = i
    return maxi

def find_min(set):

    i = 0
    minimum = set[0]

    while i < len(set):
        if set[i] < minimum:
            minimum = set[i]
        i += 1

    return minimum

def find_max(set):

    i = 0
    maximum = set[0]

    while i < len(set):
        if set[i] > maximum:
            maximum = set[i]
        i += 1

    return maximum


def sum_of_digits(int):
    sum = 0
    while int > 0:
        digit = int % 10
        sum += digit
        int //= 10
    return sum

x = 2
y = 8
result = power(x, y) #2 to the power of 8
print(f"The result of Oski stole your power (5.1) with x = {x} and y = {y} is {result}.")

