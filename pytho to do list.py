def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Wyświetl wszystkie zadania")
    print("2. Dodaj nowe zadanie")
    print("3. Usuń zadanie")
    print("4. Zakończ program")

def display_tasks(tasks):
    if len(tasks) == 0:
        print("Brak zadań na liście.")
    else:
        print("\nLista zadań:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Wpisz treść zadania: ")
    tasks.append(task)
    print(f"Zadanie '{task}' zostało dodane.")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Podaj numer zadania do usunięcia: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Zadanie '{removed_task}' zostało usunięte.")
        else:
            print("Niepoprawny numer zadania.")
    except ValueError:
        print("Proszę podać numer.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Wybierz opcję (1-4): ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Zakończenie programu.")
            break
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
