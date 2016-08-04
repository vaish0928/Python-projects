Start = print ('''
After you walked into a closet, you were sent into another world called Temple Run. 
You turn around and you no longer see your clothes. You dont see your shoes.
You dont even see your shoes. Instead you see a giant hungry gorrilla chasing you.
There is a hallway to your right and to your left.
''')

print ("start")

print ("Type 'left' to go left or 'right' to go right.")
user_input = input()
done = False
while not done:
	if user_input == "left":
		print("You decide to go left and You run into a tree")
		print("Type 'climb' to climg the tree or 'cut' to cut the tree")
		user_input = input()
		while not done:
			if user_input == "climb":
				print("You jumbed on the Nimbus")
				print("You go to Bowser's castle. Type 'fight' to fight or 'run away' to run away")
				user_input = input()
				while not done:
					if user_input == "fight":
						print("Kill Bowser")
						done = True
					elif user_input == "run away":
						print ("Find Princess Peach")
						done = True
					else:
						print ("Type 'fight' to fight or 'run away' to run away")
						user_input = input()			
			elif user_input == "cut":
				print ("You get killed by an ogre :(")
				done = True
			else:
				print ("Type 'climb' to climg the tree or 'cut' to cut the tree")
				user_input = input()
		done = True
	elif user_input == "right":
		print("You decide to go right and you enter the temple")
		print("Type 'right' to go right and 'left' to go left")
		user_input = input()
		while not done:
			if user_input == "right":
				print("At the end of the hallway, you fall into the waterfall")
				print("You resurface and you continue to swim or find an island. Type 'swim' to swim and 'island' to find an island")
				user_input = input()
				while not done:
					if user_input == "swim":
						print("You find Atlantis!")
						done = True
					elif user_input == "island":
						print("You dance with monkeys and eat coconuts")
						done = True
					else:
						print ("Type 'swim' to swim and 'island' to find an island")
						user_input= input()
				done= True
			elif user_input == "left":
				print("You meet a princess or a prince and live happily ever after")
				done = True
			else:
				print("Type 'right' to go right and 'left' to go left")
				user_input= input()
		done = True
	else:
		print("Type 'left' to go left or 'right' to go right.")
		user_input= input()
print("Game over")
