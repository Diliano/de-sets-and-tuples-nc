# Task 1
# This function takes two arguments and
# should return a tuple containing the arguments


def number_tuple(number1, number2):
    pass


def test_number_tuple():
    assert number_tuple(1, 2) == (1, 2)


# Task 2
# This function takes a tuple and
# should unpack it and return a list
# of the elements

def unpack_tuple(my_tuple):
    pass


def test_unpack_tuple():
    assert unpack_tuple(("Alex", "Windows")) == ["Alex", "Windows"]
    assert unpack_tuple(("Danika", "Linux")) == ["Danika", "Linux"]
    assert unpack_tuple(("Simon", "Mac")) == ["Simon", "Mac"]


#  Task 3
# This function takes a tuple and
# should return the number of times the word "three" appears


def tuple_appearances(my_tuple):
    pass


def test_tuple_appearances():
    assert tuple_appearances((1, 2, 3, 4, 5)) == 0
    assert tuple_appearances(("three", "one", "three", "two", "three",)) == 3
    assert tuple_appearances(("one", 1, "two", 2, "three", 3)) == 1


# Task 4
# This function takes a tuple and
# should return the index of the number 5


def tuple_indexes(my_tuple):
    pass


def test_tuple_indexes():
    assert tuple_indexes((1, 6, 5, 2, 5)) == 2
    assert tuple_indexes(("ooh", 78, "strings", 5, "and", "numbers", 4)) == 3

# Task 5
# This function takes a tuple and
# should return the 2nd to last element using
# negative indexing


def tuple_negative_indexing(my_tuple):
    pass


def test_tuple_negative_indexing():
    assert tuple_negative_indexing((1, 6, 5, 2, 5)) == 2
    assert tuple_negative_indexing(
        ("ooh", 78, "strings", 5, "and", "numbers", 4)) == "numbers"
    assert tuple_negative_indexing(
        ("Wait", "I've", "seen", "this", "before", "somewhere")) == "before"


# Task 6
# This function takes a tuple and
# should return the last 3 elements


def tuple_sections(my_tuple):
    pass


def test_tuple_sections():
    assert tuple_sections((1, 6, 5, 2, 5)) == (5, 2, 5)
    assert tuple_sections(
        ("ooh", 78, "strings", 5, "and", "numbers", 4)) == (
            "and", "numbers", 4)
    assert tuple_sections(
        ("Wait", "I've", "seen", "this", "before", "somewhere")) == (
            "this", "before", "somewhere")


# Task 7
# This function takes a tuple and an other argument and
# should check to see if that arg exists in the tuple
# True - if the element is in the tuple
# False - if the element does not exist

def tuple_is_it_there(my_tuple, element):
    pass


def test_tuple_is_it_there():
    assert tuple_is_it_there((1, 6, 5, 2, 5), 6) == True  # noqa
    assert tuple_is_it_there(
        ("ooh", 78, "strings", 5, "and", "numbers", 4), "Joe is cool") == False  # noqa
    assert tuple_is_it_there(
        (44, 63, 14, 23, 4, 81), 89) == False  # noqa
    assert tuple_is_it_there(
        ("Wait", "I've", "seen", "this", "before", "somewhere"), "Wait") == True  # noqa


# Task 8
# This function takes a multiple arguments and
# should switch the argument values and return them in a tuple
# e.g 1, 2 should switch to and return (2, 1)

def tuple_switcheroo(*args):
    pass


def test_tuple_switcheroo():
    assert tuple_switcheroo(3, 4) == (4, 3)
    assert tuple_switcheroo(5, 1) == (1, 5)
    assert tuple_switcheroo(8, 2) == (2, 8)
