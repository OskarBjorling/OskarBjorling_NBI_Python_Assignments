def balance_lists(lstA, lstB):
    lstA = list(lstA)
    lstB = list(lstB)

    def move_one(source, destination):
        destination.append(source.pop())

    while len(lstA) >  len(lstB)+1:
        move_one(lstA, lstB)

    while len(lstB) >  len(lstA)+1:
        move_one(lstB, lstA)

    return lstA, lstB


def test_balance_lists():
    a, b = balance_lists([], [])
    assert a == []
    assert b == []

    a, b = balance_lists([1, 2], ["x", "y"])
    assert len(a) == 2
    assert len(b) == 2
    assert len(a) + len(b) == 4

    a, b = balance_lists([1, 2], ["x"])
    assert abs(len(a) - len(b)) <= 1
    assert len(a) + len(b) == 3

    a, b = balance_lists([1, 2, 3], ["x"])
    assert abs(len(a) - len(b)) <= 1
    assert len(a) + len(b) == 4
    assert set(a + b) == {1, 2, 3, "x"}



