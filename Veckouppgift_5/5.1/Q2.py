# 2 Det har smugit sig in kommentarer i stället för kod på några ställen.Skriv färdigt testfallen test_empty_list och test_number_list.

# Returnerar summan av alla tal i listan
def sum_list(lst):
   tot=0
   for num in lst:
        tot = tot + num
   return tot


def test_empty_list():
    expected =  0
    actual = sum_list([])
    assert actual == expected


def test_numtest_number_list():
    # TODO: testa med listor som har ett, två respektive fem element.
    assert sum_list([5]) == 5
    assert sum_list([5,5]) ==10
    assert sum_list([5,5,10,2,3]) ==25