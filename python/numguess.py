import random

answer = random.randint(1,100)
print(answer)

username = input("Hi there, What's your name??")
guess = eval(input("Hi, " + username + " guess the number: "))

if guess == answer:
	print("Correct! The answer was" + str(answer))
else:
	print("Wrong")



