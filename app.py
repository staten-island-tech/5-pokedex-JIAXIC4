import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
grass = open("./types.json", encoding="utf8")
data = json.load(pokedex)
typ = json.load(grass)

print(data[0])

print("Welcome to Pokemon Store!")

for index, item in enumerate(data, start=0):
    print(index, ":", item["name"])

language = input("What language do you want? english, chinese, japanese, or french: ").strip().lower()

for mon in data:
    if language in mon["name"]:
        print(mon["name"][language])

for index, item in enumerate(data, start=0):
    print(index, ":", item["type"])

tye = input("what type do you want? :").capitalize()

for mond in data:
    if tye in mond["type"]:
        print(mond["name"][language])

pokemon = input("search for a pokemon: ").capitalize()
list = []
def find_matching_names(pokemo, pokelist):
    pokelist = data["name"]
    pokemo = pokemon
    if pokemo in pokelist:
        list.append(pokemo)


    


# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

