'''
  1 for gun
  0 for Knife

'''

                                                                                                                                    
import random
enemy=random.choice([0,1])
youstr=input("Enter your choice :")
youdict={"g":1 ,"k": 0}
revdict={1:"gun", 0:"knife"}

you=youdict[youstr]
print(f"your Choice : {revdict[you]}\nEnemy Choice : {revdict[enemy]}")
if(you==enemy):
    print("Game Draw")

else:
    if(enemy==1 and you==0):
        print("Your are lose")

    elif(enemy==0 and you==1):
        print("Your are win")


