import random
print("Welcome to number guessing game btw 1 to 100")
number=random.randint(1,100)
count=0
while(True):
  try:
    user=int(input("guess number btw 1 to 100 "))
    if(user<1 or user>100):
      print("Enter btw 1 to 100")
      continue

    count+=1
    if(user==number):
      print(f"Congratulation you guessed the number and the number is {number}")
      print(f"The number of try you have done is {count}")
      break
    elif(user>number):
      print("too high")
    elif(user<number):
       print("too low")

    else:
      print("invalid number")

  except ValueError:
   print("Invalid input give a number which is interger")
      
      
 