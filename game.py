import random
option=["rock","sessor","paper"]
player="True"
while(player=="True"):
    p1=input("choose your option:\t")
    c1=random.choice(option)
    print("system option:\t",c1)
    if c1==p1:
        print("Tie")
    elif c1=="rock" and p1=="sessor":
        print("system wins")
    elif c1=="rock" and p1=="paper":
        print("player wins")
    elif c1=="sessor" and p1=="rock":
        print("player wins")
    elif c1=="sessor" and p1=="paper":
        print("system wins")
    elif c1=="paper" and p1=="sessor":
        print("player wins")
    elif c1=="paper" and p1=="rock":
        print("system wins")
    else:
        print("invalid")
    
