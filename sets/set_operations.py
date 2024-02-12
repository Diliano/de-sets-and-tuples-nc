import pytest
#  Task 1
# This function takes multiple sets and
# should return a union of the sets


def sets_union(my_set, your_set):
    pass

def test_sets_union():
    assert sets_union({"laptop", "phone", "glasses", "lunch"},
                      {"phone", "keys", "wallet", "lunch"}
                      ) == {
                          "phone", "glasses", "lunch",
                          "wallet", "laptop", "keys"
    }
    assert sets_union({1, 2, 3, 4, 5}, {5, 6, 7, 1}) == {1, 2, 3, 4, 5, 6, 7}
    assert sets_union(
        {1, 2, 3, "data", 4, 5},
        {"we", 3, "love", 2, "data"}
    ) == {
        1, 2, 3, 4, 5, "we", "love", "data"
    }


# Task 2
# This functions takes two sets and
# should return an intersection of the data in a set


def intersect_sets(my_set, your_set):
    pass

@pytest.mark.skip()
def test_intersect_sets():
    assert intersect_sets({"laptop", "phone", "glasses", "lunch"},
                          {"phone", "keys", "wallet", "lunch"}
                          ) == {"phone", "lunch"}
    assert intersect_sets({1, 2, 3, 4, 5}, {5, 6, 7, 1}) == {1, 5}
    assert intersect_sets(
        {1, 2, 3, "data", 4, 5},
        {"we", 3, "love", 2, "data"}
    ) == {2, 3, "data"}


# Task 3
# This function takes two sets and
# should return the items that are in the first set
# but not in the second set


def different_sets(my_set, your_set):
    pass

@pytest.mark.skip()
def test_different_sets():
    assert different_sets({"laptop", "phone", "glasses", "lunch"},
                          {"phone", "keys", "wallet", "lunch"}
                          ) == {"laptop", "glasses"}
    assert different_sets({1, 2, 3, 4, 5}, {5, 6, 7, 1}) == {2, 3, 4}
    assert different_sets(
        {1, 2, 3, "data", 4, 5},
        {"we", 3, "love", 2, "data"}
    ) == {1, 4, 5}


# Task 4
# This function takes two arguments and
# should return the elements that are not in both sets


def not_in_both_sets(my_set, your_set):
    pass

@pytest.mark.skip()
def test_not_in_both_sets():
    assert not_in_both_sets({"laptop", "phone", "glasses", "lunch"},
                            {"phone", "keys", "wallet", "lunch"}
                            ) == {"wallet", "laptop", "keys", "glasses"}
    assert not_in_both_sets({1, 2, 3, 4, 5}, {5, 6, 7, 1}) == {2, 3, 4, 6, 7}
    assert not_in_both_sets(
        {1, 2, 3, "data", 4, 5},
        {"we", 3, "love", 2, "data"}
    ) == {1, 4, 5, "love", "we"}
