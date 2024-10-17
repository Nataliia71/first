import math
import statistics
# vysledek = math.ceil(3.1)
# print(vysledek)

# vysledek = math.floor(3.9)
# print(vysledek)
# prumer = statistics.mean([2,3,4,5])
# print(prumer)

# cislo = float (input("Zadejte cislo:"))
# vysledek = math.ceil(cislo)
# print(vysledek)
# vysledek = math.floor(cislo)
# print(vysledek)
# vysledek = round(cislo,0)
# print(vysledek)


# school_report = [
#     ["Český jazyk", 1],
#     ["Anglický jazyk", 1],
#     ["Matematika", 1],
#     ["Přírodopis", 2],
#     ["Dějepis", 1],
#     ["Fyzika", 2],
#     ["Hudební výchova", 4],
#     ["Výtvarná výchova", 2],
#     ["Tělesná výchova", 3],
#     ["Chemie", 4],
# ]

# votes = [
#     "curling", 
#     "vánoční svařák na trzích", 
#     "vánoční svařák na trzích", 
#     "curling", 
#     "zážitková první pomoc",
#     "curling", 
#     "zážitková první pomoc",
#     "curling",
#     "zážitková první pomoc",
#     ]
# winner = statistics.mode(votes)
# print(winner)


# school_report = [
#     ["Český jazyk", 1],
#     ["Anglický jazyk", 1],
#     ["Matematika", 1],
#     ["Přírodopis", 2],
#     ["Dějepis", 1],
#     ["Fyzika", 2],
#     ["Hudební výchova", 4],
#     ["Výtvarná výchova", 2],
#     ["Tělesná výchova", 3],
#     ["Chemie", 4],
# ]
# znamky = []
# predmety = ["Matematika", "Český jazyk", "Anglický jazyk", "Fyzika"]
# for row in school_report:
#         if row[0] in predmety:
#             znamky.append(row[1])
# print(znamky)
# prumer = statistics.mean(znamky)
# print(prumer)


# znamky = []
# dulezite_predmety = ["Český jazyk", "Matematika", "Anglický jazyk", "Fyzika"]
# for row in school_report:
#     # Při prvním běhu
#     # row = ["Český jazyk", 1]
#     # Chci uložit pouze předměty v seznamu dulezite_predmety
#     # Podívej se, jestli je předmět (row[0]) v seznamu dulezite_predmety
#     if row[0] in dulezite_predmety:
#         # row[0] = "Český jazyk"
#         # row[1] = 1
#         znamky.append(row[1])
# print(znamky)
# prumer = statistics.mean(znamky)
# print(prumer)