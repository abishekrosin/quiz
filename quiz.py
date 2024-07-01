print('welcocme to learn witj esprit')

player = input('do you want to play?')

if player.lower() != "yes":
    quit()
score=0
    
print('ok lets play')

question = input("how many days in a week ?")
if question.lower()== "seven":
    print('correct')
    score+=1
    
else:
    print('incorrect')    
    
question = input("what is the national sports in india  ?")
if question.lower() == "hockey":
    print('correct')
    score+=1
    
else:
    print('incorrect')
    
question = input("what is the national animal in india ?")
if question.lower() == "tiger":
    print('correct')
    score+=1
    
else:
    print('incorrect')
    
print("your score"+str(score))    