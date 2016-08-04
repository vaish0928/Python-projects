import random
articles = ["The ", "A ", "34", "His ", "Her ", "2 ", "4 ", "8 ", "3 ", "10 "]
adjectives = ["Fierce ", "Jolly ","Agrreable ", "Bloody ", "Screaming ", "Vengeful ", "Raving ", "Pleasant ", "Ecstatic ", "Jubliant "]
nouns = ["Daggers", "Bunnies", "Bears", "Wolves", "Kittens", "Clouds", "Toenails", "Hearts", "Needles", "Clowns"]
articles_length = len(articles)
adjectives_length = len(adjectives)
nouns_length = len(nouns)
random_index = random.randint(0, articles_length - 1)
random_index1 = random.randint(0, adjectives_length - 1)
random_index2 = random.randint(0, nouns_length - 1)
counter = 1
while counter<=10:
	print(counter, ")", articles[random_index], adjectives[random_index1], nouns[random_index2])
	print("Choose this name? Say 'yes' or 'no'")
	user_input = input()
	done = False
	while not done:
		if user_input == "yes":
			print("Congrats! Have fun with your band!")
			counter = 11
			done = True
		elif user_input == "no":
			random_index = random.randint(0, articles_length - 1)
			random_index1 = random.randint(0, adjectives_length - 1)
			random_index2 = random.randint(0, nouns_length - 1)
			counter += 1
			done = True
		else:
			print("Say 'yes' or 'no'")
			done = True
			
			

