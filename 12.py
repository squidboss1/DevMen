from datetime import datetime

class Note:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.creation_time = datetime.now()

class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
        print("Dodano nową notatkę.")

    def add_existing_note(self, author, content):
        # Dodaj istniejącą notatkę do notatnika
        note = Note(author, content)
        self.notes.append(note)
        print("Dodano istniejącą notatkę.")

    def get_number_of_notes(self):
        return len(self.notes)

    def display_all_notes(self):
        if not self.notes:
            print("Notatnik jest pusty.")
        else:
            print("Wszystkie notatki:")
            for index, note in enumerate(self.notes, 1):
                print(f"\nNotatka {index}:")
                print(f"Autor: {note.author}")
                print(f"Treść: {note.content}")
                print(f"Czas utworzenia: {note.creation_time}")

notebook = Notebook()

# Dodaj nową notatkę
new_note = Note("John Doe", "To jest moja pierwsza notatka.")
notebook.add_note(new_note)

# Dodaj istniejącą notatkę
notebook.add_existing_note("Jane Doe", "To jest moja druga notatka.")


print(f"Liczba notatek: {notebook.get_number_of_notes()}")

notebook.display_all_notes()
