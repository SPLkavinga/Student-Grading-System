pass_01 = 0
defer = 0
fail = 0
running = True
output = 0
dic = {}
dic_list = []
esc = ""
student_key = ""


def name_validation():
    while True:
        try:
            name = int(input("\nEnter student ID: w"))
            name = str(name)
            if len(name) != 7:
                print("Invalid ID")
                continue

            global student_key
            student_key = "w" + name
            break

        except ValueError:
            print("Invalid ID")
            continue


def pas_1():        
    while True:
        try:
            global pass_01
            pass_01 = int(input("\nPlease enter your credit at pass: "))
            if not running:
                continue
            if not 0 <= pass_01 <= 120:
                print("Invalid pass mark,Try again with valid mark")
                continue
            else:
                break
        except ValueError:
            print("Integer required")
            continue


def defer_1():
    while True:
        try:
            global defer
            defer = int(input("Please enter your credit at defer: "))
            if not running:
                continue
            if not 0 <= defer <= 120:
                print("Invalid defer mark,Try again with valid mark")
                continue
            else:
                break
        except ValueError:
            print("Integer required")
            continue


def fail_1():
    while True:
        try:
            global fail
            fail = int(input("Please enter your credit at fail: "))
            if not running:
                continue
            if not 0 <= fail <= 120:
                print("Invalid fail mark,Try again with valid mark")
                continue
            else:
                break
        except ValueError:
            print("Integer required")
            continue


def mark_range():
    if (pass_01 + defer + fail) == 120:
        sub_dic = []
        if pass_01 == 120 and defer == 0 and fail == 0:
            print('Progress')
            result = 'Progress'

            output = str(student_key + " : " + result + " - ")
            sub_dic.append(output)
            sub_dic.append(pass_01)
            sub_dic.append(",")
            sub_dic.append(defer)
            sub_dic.append(",")
            sub_dic.append(fail)

        elif pass_01 == 100 and pass_01 > (defer + fail):
            print("Progress(module trailer)")
            result = "Progress(module trailer)"

            output = student_key + " : " + result + " - "
            sub_dic.append(output)
            sub_dic.append(pass_01)
            sub_dic.append(",")
            sub_dic.append(defer)
            sub_dic.append(",")
            sub_dic.append(fail)

        elif fail > (pass_01 + defer):
            print('Excluded')
            result = 'Excluded'

            output = student_key + " : " + result + " - "
            sub_dic.append(output)
            sub_dic.append(pass_01)
            sub_dic.append(",")
            sub_dic.append(defer)
            sub_dic.append(",")
            sub_dic.append(fail)
        else:
            print('Module retriever')
            result = 'Module retriever'

            output = student_key + " : " + result + " - "
            sub_dic.append(output)
            sub_dic.append(pass_01)
            sub_dic.append(",")
            sub_dic.append(defer)
            sub_dic.append(",")
            sub_dic.append(fail)

        dic_list.append(sub_dic)
        global dic
        dic = dic_list  # list to tupple


def outputs():
    while True:
        print("\nWould you like to enter another set of data? ")
        option = input("Enter 'y' for yes or 'q' to quit and view results Y/q ?")
        option = option.lower()
        if option == "y":
            inputs()

        elif option == "q":
            print("\n****Dictonory****")
            for x in dic:
                for y in x:
                    print(y, end=" ")
                print("\n")
            exit()
        else:
            print("Invalid Input")
            continue

def inputs():
    name_validation()
    pas_1()
    defer_1()
    fail_1()
    mark_range()
    outputs()

inputs()
