grocery_list = []
print("Please type in grocery items and then 'All done' once you are finished")
user_input = input()
done = False
while not done:
    if user_input == "All Done":
        done = True
    else:
        grocery_list.append(user_input)
        print(grocery_list)
        user_input = input()
        
