#infinite loop -- don't do it - you know you want to ;)

print('This is an infinite loop, suckah!!!')
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print "Number of apples: " + str(numberOfApples)
