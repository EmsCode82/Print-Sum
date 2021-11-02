print ("Welcome to programming")

#inputs
first_number = float(input("Enter first number  "))
second_number = float(input("Enter second number  "))

#process
sum = first_number + second_number

#if-then
if (sum > 10):
    print ("too much")
else:
    #output
    print ("Sum =", sum)

    #loop
    for i in range(int(sum)):
        print (i)
