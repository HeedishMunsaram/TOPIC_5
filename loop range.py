# a basic for loop with range()
for x in range(0,10):
    print("Day" , x)

# range() with for
how_many = int(input("Run the loop how many times: "))
x = 0

for number in range(0, how_many):
    print(x)

# range with step
for x in range(2,20,2):
    print("Day" , x)

#range with negative step
for x in range(20,2,-2):
    print("Day" , x)