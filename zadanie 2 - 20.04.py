zdanie = input("Podaj zdanie: ")
slowa = zdanie.split()
odwrocone_slowa = slowa[::-1]
odwrocone_zdanie = " ".join(odwrocone_slowa)
print(odwrocone_zdanie)