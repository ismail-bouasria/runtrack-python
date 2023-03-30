#job17


for i in range(1,101):
    if i % 3 and i % 5:
        i = "FizzBuzz"
    else:
        if i % 3:
            i = "Fizz"
        else:
            if i % 5:
                i= "Buzz"
    print(i)     
