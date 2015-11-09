number = input("Hey you! Yeah You!! Gimmie a number I can plug into this Fizz Buzz assignment! ")
for n in range(1, int(number) + 1):
    if (n % 3) == 0 and (n % 5) == 0:
        print ("Fizz Buzz")
    elif (n % 3) == 0:
        print ("Fizz")
    elif (n % 5) == 0:
        print ("Buzz")
    else:
        print (n)
print ("Look at all that sweet sweet fizz buzz")