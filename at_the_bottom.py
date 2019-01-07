n = int(raw_input("Enter a number: "))
numbers = []
while n < 9:
    print "At the top i is %d" % n
    numbers.append(n)
    n = n + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % n
    print "The numbers: "
    for num in numbers:
        print num
