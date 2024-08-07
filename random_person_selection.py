'''Write a program to select a random number from a list of names and the person selected has 
to pay for everybody's food bill'''

import random

delimiter=","  
names_list = input("Enter everybody's name separated by comma ").split(delimiter)
print(names_list)
approach= int(input("Enter the approach"))

match approach:
    case 1:
#Approach 1 (using choice)
        print("Select approach choice")
        selected_person = random.choice(names_list)
        print (f"{selected_person} will pay for everybody's food bill")
    case 2:
#Approach 1 (using randint)
        print("Selecting option randint")
        random_choice= random.randint(0,len(names_list)-1)
        selected_person = names_list[random_choice]
        print (f"{selected_person} will pay for everybody's food bill")
    case 0:
        print("The approach doesn't matter, what matters is solving problems.")

