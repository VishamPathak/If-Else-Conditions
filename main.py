a = 200
b = 33

if (b > a): 
  print("b is greater than a")
else: 
  print("b is not greater than a")

# Write a conditional statement that evaluates if the user input is positive or negative

y = int(input("Tell me a number: "))
if (y > 0):
  print("I see that your number is positive")
elif (y == 0):
 print("You entered 0 which is not negative or a postive.")
else:
  print("I see that your number is negative")

# Ask the user for their age
# If they are younger than 13, tell them they can only watch PG/G movies
# If they are 13 and older but younger than 17, they can only watch PG-13/PG/G movies
# If they are 17 and older, they can watch all movies

z = int(input("What is your age? "))
if (z < 13):
  print("That means you can only watch PG/G movies")
elif (17 > z >= 13):
  print("That means you can watch PG-13/PG/G movies")
else:
  print("That means you can watch all movies")

is_Hungry = False
is_Sleepy = False
if(is_Hungry == True):
  print("You should go eat")
if(is_Hungry == False):
  print("Wow you're well fed")
if(is_Sleepy == True):
  print("You should go sleep")
if(is_Sleepy == False):
  print("Wow, you are well rested")

