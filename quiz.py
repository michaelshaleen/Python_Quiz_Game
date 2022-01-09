name = input("Name: ")
score = 0

print(f"Welcome to my computer quiz!")

play = input(f"Would you like to play a game {name}? ")

tim = " tim is GREAT"
print(tim.lower())

if play.lower() != "yes":
    quit()

print("Great! Let's play a game :) ")

# Q1
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
  score += 1
  print("Correct!")
else:
  print("Dang foo, you wrong.")


# Q2
answer = input("What does GPU stand for? ")
if answer == "graphic processing unit":
  score += 1

  print("Correct!")
else:
  print("Dang foo, you wrong.")


# Q3
answer = input("What does RAM stand for? ")
if answer == "random access memory":
  score += 1

  print("Correct!")
else:
  print("Dang foo, you wrong.")


# Q4
answer = input("What does PSU stand for? ")
if answer == "power supply":
  score += 1

  print("Correct!")
else:
  print("Dang foo, you wrong.")



print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100 ) + "%")