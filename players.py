done = False
print("Player 1, please type a number between 5 and 20")
player_1 = int(input())
while not done:
	if player_1 >= 5 and player_1 <= 20:
		done = True
	else:
		print("Player 1, please type a number between 5 and 20")
		player_1 = int(input())
print("Player 2, please guess the number that player 1 guessed between the numbers 5 and 20")
player_2 = int(input())
done1 = False
while not done1:
	if player_2 >=5 and player_2 <= 20:
		done1 = True
	else:
		print("Player 2, please guess the number that player 1 guessed between the numbers 5 and 20")
		player_2 = int(input())
done2 = False
while not done2:
	if player_1 == player_2:
		print("You rock! That's correct!")
		done2 = True
	else:
		print("Bummer! Guess Again!.")
		player_2 = int(input())
