class Manager:
    def __init__(self):
        self.menu = Menu()
        self.notes_submanager = NotesSubManager()
        self.cards_submanager = CardsSubManager()

    def start(self):
        while True:
            self.welcome_screen()
            choice = self.menu.get_choice()
            self.execute(choice)

    def welcome_screen(self):
        self.menu.show_menu()

    def execute(self, choice):
        match choice:
            case 1:
                self.notes_submanager.add()
            case 2:
                self.cards_submanager.add()
            case 3:
                self.show_notes()
            case 4:
                self.show_cards()
            case 5:
                print("Zakończono.")
                exit()
            case _:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

    def show_notes(self):
        self.notes_submanager.show()

    def show_cards(self):
        self.cards_submanager.show()


class Menu:
    def show_menu(self):
        print("""\
        Menu:
        1. Dodaj notatkę
        2. Dodaj wizytówkę
        3. Wyświetl wszystkie notatki
        4. Wyświetl wszystkie wizytówki
        5. Wyjdź
        """)

    def get_choice(self):
        try:
            choice = int(input("Którą opcję Pan/Pani wybiera?: "))
            return choice
        except ValueError:
            print("Nieprawidłowy wybór. Wprowadź liczbę.")


class NotesSubManager:
    def __init__(self):
        self.notes_list = []

    def add(self):
        content = input("Wprowadź treść notatki: ")
        note = Note(content)
        self.notes_list.append(note)
        print("Dodano notatkę.")

    def show(self):
        if not self.notes_list:
            print("Brak notatek.")
        else:
            print("Notatki:")
            for note in self.notes_list:
                print(note)


class CardsSubManager:
    def __init__(self):
        self.cards_list = []

    def add(self):
        name = input("Wprowadź imię: ")
        phone = input("Wprowadź numer telefonu: ")
        card = Card(name, phone)
        self.cards_list.append(card)
        print("Dodano wizytówkę.")

    def show(self):
        if not self.cards_list:
            print("Brak wizytówek.")
        else:
            print("Wizytówki:")
            for card in self.cards_list:
                print(card)


class Note:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"Note content: {self.content}"


class Card:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Card content: {self.name} - {self.phone}"


if __name__ == "__main__":
    manager = Manager()
    manager.start()

