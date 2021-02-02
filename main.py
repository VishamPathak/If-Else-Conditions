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

is_Hungry = True
is_Sleepy = False
is_Bored = True
if(is_Hungry == True):
  print("You should go eat")
if(is_Hungry == False):
  print("Wow you're well fed")
if(is_Sleepy == True):
  print("You should go sleep")
if(is_Sleepy == False):
  print("Wow, you are well rested")
if(is_Hungry == is_Bored or is_Sleepy == is_Hungry):
  print("You should do your homework.")
else:
  print("You can play outside.")

if(is_Sleepy == is_Hungry and is_Hungry == is_Bored):
  if(is_Sleepy == is_Bored):
    print("It's nap time.")
else:
  print("It's time for bed.")

# Ask the user for a number
# Tell the user if their number is even or odd

y = int(input("Tell me a number: "))
if (y % 2 != 0):
  print("Your number is odd!")
else:
  print("Your number is even!")


# Math Quadrants 
# Ask the user for an x and a y value

x = int(input("Please give me an x value "))
y = int(input("Please give me an y value "))
# Using a nested conditional, output which quadrant they are in 

if(x > 0):
  if(y > 0):
   print("Your number is in the first quadrant")
elif(x < 0):
 if(y < 0):
   print("Your number is in the third quadrant")
elif(x < 0):
 if(y > 0):
   print("Your number is in the second quadrant")
elif(x > 0):
 if(y < 0):
   print("Your number is in the fourth quadrant")

# create and if statement using "and" or "or" for the third and second quadrant

if(x < 0 and y > 0):
  print("Your number is in the second quadrant")
if(x < 0 and y < 0):
  print("Your number is in the third quadrant")

# let the user know when they are on the x-axis or y-axis
# if we have +y or -y but x == 0
# "You are on the y-axis"
# if we have -x or +x but y == 0
# "You are on the x-axis"

if(x == 0 and )


# if x and y are 0, output the origin

if(x == 0 and y == 0):
   print("You are on the origin")

# and, or
# and takes precendence over or
# "and" both conditions have to be correct
# "or" only one condition has to be correct

x = 5
y = 6
z = 7
if(x == 5 and y == 5 or z ==5):
  print("Yay")
else:
  print("Nay")

if(x ==5 or y == 5 and z == 5):
  print("Yay")
else:
  print("Nay")