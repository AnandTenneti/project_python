import random
for i in range(5):
    # Generate a random number between 1 and 2
    coin_spin= random.randint(1,2)
    if coin_spin==1:
        print(coin_spin, "Heads")
    else: 
        print(coin_spin,"Tails")  