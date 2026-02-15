# 4 Formulera testfall för en funktion som hittar största talet i en lista.
#   Returnerar det största talet i listan
#   Returnerar None om det inte finns något


def find_max(list):
    x = None
    for value in list:
        try:
            value=float(value)
        except (ValueError, TypeError):
            continue

        if x is None or x < value:
            x = value

    return x

def test_find_max():
    assert find_max([1,2,3,4,5,10]) == 10
    assert find_max([1,2,3,4,5]) == 5
    assert find_max([-1, -2, -3, -4, -5]) == -1
    assert find_max([0, -2, -3, -4, -5]) == 0
    assert find_max(["2A", "1", -3, -4, -5]) == 1
    assert find_max([]) == None