import time
import random

print('*' * 50)

print('Magic 8 Ball: ')

print()

question = input("What's your question? ")

print()

print("...shaking...")
time.sleep(2)

print()
print('...still shaking...')
time.sleep(2)

choice = random.randint(1,6)

if choice == 1:
	print()
	print("Sure.")

elif choice == 2:
	print()
	print("Ask Again.")

elif choice == 3:
	print()
	print("Nah.")

elif choice == 4:
	print()
	print("Sound like a bad idea.")

elif choice == 5:
	print()
	print("Why are you asking me? It's your life.")

else:
	print()
	print("I guess. But my opinion doesn't really matter...")

print('*' * 50)