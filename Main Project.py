import computerquiz as c
import gkquiz as g
import mathquiz as m
print("Hello...")
answer=input("Do you want to play Quiz ? ")
if answer.lower()!='yes':
    quit()
else:
    print("Select your Subject :","Computer","GK","Mathematics",sep="\n")
    subject=input()
    if subject.lower()=="computer":
        c.quiz()
    elif subject.lower()=="gk":
        g.quiz()
    else:
        m.quiz()
input()