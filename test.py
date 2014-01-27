#Essais de génération de grilles pour un Game of Life
import random
stop = False
while not stop:
    while 1:
        grid = [["." for i in range(10)] for j in range(10)]
        k = 0
        while k < 24:
            locOne = random.randint(0,9)
            locTwo = random.randint(0,9)
            if grid[locOne][locTwo] != "0":
                grid[locOne][locTwo] = "0"
                k = k+1
        for row in grid:
            print(row)
        stop = input("> 1 pour continuer, 0 pour quitter : ")
        print("\n")