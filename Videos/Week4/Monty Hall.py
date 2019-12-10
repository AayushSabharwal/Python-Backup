#Monte Hall
import random


swapW = 0
nonSwapW = 0

for i in range(50):
    doors = ["Goat"]*3
    goats = [0, 1, 2]
    win = random.randint(0,2)
    
    doors[win] = "BMW"
    goats.remove(win)
    
    choice = int(input("Enter choice"))
    swap = -1
    if(choice == goats[0]):
        print('Door ', goats[1], ' contains a goat. Press 1 to swap your choice to ', win, ' press 0 to remain')
        swap = win if int(input()) == 1 else choice
    elif(choice == win):
        opened = random.randint(0,1)
        print('Door ', goats[opened], ' contains a goat. Press 1 \
              to swap your choice to ', goats[1-opened], ' press 0 to remain')
        swap = goats[1-opened] if int(input()) == 1 else choice
    else:
            print('Door ', goats[0], ' contains a goat. Press 1 to swap your choice to ', win, ' press 0 to remain')
            swap = win if int(input()) == 1 else choice
    
    if(swap == win):
        print('You won!')
        if(swap == choice):
            nonSwapW = nonSwapW + 1
        else:
            swapW = swapW + 1
    else:
        print('You lose!')

print('Swapping won ', swapW, ' times')
print('Not swapping won ', nonSwapW, ' times')