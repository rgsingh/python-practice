import sys

import pytest

from src.general.python_tips_day1 import *

print(sys.path)


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def names():
    return ['Alice', 'Bob', 'Charlie']


@pytest.fixture
def filename(tmp_path):
    filepath = tmp_path / 'test_file.txt'
    with open(filepath, 'w') as file:
        file.write('Test data')
    return str(filepath)


def test_list_comprehension_with_predicate(numbers):
    assert list_comprehension_with_predicate(numbers, lambda x: x % 2 == 0) == [2, 4]


def test_list_comprehension(numbers):
    assert list_comprehension(numbers) == [2, 4]


def test_enumerate_example(names):
    assert enumerate_example(names) == [(0, 'Alice'), (1, 'Bob'), (2, 'Charlie')]


def test_generator_expression():
    gen = generator_expression()
    assert next(gen) == 1
    assert next(gen) == 4


def test_dictionary_comprehension():
    assert dictionary_comprehension() == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


def test_unpacking_sequences():
    assert unpacking_sequences() == ("John", "Doe")


def test_extended_unpacking():
    assert extended_unpacking() == (1, [2, 3, 4, 5])


def test_multiple_assignments():
    assert multiple_assignments() == (1, 2, 3)


def test_say_hello(capsys):
    say_hello()
    captured = capsys.readouterr()
    assert captured.out == "Something is happening before the function is called.\nHello!\nSomething is happening after the function is called.\n"


def test_context_manager_example(filename):
    assert context_manager_example(filename) == 'Test data'


def test_zip_function(names):
    assert zip_function(names, [25, 30, 35]) == ['Alice is 25 years old.', 'Bob is 30 years old.',
                                                 'Charlie is 35 years old.']


def test_greet():
    assert greet('Alice') == 'Hello, Alice'


def test_slots():
    obj = MyClass()
    obj.attribute1 = 'value1'
    obj.attribute2 = 'value2'
    assert obj.attribute1 == 'value1'
    assert obj.attribute2 == 'value2'

    with pytest.raises(TypeError):
        obj.attribute1['new-key'] = 'new-value'

    with pytest.raises(TypeError):
        obj.attribute2['new-nested-key'] = 'new-nested-value'

    with pytest.raises(AttributeError):
        obj.new_attribute = 'new_value'


def test_slots_with_complex_types():
    obj = MyClass()
    obj.complex_attribute1 = {'some-key': 'some-value'}
    obj.complex_attribute2 = {'some-nested-key':  'some-nested-value'}

    assert obj.complex_attribute1 == {'some-key': 'some-value'}
    assert obj.complex_attribute2 == {'some-nested-key': 'some-nested-value'}




