olyV = int(input("Anna olympia vuosi: "))

if olyV % 4 == 0 and olyV != 2020 and olyV != 2021:
    print("Vuosi", olyV, "on olympiavuosi")
elif olyV == 2020:
    print("Vuosi", olyV, "ei ollut ollympialaisia koronan takia")
elif olyV == 2021:
    print("Vuosi", olyV, "oli olympia vuosi koronantakia")
else:
    print("Vuosi", olyV, "ei ole olympiavuosi")