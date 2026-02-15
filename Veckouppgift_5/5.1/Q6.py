def muliplication_table(n, limit):

    try:
        n = int(n)
        limit = int(limit)
    except ValueError:
        return []

    if limit <= 0:
        return []

    return [i * n for i in range(1, limit + 1)]

def test_muliplication_table():
    assert muliplication_table(3, 1) == [3]
    assert muliplication_table(3, 4) == [3, 6, 9, 12]
    assert muliplication_table(3, 0) == []
    assert muliplication_table(3, -2) == []
    assert muliplication_table(-2, 3) == [-2, -4, -6]
    assert muliplication_table(0, 4) == [0, 0, 0, 0]

test_muliplication_table()
