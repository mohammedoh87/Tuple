weather = (1,0,0,0,1,1,0)
rainy = 0
sunny = 1

for i in range(0,7):
    if weather[i] == 1:
        rainy = rainy + 1
    else:
        sunny = sunny + 1

if(sunny > rainy):
    print("Good weather")
else:
    print("Bad weather")
    
