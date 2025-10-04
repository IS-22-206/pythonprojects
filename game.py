import  random

print("Welcome to dice roll game")
count=0
while True:
 choice=input("Roll the dice?(y/n)").lower()
 if(choice=="y"):
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(f'you rolled: ({die1},{die2})')
    count=count+1
 elif choice =='n':
    print(f'Thanks for playing,your rolled no is :-{count}')
    break
 else:
   print("invalid choice")






