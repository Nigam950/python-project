import random
n= random.randint(1,100)
a=-1
guesses=0
while(a != n):
 guesses+=1
 a=int(input("Guess the random number:"))
 if(a>n):
  print("Guess lower number:")
 elif(a<n):
  print("Guess higher number:")

print(f"you guesses number correctly in {guesses} attempt")


