# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }
# for key in sales:
#     print(key)

# for key, value in sales.items():
#     print(value)

# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }
# total_sales = 0
# for key, value in sales.items():
#     print(f"Knihy {key} bylo prodáno {value} kusů.")
#     total_sales = total_sales + value
#     # total_sales += value
# print(f"Celkem bylo prodáno {total_sales} kusů.")

# book = {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018}
# #  Nakladatele zajímá, jaké jsou peněžní tržby za knihy vydané v roce 2019.
# books = [
#     {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
#     {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
#     {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
# ]
# total_sales = 0
# for item in books:
#     if item['year'] ==2019:
#     # print(item['title'])
#         total_sales = total_sales + item['sold']*item['price']
# print(total_sales)

# school_report = {
#     "Český jazyk": 1,
#     "Anglický jazyk": 1,
#     "Matematika": 1,
#     "Přírodopis": 2,
#     "Dějepis": 1,
#     "Fyzika": 2,
#     "Hudební výchova": 4,
#     "Výtvarná výchova": 2,
#     "Tělesná výchova": 3,
#     "Chemie": 4,
# }
 
# # Výpočet průměrné známky
# average_grade = sum(school_report.values()) / len(school_report)

# # Výpis průměrné známky
# print(f"Průměrná známka ze všech předmětů je: {average_grade}")

# Iterace přes předměty a jejich známky ve slovníku
# for predmet, znamka in school_report.items():
#     if znamka == 1:  # Kontrola, zda je známka rovna 1
#         print(predmet)

# books = [
#     {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
#     {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
#     {"title": "Past", "pages": 390, "rating": 4},
#     {"title": "Popel popelu", "pages": 411, "rating": 10},
#     {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
#     {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
#     {"title": "Zločinný steh", "pages": 542, "rating": 8},
#     {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
#     {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
# ]
# pocet_stran = 0
# for item in books:
#     pocet_stran = pocet_stran + item['pages']
# print(pocet_stran)    

# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
# pocet_knih = 0
# for item in books:
#     if item['rating'] >=8:
#      pocet_knih = pocet_knih + 1
# print(pocet_knih)

plates = {"4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"}



