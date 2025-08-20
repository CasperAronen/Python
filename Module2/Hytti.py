paikka = input("Anna hyttiluokkasi (LUX, A, B, C): ")

if paikka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella")
elif paikka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif paikka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella")
elif paikka == "C":
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("virheellinen hyttiluokka")