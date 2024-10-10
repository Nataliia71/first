#number_of_tickets = input("Kolik si přejete lístků? ")
#price_per_ticket = 345
#total_price = number_of_tickets * price_per_ticket
#print(total_price)- видасть 345 разів 25, тому що цепочка - ретезец


#number_of_tickets = input("Kolik si přejete lístků? ")
#price_per_ticket = 345
# Změníme typ proměnné number_of_tickets z řetězce na číslo
#number_of_tickets = int(number_of_tickets)
#total_price = number_of_tickets * price_per_ticket
#print(total_price)



# play = "Každý má svou pravdu"
# number_of_tickets = int(input("Kolik si přejete lístků? "))
# price_per_ticket = 345
# total_price = price_per_ticket * number_of_tickets
# print(f"Cena {number_of_tickets} lístků na hru {play} je celkem {total_price} Kč.")

# teplota_v_F = int(input("Zadejte sve cislo:"))
# teplota_v_C = 5 * (teplota_v_F- 32 ) / 9
# print(f"Teplota v Celsiu: {teplota_v_C}")

# number_of_tickets = int(input("Kolik si přejete lístků? "))
# price_per_ticket = 195.60
# total_price = number_of_tickets * price_per_ticket
# if total_price >= 500:
#     discount = 0.1
#     total_price = total_price * (1 - discount)
#     print(f"Získáváte slevu {discount * 100} %")
# total_price = round(total_price,0)
# print(f"Celková cena nákupu je {total_price} Kč.")






# flight_number = input("Zadejte číslo letu: ")
# prefix = flight_number[0] + flight_number[1]
# if prefix == "BA":
#     company = "British Airways"
# elif prefix == "LH":
#     company = "Lufthansa"
# else:
#     company = "Neznámá společnost"
# print(f"Letíte se společností {company}")


# guest_list = ["Jirka", "Klára", "Natálie"]

# new_guest = input("Zadej jméno dalšího hosta: ")
# guest_list.append(new_guest)
# print(guest_list)
# print(len.guest_list)


school_marks = [
    ["Jiří", 1, 4, 3, 2],
    ["Natálie", 2, 3, 4, 3],
    ["Tereza", 1, 1, 2, 1],
]

print(f"První student(ka) v seznamu je {school_marks[0][0]}.")
print(f"Její/jeho poslední známka je {school_marks[0][-1]}.")