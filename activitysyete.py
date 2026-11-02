# 1. Create a list of 4 grocery items.
Grocery_list = ["Milo", "Bearbrand", "Nescafe", "Chitos"]
print(Grocery_list) # display all items
print("Items list length: ", len(Grocery_list)) # display the number of items
# 2. Update the 2nd item using its index.
Grocery_list[1] = "Absolute"
# 3. Remove one item by name, then remove the last item
Grocery_list.remove("Chitos")
removed = Grocery_list.pop()
print("Removed item: ", removed)
# 4. Ask the user for a new item and add it to the end.
new_item = input("Enter a new item: ")
Grocery_list.append(new_item)
# 5. Add more item to the front
Grocery_list.insert(0, "Coke")
# 6. Print the final list and check an item.
print(Grocery_list)
print("Is Coke in the list?: ", "Coke" in Grocery_list)