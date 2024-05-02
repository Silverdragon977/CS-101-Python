#Things that need to be covered:
#   For loops
#   range()
#   While loops
#   incrementation


number     = int(input("Enter in a number:\n"))
timesToAdd = int(input("Enter a multiplier:\n"))
start      = 1
stop       = timesToAdd
total      = 0
print(f"Adding {number}, {timesToAdd} times!")


for i in range(start,stop + 1):
    total += number
    print("Round" + str(i) + " adding " + str(number) + " to total")


print(f"The total is {total}")