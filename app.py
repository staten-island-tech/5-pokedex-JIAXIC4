import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

print("Welcome to Jiaxi's Store! Select an item to purchase!:")

for index, item in enumerate(data, start=0):
    print(index, ":", item["name"])

language = input("What language do you want?")

for index, item in enumerate(data, start=0):
    print(index, ":", item[language])

cart = []
total = 0
done = "no"

while done == "no":
    purchase = input("What would you like to buy? : ").strip().lower()
    found = False
    for items in item:
        if purchase == data["Name"].strip().lower(): 
            cart.append(items) 
            total += items["Price"]   
            done = input("Are you done with your purchase?")
            found = True
            break
    
    if not found:
        print("Your Item is not avalible in this store")
        done = input("Are you done with your purchase?")

if done == "yes":
    print("Here are the items in your cart")
    for items in cart:
        print("-", items)
    print("Total: $", total)




# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

