import pytest
# Task 1
# This function should take a list of numbers and
# return a set of the same numbers
def create_set(numbers):
    pass

@pytest.mark.skip()
def test_create_set():
    assert create_set([1, 2, 3, 4]) == {1, 2, 3, 4}
    assert create_set([5, 6, 7, 8]) == {5, 6, 7, 8}
    assert create_set([45, 87, 12, 1]) == {45, 87, 12, 1}

# Task 2
# This function should take a list of numbers and
# return a set of numbers with the number 1 added

def add_set(numbers):
    pass


@pytest.mark.skip()
def test_add_set():
    assert add_set([5, 2, 3, 4]) == {5, 2, 3, 4, 1}
    assert add_set([5, 6, 7, 8]) == {5, 6, 7, 8, 1}
    assert add_set([9, 10, 11, 12]) == {9, 10, 11, 12, 1}

# Task 3
# This function should take a list of words and
# should return a set with the word "pillow" removed


def remove_word(words):
    pass


@pytest.mark.skip()
def test_remove_word():
    assert remove_word(["hello", "pillow", "world"]) == {"hello", "world"}
    assert remove_word(["I", "love", "pillow", "coding"]) == {
        "I", "love", "coding"
    }
    assert remove_word(["pillow", "pillows", "pill", "pudding"]) == {
        "pillows", "pill", "pudding"
    }


# Task 4
# This function should take a set of words and
# should remove all elements, returning the same set


def remove_all_words(words):
    pass

@pytest.mark.skip()
def test_remove_all_words():
    # Tests that an empty set is returned
    assert remove_all_words({"help", "fix", "my", "bug", "code"}) == set()
    # Tests that the input set is mutated and returned
    input = {"I", "bug", "love", "coding"}
    assert remove_all_words(input) is input
    assert input == set()


# Task 5
#  This function takes multiple sets and
# should return one set containing all the data


def merge_sets(*args):
    pass


@pytest.mark.skip()
def test_merge_sets():
    assert merge_sets(
        {1, 2, 3, 4, 5},
        {6, 7, 8, 9, 10},
        {11, 12, 13, 14, 15},
    ) == {
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15
    }
    assert merge_sets(
        {"let", "me", "tell", "you", "a", "story"},
        {"once", "upon", "a", "time", "there"},
        {"oh", "i'm", "out", "of", "space"},
    ) == {
        "let", "me", "tell", "you", "a", "story",
        "once", "upon", "a", "time", "there",
        "oh", "i'm", "out", "of", "space"
    }
    assert merge_sets(
        {"help", "fix", "my", "bug", "code"},
        {1, 2, 3, 4, 5},
        {"sets", "are", "so", "great"}
    ) == {
        "help", "fix", "my", "bug", "code",
        1, 2, 3, 4, 5,
        "sets", "are", "so", "great"
    }

# Task 6
#  This function should take a set and
# should return an ordered list in reverse


def reverse_list(my_set):
    pass

@pytest.mark.skip()
def test_reverse_list():
    assert reverse_list({1, 2, 3, 4, 5}) == [5, 4, 3, 2, 1]
    assert reverse_list({"Hello", "world"}) == ["world", "Hello"]
    assert reverse_list({"clever", "is", "this", "well"}) == [
        "well", "this", "is", "clever"
    ]

# Task 7
# This function takes a list with duplicates and
# should return a set with no duplicates


def duplicate_list(your_list):
    pass

@pytest.mark.skip()
def test_duplicate_list():
    assert duplicate_list([1, 1, 2, 3, 3]) == {1, 2, 3}
    assert duplicate_list(["hey", "hiya", "hiya", "hello", "hey"]) == {
        "hey", "hiya", "hello"
    }
    assert duplicate_list(["hey", 1, 1, 4, "boo", "hey"]) == {
        "hey", 1, 4, "boo"
    }
