def is_sorted_ascending(numbers):
    sorted_numbers = sorted(numbers)
    if sorted_numbers == numbers:
        return True
    else:
        return False

def test_is_sorted_ascending():
    assert is_sorted_ascending([1, 2, 3, 4, 5]) == True
    assert is_sorted_ascending([2, 1, 3, 4, 5]) == False
    assert is_sorted_ascending([-3, -2, 0, 0, 10]) == True
    assert is_sorted_ascending([3, -2, 0, 0, 10]) == False
    assert is_sorted_ascending([]) == True

test_is_sorted_ascending()