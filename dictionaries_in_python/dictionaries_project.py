# Словник для зберігання контактів
contacts = {}

def add_contact():
    """Додає новий контакт у словник."""
    name = input("Введіть ім'я контакту: ")
    if name in contacts:
        print("Контакт з таким іменем вже існує.")
        return
    phone = input("Введіть номер телефону контакту: ")
    email = input("Введіть електронну пошту контакту: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Контакт '{name}' успішно додано.")

def view_all_contacts():
    """Відображає всі контакти."""
    if not contacts:
        print("Книга контактів порожня.")
        return
    print("\n--- Усі контакти ---")
    for name, info in contacts.items():
        print(f"Ім'я: {name}, Телефон: {info['phone']}, Електронна пошта: {info['email']}")
    print("--------------------")

def search_contact():
    """Шукає контакт за іменем."""
    name = input("Введіть ім'я контакту для пошуку: ")
    if name in contacts:
        info = contacts[name]
        print(f"Ім'я: {name}, Телефон: {info['phone']}, Електронна пошта: {info['email']}")
    else:
        print(f"Контакт '{name}' не знайдено.")

def update_contact():
    """Оновлює інформацію про існуючий контакт."""
    name = input("Введіть ім'я контакту для оновлення: ")
    if name in contacts:
        phone = input("Введіть новий номер телефону (залиште порожнім, щоб зберегти поточний): ")
        email = input("Введіть нову електронну пошту (залиште порожнім, щоб зберегти поточну): ")
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        print(f"Контакт '{name}' успішно оновлено.")
    else:
        print(f"Контакт '{name}' не знайдено.")

def main_menu():
    """Відображає головне меню та обробляє ввід користувача."""
    while True:
        print("\nМенеджер контактів")
        print("1. Додати новий контакт")
        print("2. Переглянути всі контакти")
        print("3. Знайти контакт")
        print("4. Оновити контакт")
        print("5. Вийти")
        
        choice = input("Введіть ваш вибір (1-5): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_all_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            print("Вихід з менеджера контактів. До побачення!")
            break
        else:
            print("Неправильний вибір. Будь ласка, введіть число від 1 до 5.")

if __name__ == "__main__":
    main_menu()
