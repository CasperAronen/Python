leviskä = float(input("anna levisköjen määrä: "))
naula = float(input("anna naulojen määrä: "))
luoti = float(input("anna luotien määrä: "))

naulaP = (leviskä * 20)
LuotiP = ((naula + naulaP) * 32)
grammat = ((luoti + LuotiP) * 13.3)
kilot = int (grammat // 1000)
tgram = int (grammat % 1000)

print("Yhteen lasketut kilot " ,kilot , "grammat" , tgram)