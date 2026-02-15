# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet
def find_2nd_max(list):
    Max_Value = None
    Second_Max_Value = None

    for value in list:
        try:
            value = float(value)
        except (ValueError, TypeError):
            continue

        if Max_Value is None:
                Max_Value = value
        elif Max_Value <= value:
            Second_Max_Value = Max_Value
            Max_Value = value
        elif Second_Max_Value == None or Second_Max_Value < value:
            Second_Max_Value = value

    return Second_Max_Value

def test_find_second_max():
    assert find_2nd_max([1,2,3,4,5,10]) == 5
    assert find_2nd_max([1,2,3,4,5]) == 4
    assert find_2nd_max([-1, -2, -3, -4, -5]) == -2
    assert find_2nd_max([0, -2, -3, -4, -5]) == -2
    assert find_2nd_max(["2A", "1", -3, -4, -5]) == -3
    assert find_2nd_max([5,5,1]) == 5
    assert find_2nd_max([1]) == None