import random

ran_num = random.randint(0,10)
chance = 3
flag = False
while chance!=0 :
    guss_num = int(input(f"Chance : {chance}/3\nEnter Number in range 0 to 10 : "))
    if guss_num == ran_num :
        print("Wow ! You Win ...")
        flag = True
        break
    elif guss_num == ran_num-1:
        print("near ...")
    else :
        chance -= 1

if ~flag :
    print(f"Number : {ran_num}")