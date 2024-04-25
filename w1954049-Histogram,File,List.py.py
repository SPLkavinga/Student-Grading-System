pass_01 = 0
defer = 0
fail = 0
a = 0
b = 0
c = 0
d = 0
result = ""
running = True
star = 0
name = 0
outcome_list = []
all_result = ""



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


def inputs():
    pas_1()
    defer_1()
    fail_1()
    mark_range()


def mark_range():
    file = open('TEXT file.txt', 'a+')
    if (pass_01 + defer + fail) == 120:
        global result
        global all_result
        if pass_01 == 120 and defer == 0 and fail == 0:
            print('Progress')
            result = 'Progress'
            file.write('Progress -')
            outcome_list = [pass_01, defer, fail]
            all_result += result + '-' + str(outcome_list[0]) + ',' + str(outcome_list[1]) + ',' + str(outcome_list[2])+ '\n'
            global a
            a += 1

        elif pass_01 == 100 and pass_01 > (defer + fail):
            print('Progress(module trailer)')
            result = 'Progress(module trailer)'
            file.write('Progress(module trailer)')
            outcome_list = [pass_01, defer, fail]
            all_result += result + '-' + str(outcome_list[0]) + ',' + str(outcome_list[1]) + ',' + str(outcome_list[2])+ '\n'
            global b
            b += 1

        elif fail > (pass_01 + defer):
            print('Exclude')
            result = 'Excluded'
            file.write('Excluded -')
            outcome_list = [pass_01, defer, fail]
            all_result += result + '-' + str(outcome_list[0]) + ',' + str(outcome_list[1]) + ',' + str(outcome_list[2])+ '\n'
            global c
            c += 1

        else:
            print('Module retriever')
            result = 'Module retriever'
            file.write('Module retriever')
            outcome_list = [pass_01, defer, fail]
            all_result += result + '-' + str(outcome_list[0]) + ',' + str(outcome_list[1]) + ',' + str(outcome_list[2])+ '\n'
            global d
            d += 1
    else:
        print('Total incorrect.')

    file.write(str(pass_01) + "," + str(defer) + "," + str(fail) + "\n")  # writing data in the Text File
    file.close()


def outputs():
    while True:
        print("\nWould you like to enter another set of data? ")
        option = input("Enter 'y' for yes or 'q' to quit and view results Y/q ?")
        option = option.lower()

        if option == "y":
            inputs()

        elif option == "q":

            print("\n****Histogram****")
            print('Progress',a,':',a*'*')
            print('trailer',b,':',b*'*')
            print('retriever',d,':',d*'*')
            print('Excluded',c,':',c*'*')
            
            addition = a + b + c + d
            print(addition, "outcomes in total.")
            print("-" * 55)

            print("\n****List****")

            outcome_list = [pass_01, defer, fail]
            global all_result
            print(all_result)
            print("-" * 55)

            print("\n****Text File****")
            
            file = open('TEXT file.txt', 'w')
            file.write(all_result)
            file.close()
            
            file = open('TEXT file.txt', 'r')
            print(file.read())
            print("-" * 55)           

            esc = input("\n\nDo yo want to exit?(yes / no) :")
            esc = esc.lower()
            if esc == 'yes':
                print("Thank you!")
                break
            else:
                continue
            
inputs()
outputs()

