def min_max_brightness(data):
    min_brightness = min(min(row) for row in data)
    max_brightness = max(max(row) for row in data)
    return min_brightness, max_brightness


def min_rows_to_remove(data):
    symmetry_rows = sum(1 for row in data if row[0] == row[-1])
    return len(data) - symmetry_rows


def contrast_pixels(data):
    contrast_pixels_count = 0

    for column in range(len(data) - 1):
        for line in range(len(data[column]) - 1):

            contrast_with_pixel_below = abs(data[column][line + 1] - data[column][line])
            contrast_with_pixel_on_the_right = abs(data[column][line] - data[column + 1][line])

            def is_above_treshold(contrast):
                return contrast > 128

            if is_above_treshold(contrast_with_pixel_below) or is_above_treshold(contrast_with_pixel_on_the_right):
                contrast_pixels_count += 1

    return contrast_pixels_count


def max_vertical_length(data):
    max_length = 0

    for col in range(len(data[0])):
        current_length = 1
        for row in range(len(data) - 1):
            if data[row][col] == data[row + 1][col]:
                current_length += 1
            else:
                current_length = 1
            max_length = max(max_length, current_length)

    return max_length


with open('dane.txt', 'r') as file:
    lines = file.readlines()


# data = [list(map(int, line.split())) for line in lines]
def parse(lines):
    data = []

    for line in lines:
        # Rozbijanie linii na elementy za pomocą metody split
        elements = line.split()

        # Utworzenie nowej listy, w której każdy element jest skonwertowany na liczbę całkowitą
        int_elements = list(map(int, elements))

        # Dodanie skonwertowanej listy do głównej listy danych
        data.append(int_elements)

    return data


data = parse(lines)

with open('wyniki6.txt', 'w', encoding="utf-8") as output_file:
    min_brightness, max_brightness = min_max_brightness(data)
    output_file.write(f"1. Najciemniejszy piksel: {min_brightness}, Najjaśniejszy piksel: {max_brightness}\n")

    min_rows = min_rows_to_remove(data)
    output_file.write(f"2. Najmniejsza liczba wierszy do usunięcia: {min_rows}\n")

    contrast_pixels_count = contrast_pixels(data)
    output_file.write(f"3. Liczba pikseli kontrastujących: {contrast_pixels_count}\n")

    max_vertical = max_vertical_length(data)
    output_file.write(f"4. Najdłuższa linia pionowa: {max_vertical}\n")
