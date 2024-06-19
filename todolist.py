import os
tasks_file = "tasks.txt"
tasks = []


def load_tasks_from_file():
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as file:
            for line in file:
                tasks.append(line.strip())


def save_tasks_to_file():
    with open(tasks_file, "w") as file:
        for task in tasks:
            file.write(task)


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task {task} added to list")


def delete_task():
    task = input("Enter the task: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task {task} deleted from the list")


def show_list():
    print(tasks)


def show_options():
    print("1: Add a task\n2: Delete a task\n3: Show the list\n4: Stop")


def to_do_list():
    print("Good morning!")
    load_tasks_from_file()
    while True:
        print("What would you like to do?")
        show_options()
        choose = int(input("Enter the number: "))
        try:
            if choose == 1:
                add_task()
            elif choose == 2:
                delete_task()
            elif choose == 3:
                show_list()
            elif choose == 4:
                break
            else:
                print("Please enter correct number. ")
        except ValueError:
            print("Please enter the number. ")
    save_tasks_to_file()
    print("Bye")


if __name__ == "__main__":
    to_do_list()
x