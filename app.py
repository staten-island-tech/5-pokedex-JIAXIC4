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
    else:
        print("No Pokémon found matching your search.")




for index, item in enumerate(data, start=0):
    print(index, ":", item["type"])

def what_type(tyyy):
    for mond in data:
        if tyyy in mond["type"]:
            print(mond["name"][language])

tyyy = input("what type do you want? :").capitalize()
what_type(tyyy)


def find_matching_names(search, pokelist, language):
    matches = []

    for mon in pokelist:
        name = mon["name"][language]
        if search.lower() in name.lower():
            matches.append(name)

    if matches:
        print("Matching Pokémon:")
        for m in matches:
            print(m)
    else:
        print("No Pokémon found matching your search.")
pokemon = input("Search for a pokemon: ").strip()
find_matching_names(pokemon, data, language)

pokemon_input = input("Search for a Pokémon: ").strip().lower()

selected_pokemon = None

for mon in data:
    if pokemon_input in mon["name"][language].lower():
        selected_pokemon = mon
        break

if selected_pokemon:
    print(f"\nYou chose: {selected_pokemon['name'][language]}")

    stats_choice = input("Would you like to see this Pokémon's base stats? (yes/no): ").strip().lower()
    if stats_choice == "yes":
        stats = ["HP", "Attack", "Defense", "Sp. Attack", "Sp. Defense", "Speed"]
        print(f"\n{selected_pokemon['name'][language]}'s Base Stats:")
        for stat in stats:
            print(f"{stat}: {selected_pokemon['base'][stat]}")

else:
    print("No Pokémon found matching your search.")
    


# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

