def quiz():
    score=0
    answer=int(input("300000/____=300 "))
    if answer==1000:
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    answer=int(input("The predecessor of one crore is "))
    if answer==9999999:
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    answer=int(input("____*1000=99820000 "))
    if answer==99820:
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    answer=int(input("(33*3)+(3/3)=____ "))
    if answer==100:
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    answer=int(input("LCM of 3,8 and 9 is ____ "))
    if answer==72:
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    print("Great... you completed the quiz")
    print("Your score is ",(score/5)*100,"percent")
