def find_Median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    mid = n//2

    if n % 2 == 1:
        return numbers[mid]
    else:
        return (numbers[mid - 1] + numbers[mid])/2

def test_Find_Median():
    assert find_Median([1,2,3,4,5]) == 3
    assert find_Median([1,2,3,4]) == 2.5
    assert find_Median([1]) == 1
    assert find_Median([-0.1, -0.2, -0.3, -0.4]) == -0.25
    assert find_Median([-10, -20, -30, -40]) == -25

