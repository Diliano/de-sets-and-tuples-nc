import pytest


# Task 1
def create_tuple(arg1, arg2):
    """
    This function takes two arguments and should return a tuple
        containing the arguments
    """
    pass


def test_create_tuple():
    assert create_tuple(1, 2) == (1, 2)
    assert create_tuple('a', 'b') == ('a', 'b')
    assert create_tuple([1, 2, 3], [4, 5, 6]) == ([1, 2, 3], [4, 5, 6])


# Task 2
def tuple_to_list(my_tuple):
    """
    This function should convert the given tuple to a list
    """
    pass


@pytest.mark.skip()
def test_tuple_to_list():
    assert tuple_to_list(("Alex", "Windows")) == ["Alex", "Windows"]
    assert tuple_to_list(("Danika", "Linux")) == ["Danika", "Linux"]
    assert tuple_to_list(("Simon", "Mac")) == ["Simon", "Mac"]


#  Task 3
def count_threes(my_tuple):
    """
    This function should return the number of times the word "three" appears
        in the given tuple
    """
    pass


@pytest.mark.skip()
def test_count_threes():
    assert count_threes((1, 2, 3, 4, 5)) == 0
    assert count_threes(("three", "one", "three", "two", "three",)) == 3
    assert count_threes(("one", 1, "two", 2, "three", 3)) == 1


# Task 4
def get_index_of_five(my_tuple):
    """
    This function takes a tuple and should return the index of the number 5
    """
    pass


@pytest.mark.skip()
def test_get_index_of_five():
    assert get_index_of_five((1, 6, 5, 2, 5)) == 2
    assert get_index_of_five(
        ("ooh", 78, "strings", 5, "and", "numbers", 4)) == 3


# Task 5
def get_second_to_last_element(my_tuple):
    """
    This function takes a tuple and should return the 2nd to last element
    """
    pass


@pytest.mark.skip()
def test_get_second_to_last_element():
    assert get_second_to_last_element((1, 6, 5, 2, 5)) == 2
    assert get_second_to_last_element(
        ("ooh", 78, "strings", 5, "and", "numbers", 4)) == "numbers"
    assert get_second_to_last_element(
        ("Wait", "I've", "seen", "this", "before", "somewhere")) == "before"


# Task 6
def get_last_three_elements(my_tuple):
    """
    This function should return the final 3 elements of the given tuple
    """
    pass


@pytest.mark.skip()
def test_get_last_three_elements():
    assert get_last_three_elements((1, 6, 5, 2, 5)) == (5, 2, 5)
    assert get_last_three_elements(
        ("ooh", 78, "strings", 5, "and", "numbers", 4)) == (
            "and", "numbers", 4)
    assert get_last_three_elements(
        ("Wait", "I've", "seen", "this", "before", "somewhere")) == (
            "this", "before", "somewhere")


# Task 7
def check_element_is_present(my_tuple, element):
    """
    This function should take two arguments, a tuple and a value.
    It should check if the value is present in the tuple and return a boolean.
    True - if the element is present in the tuple
    False - if the element is NOT present in the tuple
    """
    pass


@pytest.mark.skip()
def test_check_element_is_present():
    assert check_element_is_present((1, 6, 5, 2, 5), 6) is True
    assert check_element_is_present(
        ("ooh", 78, "strings", 5, "and", "numbers", 4), "Joe is cool") is False
    assert check_element_is_present((44, 63, 14, 23, 4, 81), 89) is False
    assert check_element_is_present(
        ("Wait", "I've", "seen", "this", "before", "somewhere"),
        "Wait") is True


# Task 8
def tuple_switcheroo(*args):
    """
    This function should take any number of arguments and return the given
        arguments in a tuple. However the order of the arguments should be
        reversed.

    E.g: tuple_switcheroo(1,2,3) should return (3,2,1)
    """
    pass


@pytest.mark.skip()
def test_tuple_switcheroo():
    assert tuple_switcheroo(3, 4) == (4, 3)
    assert tuple_switcheroo(5, 4, 3, 2, 1) == (1, 2, 3, 4, 5)
    assert tuple_switcheroo('a', 'c', 'b') == ('b', 'c', 'a')
