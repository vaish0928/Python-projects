from hashlib import *

loginDict = {}
ask = input("Are you already signed up? Type Yes or No: ")
if ask == "Yes":
	login()
elif ask == "No":
	sign_up()

def sign_up():
	name = input("Enter a username: ")
	password = input("Enter a password: ")
	loginDict["name"]= "password"

def login(loginDict):
	user_name = input("Type in your username: ")
	if user_name in loginDict:
		makehash()
	else:
		print ("username not found.") 
		retry = input("Would you like to sign up or retry? ")
		if retry == "sign up":
			sign_up()
		if retry == "retry":
			login()
	
def makehash(password):
	password = input("Enter password: ")
	return sha256(password.encode('utf-8')).hexdigest()
	

	
def prompt():

