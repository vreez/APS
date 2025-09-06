word = input()
dic = {"Pokemon":"Pikachu", "Digimon":"Agumon", "Yugioh":"Black Magician"}
if word == "Pokemon":
    print(dic["Pokemon"])
elif word == "Digimon":
    print(dic["Digimon"])
elif word == "Yugioh":
    print(dic["Yugioh"])
else:
    print("I don't know")