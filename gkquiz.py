def quiz():
    score=0
    answer=input("Who was the first woman Prime Minister of India ? ")
    if answer.lower()=="indira gandhi":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    answer=input("Name the national bird of the United State of America. ")
    if answer.lower()=="bald eagle":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    answer=input("Name the deepest ocean in the world. ")
    if answer.lower()=="pacific ocean":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    answer=input("Name the gas which is filled in balloons. ")
    if answer.lower()=="helium":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    print("Great... you completed the quiz")
    print("Your score is ",(score/4)*100,"percent")
