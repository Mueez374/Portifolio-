total = 0
numbers=[10,20,30,40,50]
total = sum(numbers) 
mean = sum(numbers)/5
print(total)
print(mean) 
# new code underneath 

score= 0
attempt = 2
correctanswer= "green"
while attempt > 0 :
      guess = input("what is the colour of grass")
      if guess== correctanswer :
          score = score + 1
          break 
      else:
            attempt = attempt - 1
            if attempt > 0:
              print("try again")
            else: 
               print("Game over")
print("Your Score is", score)
  
                
           

