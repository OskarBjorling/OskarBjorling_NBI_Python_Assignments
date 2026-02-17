#2a
class Djur:
    def __init__(self, namn, late):
        self.namn = namn
        self.late = late

    def make_noise(self):
        print(f"{self.namn} säger: {self.late}")

hund = Djur("Hund", "Voff!")
katt = Djur("Katt", "Mjau!")
tupp = Djur("Tupp", "Kukkeliku!")
ko = Djur("Ko", "Muu!")

djur_lista = [hund, katt, ko, tupp]

for djur in djur_lista:
    djur.make_noise()


#2b
class Country:
    def __init__(self, name, pop, area=None, *languages):
        self.name = name
        self.pop = pop
        self.area=area
        self.languages = list(languages)


    def add_language(self, *languages):
        self.languages.extend(languages)

    def print_info(self):
        if self.area != None:
            print(f"I {self.name} bor det {self.pop} miljoner invånare på {self.area} kvadratkilometer")
        else:
            print(f"I {self.name} bor det {self.pop} miljoner invånare")
        if len(self.languages)>0:
            if len(self.languages)==1:
                språk_text = self.languages[0]
            else:
                språk_text = ", ".join(self.languages[:-1]) + " & " + self.languages[-1]
            print(f"I {self.name} talar man: {språk_text}")

se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)
dk = Country("Danmark", 6.0)
i = Country("Island", 3.8)
ch= Country("Schweiz", 5.5)
list_countries = [se, no, i, dk, ch]

#for country in list_countries:
#    country.print_info()

se.add_language("Svenska")
ch.add_language("Tyska", "Schweizertyska", "Franska")
ch.add_language("Rätromananska")
se.add_language("Samiska")


#se.print_info()
#ch.print_info()
for country in list_countries:
    country.print_info()