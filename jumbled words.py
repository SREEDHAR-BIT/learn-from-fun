import random
from getpass import getpass
print("WELCOME TO LEARN FROM FUN")
words=["INDEPENDENCE","FREEDOM","RAINBOW","RESPONSIBILITY"]
pp=0
cp=0
pp1=0
pp2=0
turn=0
player_selection=int(input("Press 1 to play with computer or Press 2 to play with your friend "))#Player selection
if player_selection == 1:
     player_name=input("Enter your name ")
     while(1):
         #to make computer choice
         rand=random.choice(words)
         rand_list=list(rand)
         random.shuffle(rand_list)
         shuf=''.join(rand_list)
         if turn%2==0:
              print(shuf)
              a=input("Guss the word ") 
              b=a.upper()
              if b==rand:
                   pp=pp+1
                   print(player_name,"Won the match ")
              else:
                   cp=cp+1
                   print("computer won the match ") 
         decision=int(input("Do you want to continue the game if yes press 1 else press 2 "))#continue the game
         if decision==1:
              print("your score=", pp ,"computer score is",cp ) 
         else:
              print("your score=", pp ,"computer score is",cp ) 
              print("HAVE A GREAT DAY")
              break
         
else:
     p1=input("Enter the player 1 name ")
     p2=input("Enter the player 2 name ")
     turn=0
     while(1):
          turn=turn+1
          if turn%2==0:
               turn=turn+1
               print(p1)
               input_word=getpass(" Enter the word which is in your mind ")
               input_word_list=list(input_word)
               random.shuffle(input_word_list)
               shuff="".join(input_word_list)
               print(shuff)
               print(p2)
               player_guss=input("Enter your guss ")
               if input_word==player_guss:
                    print(p2," won the match ")
                    pp2=pp2+1
               else:
                    print(p1," won the match ")
                    pp1=pp1+1
                    
          
          else:
               print(p2)
               input_word=getpass(" Enter the word which is in your mind ")
               input_word_list=list(input_word)
               random.shuffle(input_word_list)
               shuff="".join(input_word_list)
               print(shuff)
               print(p1)
               player_guss=input("Enter your guss ")
               if input_word==player_guss:
                    print(p1," won the match ")
                    pp1=pp1+1
                    
               else:
                    print(p2," won the match ")
                    pp2=pp2+1
                    
                    
          
          decision=int(input("Do you want to continue the game if yes press 1 else press 2 "))#continue the game
          if decision==1:
               turn=turn+1   
               print(p1,"your score is=",pp1 ,p2," your score is",pp2 )  
          else:
               print(p1,"your score is=",pp1 ,p2," your score is",pp2 )
               print("HAVE A GREAT DAY")
               break