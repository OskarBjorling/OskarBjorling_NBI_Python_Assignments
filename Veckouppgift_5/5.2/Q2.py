def Word_Count(string):
    words = string.split()
    return len(words)

def test_Word_Count():
    assert Word_Count("Hello World")==2
    assert Word_Count(" A A  ") == 2
    assert Word_Count(" AA ") == 1
    assert Word_Count("AA") == 1
    assert Word_Count("   ") == 0
    assert Word_Count(" ") == 0
    assert Word_Count(" 1 1 ") == 2

