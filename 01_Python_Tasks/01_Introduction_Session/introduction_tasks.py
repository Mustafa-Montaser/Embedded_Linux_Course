def run_task_1():
    given_list = []
    list_len = int(input("Enter number of list elements: "))
    for ele in range(0, list_len):
        given_list.append(int(input("Enter element of index " + str(ele) + " : ")))
    else:
        print("Number 4 is repeated in given list for " + str(given_list.count(4)) + " times.")


def run_task_2():
    letter = input("Enter a letter to be checked if it's a vowel letter or not: ")
    if letter.lower() in "aeiou":
        print("Letter " + str(letter) + " is a vowel letter")
    else:
        print("Letter " + str(letter) + " is not a vowel letter")


def run_task_3():
    import os
    print("Current CWD is: " + os.getcwd())


def run_task_4():
    from math import pi
    radius = float(input("Enter radius value: "))
    print("Circle Area = " + str(pi * (radius ** 2)) + " unit square")

def run_task_null():
    print("Error task ID")


def run_task_5():
    import calendar
    y = int(input("Enter year: "))
    m = int(input("Enter month: "))
    print(calendar.month(y, m))

def select_task(task_id):
    tasks = {
        1: run_task_1,
        2: run_task_2,
        3: run_task_3,
        4: run_task_4,
        5: run_task_5,
    }
    if task_id in range(0, (len(tasks.keys()) + 1)):
        tasks[task_id]()
    else:
        run_task_null()


if __name__ == "__main__":
    print("Task 1: Count number 4 in given list")
    print("Task 2: Test a vowel letter")
    print("Task 3: Access environemt variable. Get CWD")
    print("Task 4: Circle Area calculator")
    print("Task 5: Calender for given year and month")

    select_task(int(input("Enter task ID: ")))




