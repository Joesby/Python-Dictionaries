restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

#Task 1: Restaurant Menu Update
#Add a new caregory called "Beverages" with at least two items
restaurant_menu.update({"Beverages": {"Soda": 1.99, "Coffee": 2.99}})

#Update the price of "steak" to 17.99
restaurant_menu.update({"Main Course": {"Steak: 17.99"}})

#Remove "Bruschetta" from "Starters"
#use the delete key word followed by the dictionary name, the first key, then the nested key to remove "Bruschetta"
del restaurant_menu["Starters"] ["Bruschetta"]

#display the changes made to the restaurant menu dictionary
print(restaurant_menu)