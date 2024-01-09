class DivisionByZeroError(Exception):
    def __str__(self):
        print("Division by zero")


class InvalidInputError(Exception):
    def __str__(self):
        print("Invalid input")


def example1():
    for i in range(3):
        try:
            x = int(input("Enter a number: "))
            y = int(input("Enter another number: "))

            if y == 0:
                raise DivisionByZeroError("Error: Division by zero is not allowed.")

            print(x, '/', y, '=', x / y)

        except ValueError:
            print("Error: Please enter integers.")
        except DivisionByZeroError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []

    try:
        for i in range(len(L)):
            sumOfPairs.append(L[i] + L[i + 1])

    except TypeError as e:
        print(f"Error: {e}. Make sure the list contains only numeric values.")
    except ValueError:
        print("Error: Please give me integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    else:
        print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    file = open(fileName, "r")
    try:
        for line in file:
            print(line.upper())

    except FileNotFoundError:
        print(f"Error: File '{fileName}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while trying to read file '{fileName}'.")
    except Exception as e:
        print(f"An unexpected error occurred while reading file '{fileName}': {e}")

    finally:
        file.close()
        print("File closed.")



def main():
    example1()

    L = [10, 3, 5, 6, 9, 3]
    example2(L)

    example2([10, 3, 5, 6, "NA", 3])

    printUpperFile("doesNotExistYet.txt")
    printUpperFile("./Desssktop/misspelled.txt")


if __name__ == "__main__":
    main()

