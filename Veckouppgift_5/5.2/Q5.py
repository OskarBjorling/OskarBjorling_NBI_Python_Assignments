def autocomplete_list(input, master_list):
    matches = []

    for name in master_list:
        if name.lower().startswith(input.lower()):
            matches.append(name)

    return matches

def getmasterlist():
    masterlist = []
    masterlist.append("Oskar Björling")
    masterlist.append("Emma Andersson")
    masterlist.append("Liam Svensson")
    masterlist.append("Sara Johansson")
    masterlist.append("Noah Karlsson")
    masterlist.append("Maja Nilsson")
    masterlist.append("Elias Eriksson")
    masterlist.append("Alva Lindberg")
    masterlist.append("Hugo Persson")
    masterlist.append("Elsa Gustafsson")
    return masterlist

def test_autocomplete_list():
    masterlist = getmasterlist()

    assert autocomplete_list("O", masterlist) == ["Oskar Björling"]
    assert autocomplete_list("Em", masterlist) == ["Emma Andersson"]
    assert autocomplete_list("E", masterlist) == ["Emma Andersson", "Elias Eriksson", "Elsa Gustafsson"]
    assert autocomplete_list("X", masterlist) == []
    assert autocomplete_list("", masterlist) == masterlist
    assert autocomplete_list("1", masterlist) == []

    #print("All tests passed")

test_autocomplete_list()

#masterlist = getmasterlist()
#text = input("Search: ")
#(autocomplete_list(text, masterlist))