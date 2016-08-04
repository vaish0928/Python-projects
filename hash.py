from hashlib import *

loginDict = {}

	

def prompt():
	name = input("Username: ")
	if name in loginDict:
		password = input("password: ")
		hash = makehash(password)
		done = False
		while not done:
			if hash in loginDict:
				print("Welcome to your account!")
				done = True
			else:
				password = input("password: ")
				hash = makehash(password)
	else:
		login(loginDict)
	

def login(loginDict):
	sign_up = input("Username incorrect. Sign up? Enter username: ")
	password = input("Enter password: ")
	loginDict[sign_up]= password
	password = makehash(password)

def makehash(password):
	return sha256(password.encode('utf-8')).hexdigest()

user = input("Login or Sign Up? Type Login or Signup")
if user== "Login":
	prompt()
elif user == "Signup":
	login(loginDict)
user = input("Do you want to log in? Type Y or N: ")
if user == "Y":
	prompt()

	
	

