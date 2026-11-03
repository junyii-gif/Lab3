import Lab3

print("Test_Lab3")


# REQ-01
def test_bubble_sort_ascending_nine_numbers():
    input_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

# REQ-02
def test_bubble_sort_descending_nine_numbers():
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

# REQ-03: exactly 10 numbers -> 1
def test_bubble_sort_ten_numbers():
    input_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 1)

# REQ-03: more than 10 numbers -> 1
def test_bubble_sort_more_than_ten_numbers():
    input_arr = [15, 3, 8, 1, 12, 7, 4, 10, 2, 9, 6]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 1)

# REQ-04: 0 numbers -> 0
def test_bubble_sort_empty():
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 0)

# REQ-05: non-integer string -> 2
def test_bubble_sort_non_integer_string():
    input_arr = [64, 34, "abc", 12]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 2)

# REQ-05: float -> 2
def test_bubble_sort_non_integer_float():
    input_arr = [64, 34, 2.5, 12]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 2)