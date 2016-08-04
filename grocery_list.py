print("Welcome to Shoprite!")
groceries = {}

def create_list ():
	choice = input("Would you like to add an item? Type Y or N: ")
	if  choice == "Y":
		add_item()

def add_item():
	done = False
	item = input("What item would you like to add? ")
	quantity = input("How many " + item + "s would you like to add?")
	groceries[item] = quantity
	while not done:
		choice1 = input("Would you like to add another item? Type Y or N: ")
		if choice1 == "Y":
			item = input("What item would you like to add? ")
			quantity = input("How many " + item + "s would you like to add?")
			groceries[item] = quantity
		elif choice1 == "N":
			done= True
	choice = input("Would you like to update the quantity of an item? Type Y or N: ")
	if choice == "Y":
		update_item()
	elif choice == "N":
		choice2 = input("Would you like to delete an item? Type Y or N: ")
		if choice2 == "Y":
			delete_item()
		elif choice2 == "N":
			choice3 = input("Would you like to see the list? Type Y or N: ")
			if choice3 == "Y":
				print_list()
	
		

def update_item():
	item = input("What item would you like to update? ")
	if item in groceries:
		quantity = input ("How many " + item + "s do you want now?")
		groceries[item] = quantity
	else:
		print("Item not found.") 
		new_item = input("Would you like to add " + item + " to your groceries? Type Y or N: ")
		if new_item == "Y":
			add_item()			
	 
	done = False
	while not done:
		choice1 = input("Would you like to update another item? Type Y or N: ")
		if choice1 == "Y":
			item = input("What item would you like to update? ")
			quantity = input ("How many " + item + "s do you want now?")
			groceries[item] = quantity
		elif choice1 == "N":
			done = True
	choice = input("Would you like to delete an item? Type Y or N: ")
	if choice == "Y":
		delete_item()
	

def delete_item():
	item = input("What item would you like to delete from the list? ")
	del groceries[item]
	done = False
	while not done:
		choice1 = input ("Would you like to delete another item? Type Y or N: ")
		if choice1 == "Y":
			item = input("What item would you like to delete from the list? ")
			del groceries[item]
		elif choice1 == "N":
			done = True
	choice = input("Would you like to see the list? Type Y or N: ")
	if choice == "Y":
		print_list()
def print_list():
		print(groceries)
	
create_list ()