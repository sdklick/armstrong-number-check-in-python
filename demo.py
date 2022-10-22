# check armstrong number program
userinput = int(input("please enter number : "))
b = str(userinput)
c = len(b)
sum = 0
for x in b:
    multi = 1
    for y in range(0, c):
        z = int(x)
        multi = multi*z
    sum = sum+multi
if sum == userinput:
    print(userinput, "is a armstrong number")
else:
    print(userinput, "is not a armstrong number")