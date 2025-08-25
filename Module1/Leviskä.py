leviskä = float(input("anna levisköjen määrä: "))
naula = float(input("anna naulojen määrä: "))
luoti = float(input("anna luotien määrä: "))

naulaP = (leviskä * 20)
LuotiP = ((naula + naulaP) * 32)
grammat = ((luoti + LuotiP) * 13.3)
kilot = int (grammat // 1000)
tgram = int (grammat % 1000)

print("Yhteen lasketut kilot " ,kilot , "grammat" , tgram)

#expected_grams = (talents * 20 * 32 + pounds * 32 + lots) * 13.3
#kilograms =  int(expected_grams // 1000)
#total_grams = (expected_grams % 1000)
#remaining_grams =round(total_grams, 2)
#print("The weight in modern units:" ,kilograms , "kilograms and" ,remaining_grams,"grams.")
#print(expected_grams)