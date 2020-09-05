# This is my awesome app, and it will help to calculate the moving cost
distance = input("please input the total distance in KM: ")
distance = int(distance)
layout = input('INPUt 1 if your layout is 1LDK or 2 if it is 2LDK: ')
layout = int(layout)
if(layout == 1):
    base_cost = 8000
elif(layout == 2):
    base_cost = 12000
else:
    base_cost = 10000

# where x is total amount 
x = input("how many items in your house? ")
x = int(x)

# This 1000 and 100 are based on the average stats from www.bala.com  
COST = base_cost + distance * 1000 + x * 100
print("The total cost is {}, thank you so much".format(COST)) 