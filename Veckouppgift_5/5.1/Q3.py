# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
def count_vowels(word):
    Vovels ="aeiouyåäö"
    count = 0
    for ch in word.lower():
        if ch in Vovels:
                count += 1
    return count

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0
    assert count_vowels("") == 0
    assert count_vowels("A") > 0
    assert count_vowels("aeio1 uyåäö") != 0
    assert count_vowels("a") != 0
    assert count_vowels("a") == 1
    assert count_vowels("aq1i") == 2


