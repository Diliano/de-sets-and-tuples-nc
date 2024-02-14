import pytest


#  Task 1
def check_common_values(set_1, set_2):
    """
    This function should take two sets and check if they have any elements in
        common.
    - If they DO share any common elements then the function should return True
    - If they DON'T share any common elements then the function should return
        False
    """
    pass


@pytest.mark.skip()
def test_check_common_values():
    assert check_common_values({1, 2, 3}, {2, 3, 4}) is True
    assert check_common_values({"a", "b", "c"}, {"x", "y", "z"}) is False


# Task 2
def check_subset(set_1, set_2):
    """
    This function should take two sets, set_1 and set_2, if set_2 is a
    *subset* of set_1 then the function should return true.

    A subset is a set made up of values contained in the set it is being
    compared to.
    E.g.
    {3,4} is a *subset* of {1,2,3,4,5}
    """
    pass


@pytest.mark.skip()
def test_check_subset():
    assert check_subset({'a', 'b', 'c'}, {'a'}) is True
    assert check_subset({1, 2, 3}, {5, 6}) is False


# Task 3
def check_superset(set_1, set_2):
    """
    This function should take two sets, set_1 and set_2, if set_2 is a
    *superset* of set_1 then the function should return true.

    A superset is a set that includes all the values contained in the set
    it is being compared to.
    E.g.
    {1,2,3,4,5} is a *superset* of {3,4}
    """
    pass


@pytest.mark.skip()
def test_check_superset():
    assert check_superset({1, 2}, {1, 2, 3, 4, 5}) is True
    assert check_superset({1, 2, 3, 4, 5}, {1, 2, 3}) is False
    assert check_superset({'a', 'b', 'c'}, {1, 2, 3}) is False


# Task 4
def find_set_differences(set_1, set_2):
    """
    This function should take two sets, set_1 and set_2.

    It should return a set containing all the elements of set_1 that aren't
    in set_2 AND all the elements of set_2 that aren't in set_1.
    """
    pass


@pytest.mark.skip()
def test_find_set_differences():
    assert find_set_differences(
        {"laptop", "phone", "glasses", "lunch"},
        {"phone", "keys", "wallet", "lunch"}
    ) == {"wallet", "laptop", "keys", "glasses"}
    assert find_set_differences(
        {1, 2, 3, 4, 5}, {5, 6, 7, 1}) == {2, 3, 4, 6, 7}
    assert find_set_differences(
        {1, 2, 3, "data", 4, 5},
        {"we", 3, "love", 2, "data"}
    ) == {1, 4, 5, "love", "we"}


# Task 5
def create_union(set_1, set_2):
    """
    This function should create a *union* of set_1 and set_2. A union will
    have all the values of of both sets. There will be no duplicates.
    """
    pass


@pytest.mark.skip()
def test_create_union():
    assert create_union({"laptop", "phone", "glasses", "lunch"},
                        {"phone", "keys", "wallet", "lunch"}
                        ) == {
        "phone", "glasses", "lunch",
        "wallet", "laptop", "keys"
    }
    assert create_union({1, 2, 3, 4, 5}, {5, 6, 7, 1}) == {1, 2, 3, 4, 5, 6, 7}
    assert create_union(
        {1, 2, 3, "data", 4, 5},
        {"we", 3, "love", 2, "data"}
    ) == {
        1, 2, 3, 4, 5, "we", "love", "data"
    }


# Task 6
def create_intersection(set_1, set_2):
    """
    This function should create an *intersection* of set_1 and set_2. An
    intersection will have contain all the values that are present in
    BOTH sets.
    """
    pass


@pytest.mark.skip()
def test_create_intersection():
    assert create_intersection(
        {"laptop", "phone", "glasses", "lunch"},
        {"phone", "keys", "wallet", "lunch"}
    ) == {"phone", "lunch"}
    assert create_intersection({1, 2, 3, 4, 5}, {5, 6, 7, 1}) == {1, 5}
    assert create_intersection(
        {1, 2, 3, "data", 4, 5}, {"we", 3, "love", 2, "data"}
    ) == {2, 3, "data"}
