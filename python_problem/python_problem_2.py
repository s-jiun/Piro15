student_info = {}

class ExistingKeyError(Exception):
    def __init__(self):
        super().__init__("Already exist name!")

class OutOfRangeError(Exception):
    def __init__(self):
        super().__init__("Score must be in range of 0 ~ 100")

class EmptyDictError(Exception):
    def __init__(self):
        super().__init__("No student data!")

class GradingError(Exception):
    def __init__(self):
        super().__init__("There is a student who didn't get grade")

def Menu1(name, mid_score, final_score):
    student_info[name] = [mid_score, final_score]

def Menu2():
    for name in list(student_info.keys()):
        if len(student_info[name]) == 2:
            avg = (student_info[name][0] + student_info[name][1]) / 2
            if avg >= 90:
                student_info[name].append('A')
            elif avg >= 80:
                student_info[name].append('B')
            elif avg >= 70:
                student_info[name].append('C')
            else:
                student_info[name].append('D')
        else:
            continue

def Menu3():
    print("-------------------------------")
    print("name\tmid\tfinal\tgrade")
    print("-------------------------------")
    for name in list(student_info.keys()):
        print("{0}\t{1}\t{2}\t{3}".format(name, student_info[name][0], student_info[name][1], student_info[name][2]))
        

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            name, mid_score, final_score = input("Enter name mid-score final-score :").split()
            mid_score = int(mid_score)
            final_score = int(final_score)
            if name in student_info:
                raise ExistingKeyError
            elif mid_score < 0 or mid_score > 100:
                raise OutOfRangeError
            elif final_score < 0 or final_score > 100:
                raise OutOfRangeError
        except ValueError as e:
            print(e)
        except ExistingKeyError as e:
            print(e)
        except OutOfRangeError as e:
            print(e)
        else:
            Menu1(name, mid_score, final_score)

    elif choice == "2" :
        try:
            if bool(student_info) == False:
                raise EmptyDictError
        except EmptyDictError as e:
            print(e)
        else:
            Menu2()
            print("Grading to all students.")

    elif choice == "3" :
        try:
            if bool(student_info) == False:
                raise EmptyDictError
            else:
                for i in list(student_info.values()):
                    if len(i) != 3:
                        raise GradingError
                    else:
                        continue
        except GradingError as e:
            print(e)
        else:
            Menu3()
