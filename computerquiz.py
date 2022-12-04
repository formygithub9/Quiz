def quiz():
    score=0
    answer=input("What is the full form of CPU ? ")
    if answer.lower()=="central processing unit":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    answer=input("What is the full form of RAM ? ")
    if answer.lower()=="random access memory":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    answer=input("What is the full form of BIOS ? ")
    if answer.lower()=="basic input output system":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    answer=input("What is the full form of UPS ? ")
    if answer.lower()=="uninterrupted power supply":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    print("Great... you completed the quiz")
    print("Your score is ",(score/4)*100,"percent")
