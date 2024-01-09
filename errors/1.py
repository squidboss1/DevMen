class FileHandler:
    def __init__(self, file_path, no_connectors, max_file_size):
        self.set_file_path(file_path)
        self.set_no_connectors(no_connectors)
        self.set_max_file_size(max_file_size)

    def set_file_path(self, file_path):
        self.file_path = file_path

    def set_no_connectors(self, no_connectors):
        if not (0 <= no_connectors <= 10):
            raise ValueError("Error: noConnectors must be between 0 and 10!")

        self.no_connectors = no_connectors

    def set_max_file_size(self, max_file_size):
        if not (1000 <= max_file_size <= 9999):
            raise ValueError("Error: maxFileSize must be a four-digit number!")

        self.max_file_size = max_file_size

    def read_content(self):
        print(f"Reading content from file: {self.file_path}")

    def save_to_file(self, content):
        print(f"Saving content to file: {self.file_path}")
        print(f"Content: {content}")


file_handler = FileHandler("example.txt", 5, 3000)
file_handler.read_content()
file_handler.save_to_file("Hello, this is a dummy content.")
