def prime_numbers_fun():
    prime_numbers = []
    actual_number = 2

    while True:
        is_prime = all(actual_number % liczba != 0 for liczba in prime_numbers)

        if is_prime:
            yield actual_number
            prime_numbers.append(actual_number)

        actual_number += 1


generator = prime_numbers_fun()

for _ in range(10):
    print(next(generator))
