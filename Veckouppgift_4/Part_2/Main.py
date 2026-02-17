# 1 Skriv en funktion som tar en sträng som parameter. När den anropas ska den skriva ut strängen och "är en fena på programmering".

def Print_String(name):
    print(name + " är en fena på programmering")

Print_String("David")

# 2a Skriv en funktion med namnet "eko". När den anropas med en sträng ska den upprepa strängen, och skriva ut resultatet.

def eko(str):
    print(str + str)

eko("hej")


#3 Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion och justera den enligt kommentaren.

end = 5
y = 1
for x in range(1, 100):
    y *= 2
    # avsluta loopen med en if-sats här
    if x>=end:
        break
print(y)

# 4 Skriv en funktion med namnet last. Den ska ta en lista som parameter och returnera det sista elementet i listan.
#last([1, 2, 3]) → 3

def last(lst):
    return lst[-1]

print(last([1,2,3,4,5]))

# 5 Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.
# cut_edges([1, 2, 3, 4]) → [2, 3]

def cut_edges(lst):
    return lst[1:-1]

print(cut_edges([1,2,3,4,5]))

# 6 Lös felen i koden.
def increase(x):
    x += 1
    return x

print(increase(1))

# 7 Bygg en funktion med namnet average. Den ska ta parametrar: x och y. Båda ska vara tal. Funktionen ska returnera medelvärdet. Till exempel så räknar man ut medelvärdet av 4 och 8 genom med formeln: (4 + 8) / 2, vilket blir 6.

def average(x,y):
    return (x+y)/2

print(average(10,20))

# 8 Gör en funktion som kan skriva ut innehållet i en lista lite snyggare. Först ska funktionen tala om ifall listan är tom, eller hur många element den har. Sedan ska funktionen skriva ut elementen i en punktlista. Exempel:
# pretty_print(["a", "b", 3.14])
# Listan har 3 element:
# 1. a
# 2. b
# 3. 3.14

def pretty_print(lst):
    if len(lst)==0:
        print("listan är tom")
    else:
        print(f"Listan har {len(lst)} element:")
        for i,element in enumerate(lst,start = 1):
                print(f"{i}. {element}")

pretty_print(["A", "B", 3.14])