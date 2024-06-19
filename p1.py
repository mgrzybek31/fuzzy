import os
tasks_file = "tasks.txt"
tasks = []


def save_tasks_to_file():
    with open(tasks_file, 'w') as file:
        for task in tasks:
            file.write(task)


def load_tasks_from_file():
    if os.path.exists(tasks_file):
        with open(tasks_file, 'r') as file:
            for line in file:
                tasks.append(line.strip())


def print_options():
    print("1: Add the task\n2: Delete the task\n3: Show the list\n4: Stop")


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task {task} added to list")


def delete_task():
    task = input("Enter the task: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task {task} removed from list")
    else:
        print(f"{task} not in list")


def show_list():
    print(f"The list: {tasks}")


def main():
    print("Good morning")
    load_tasks_from_file()
    while True:
        print("What would you like to do? ")
        print_options()
        choose = int(input("Choose the number: "))
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
                print("Invalid input!")
        except ValueError:
            print("Enter number,not letter!")
    save_tasks_to_file()
    print("Bye!")


if __name__ == '__main__':
    main()
