
# list comprehension that takes a predicate in the second parameter
# and returns a list of elements that satisfy the predicate
# e.g. list_comprehension([1, 2, 3, 4, 5], lambda x: x % 2 == 0) -> [2, 4]
def list_comprehension_with_predicate(numbers, predicate):
    return [num for num in numbers if predicate(num)]


def list_comprehension(numbers):
    return [num for num in numbers if num % 2 == 0]


def enumerate_example(names):
    result = []
    for index, name in enumerate(names):
        result.append((index, name))
    return result


def generator_expression():
    return (x * x for x in range(1, 1001))


def dictionary_comprehension():
    return {x: x * x for x in range(1, 11)}


def unpacking_sequences():
    first_name, last_name = ("John", "Doe")
    return first_name, last_name


def extended_unpacking():
    first, *rest = [1, 2, 3, 4, 5]
    return first, rest


def multiple_assignments():
    x, y, z = 1, 2, 3
    return x, y, z


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


def context_manager_example(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data


def zip_function(names, ages):
    result = []
    for name, age in zip(names, ages):
        result.append(f"{name} is {age} years old.")
    return result


def greet(name: str) -> str:
    return f"Hello, {name}"


class MyClass:
    __slots__ = ['attribute1', 'attribute2', 'complex_attribute1', 'complex_attribute2']
