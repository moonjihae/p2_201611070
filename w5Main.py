def grade():
    g=input("get your score:")
    grade=int(g)
    if 100>grade>=90:
        print ("A")
    if 90>grade>=80:
        print("B")
    if 80>grade>=70:
        print("C")
    if 70>grade>=60:
        print("D")
    if 60>grade:
        print("F")
grade()
