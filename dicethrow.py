import random
number=0
while True:
    number+=1
    r=random.randrange(1,7)
    print(number,r)
    if r==6:
        break
print (f"It took {number} throws to get a 6")
    
        