def fizzbuzz(b):
    a=[1,2,3]

    if(len(a+b)%3 == 0) and (len(a+b)%5==0) :
        print("\tfizzbuzz")
    elif (len(a+b)%3) == 0:
        print("\tfizz")
    elif (len(a+b)%5) == 0: 
        print("\tbuzz")
    elif(len(a+b)%3 == 0) and (len(a+b)%5==0) :
        print("\tfizzbuzz")
    else:
        print(len(a+b))