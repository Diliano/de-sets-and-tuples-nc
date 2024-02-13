import pytest


# Task 1
def create_set(numbers):
    """
    This function should take a list of numbers and convert it to a set
    """
    pass


@pytest.mark.skip()
def test_create_set():
    assert create_set([1, 2, 3, 4]) == {1, 2, 3, 4}
    assert create_set([5, 6, 7, 8]) == {5, 6, 7, 8}
    assert create_set([45, 87, 12, 1]) == {45, 87, 12, 1}
    assert create_set([1, 1, 2, 3, 3]) == {1, 2, 3}


# Task 2
def is_in_set(my_set, element):
    """
    This function should take a set and and element and return the original set
    with the given element added
    """
    pass


@pytest.mark.skip()
def test_is_in_set():
    assert is_in_set({5, 2, 3, 4}, 1) is False
    assert is_in_set({'a', 'b', 'c', 'd'}, 'a') is True


# Task 3
def remove_set_element(my_set):
    """
    This function should take a set, remove an arbitrary element and return
    the removed element
    """
    pass


@pytest.mark.skip()
def test_remove_set_element():
    test_set = {1, 2, 3, 4, 5}
    removed_element = remove_set_element(test_set)

    # Check if the function has returned one of the elements in the set
    assert removed_element in [1, 2, 3, 4, 5]
    # Check if an element has been removed from the set
    assert len(test_set) == 4


# Task 4
def discard_set_element(words):
    """
    This function should take a set and a value. It should remove the
    specified value from the set and return the original set.
    """
    pass


@pytest.mark.skip()
def test_discard_set_element():
    assert discard_set_element(
        {"help", "fix", "my", "code"}, "help") == {"fix", "my", "bug"}

    input = {"I", "bug", "love", "coding"}
    assert discard_set_element(input) is input


# Task 5
def copy_set(my_set):
    """
    This function should take a set and return a *new copy* of that set
    """
    pass


@pytest.mark.skip()
def test_copy_set():
    assert copy_set({1, 2, 3}) == {1, 2, 3}

    # check that the function returns a new set
    input = {1, 2, 3}
    assert copy_set(input) is not input
